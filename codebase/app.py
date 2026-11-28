"""Giao diện bản chạy thử.

Mặc định: API HTTP cho FE Next.js (`frontend/`).
CLI: python codebase/app.py --cli   hoặc giữ eval qua agent.answer().

  python run.py                   → API http://127.0.0.1:8787
  cd frontend && npm run dev      → UI http://127.0.0.1:3000
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

for _stream in (sys.stdout, sys.stderr, sys.stdin):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

HOST = os.environ.get("APP_HOST", "127.0.0.1")
PORT = int(os.environ.get("APP_PORT", "8787"))


def _where(e):
    import traceback
    path = getattr(e, "filename", None) or (
        traceback.extract_tb(e.__traceback__)[-1].filename if e.__traceback__ else ""
    )
    if not path:
        return "codebase/"
    p = os.path.abspath(path)
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.relpath(p, base).replace(os.sep, "/") if p.startswith(base) else path


def _load_agent():
    try:
        import tracing
        from agent import answer
        return tracing, answer
    except Exception as e:
        print("Không nạp được codebase/ — lỗi ở %s: %s: %s" % (_where(e), type(e).__name__, e))
        print("Sửa lỗi rồi chạy lại. Cách nối model: docs/connect-model.md")
        raise


def run_cli() -> int:
    tracing, answer = _load_agent()
    print("Bản chạy thử CLI — gõ đầu vào rồi Enter. Thoát: Ctrl+C (hoặc Enter 2 lần với dòng trống).")
    blank = 0
    while True:
        try:
            text = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not text:
            blank += 1
            if blank >= 2:
                return 0
            continue
        blank = 0
        tracing.begin("app")
        try:
            result = answer(text)
        except NotImplementedError as e:
            tracing.end()
            print("Chưa nối model: %s" % e)
            return 1
        except Exception as e:
            tracing.end()
            print("[lỗi] %s: %s" % (type(e).__name__, e))
            continue
        s, _ = tracing.end()
        print(result.get("output", "") if isinstance(result, dict) else result)
        print("   (model: %s · gọi model %d lần · công cụ %d lần · token vào %d / ra %d)"
              % (", ".join(s["models"]) or "—", s["model_calls"], s["tool_calls"],
                 s["tokens_in"], s["tokens_out"]))


# Không gắn lên class (self.answer sẽ bị bind thêm self → TypeError).
_TRACING = None
_ANSWER = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("[api] " + (fmt % args) + "\n")

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, code, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self._cors()
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/health"):
            self._json(200, {"ok": True, "service": "abc-lab-deadline", "ask": "POST /api/ask"})
            return
        self._json(404, {"error": "not found"})

    def do_POST(self):
        path = urlparse(self.path).path
        if path != "/api/ask":
            self._json(404, {"error": "not found"})
            return
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b"{}"
        try:
            data = json.loads(raw.decode("utf-8"))
        except ValueError:
            self._json(400, {"error": "JSON không hợp lệ"})
            return
        text = (data.get("message") or data.get("text") or "").strip()
        if not text:
            self._json(400, {"error": "Thiếu message"})
            return

        _TRACING.begin("app")
        try:
            result = _ANSWER(text)
            s, _ = _TRACING.end()
            output = result.get("output", "") if isinstance(result, dict) else str(result)
            self._json(200, {
                "output": output,
                "model": ", ".join(s["models"]) or None,
                "model_calls": s["model_calls"],
                "tool_calls": s["tool_calls"],
                "tokens_in": s["tokens_in"],
                "tokens_out": s["tokens_out"],
            })
        except NotImplementedError as e:
            _TRACING.end()
            self._json(503, {"error": "Chưa nối model: %s" % e})
        except Exception as e:
            _TRACING.end()
            self._json(500, {"error": "%s: %s" % (type(e).__name__, e)})


def run_api() -> int:
    global _TRACING, _ANSWER
    _TRACING, _ANSWER = _load_agent()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print("API sẵn sàng: http://%s:%d" % (HOST, PORT))
    print("  POST /api/ask  {\"message\": \"hạn nộp lab 3 là khi nào?\"}")
    print("FE Next.js: cd frontend && npm run dev  → http://127.0.0.1:3000")
    print("CLI: python codebase/app.py --cli")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        return 0
    finally:
        server.server_close()
    return 0


def main() -> int:
    if "--cli" in sys.argv:
        return run_cli()
    return run_api()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        sys.exit(1)
