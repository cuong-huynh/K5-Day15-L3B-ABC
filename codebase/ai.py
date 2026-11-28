"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
# Tuỳ chọn: ghi đè URL (vd endpoint dedicated FPT). Để trống = dùng URL mặc định theo provider.
API_BASE = (os.environ.get("API_BASE") or "").strip().rstrip("/")

SHOW_RAW = False   # đổi thành True để in nguyên phản hồi của API khi cần tìm tên trường

# Provider dạng OpenAI chat/completions
URLS = {
    "groq": "https://api.groq.com/openai/v1/chat/completions",
    "fpt": "https://token-api.fpt.ai/v1/chat/completions",   # FPT AI Factory serverless
    "openai": "https://api.openai.com/v1/chat/completions",
    "deepseek": "https://api.deepseek.com/chat/completions",
}


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json", "User-Agent": "lab-client/1.0"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def chat_completions_url():
    """URL gọi chat: API_BASE (nếu có) hoặc URL mặc định theo MODEL_PROVIDER."""
    if API_BASE:
        if API_BASE.endswith("/chat/completions"):
            return API_BASE
        return API_BASE + "/chat/completions"
    if MODEL_PROVIDER in URLS:
        return URLS[MODEL_PROVIDER]
    raise NotImplementedError(
        "chưa có URL cho MODEL_PROVIDER=%s — đặt API_BASE=.../v1 hoặc thêm vào URLS trong ai.py"
        % MODEL_PROVIDER)


def call_openai_compatible(system, user):
    """Gọi API dạng OpenAI (Groq / FPT / OpenAI / DeepSeek…)."""
    if not API_KEY:
        raise RuntimeError("API_KEY trống — điền key vào .env")
    if not MODEL_NAME:
        raise RuntimeError("MODEL_NAME trống — điền mã model vào .env")
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(
        chat_completions_url(),
        {"Authorization": "Bearer " + API_KEY},
        {"model": MODEL_NAME, "messages": messages, "temperature": 0},
    )
    u = data.get("usage") or {}
    text = data["choices"][0]["message"]["content"]
    return {
        "text": text,
        "tokens_in": int(u.get("prompt_tokens") or u.get("input_tokens") or 0),
        "tokens_out": int(u.get("completion_tokens") or u.get("output_tokens") or 0),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}

    if MODEL_PROVIDER in URLS or API_BASE:
        r = call_openai_compatible(system, user)
        return {"text": r["text"], "model": MODEL_NAME,
                "tokens_in": int(r["tokens_in"]), "tokens_out": int(r["tokens_out"])}

    raise NotImplementedError(
        "chưa viết phần gọi model thật cho MODEL_PROVIDER=%s trong codebase/ai.py — xem docs/connect-model.md"
        % MODEL_PROVIDER)
