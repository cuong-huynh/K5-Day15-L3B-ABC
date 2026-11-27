"""Công cụ của bài toán A2 (Trợ lý Discord: hạn nộp / lịch từ thông báo chính thức).

Mỗi công cụ là một hàm có @tool; docstring ghi: tên · input · output · tác động ra ngoài.
Dữ liệu: data/announcements.json — DỮ LIỆU GIẢ (synthetic), xem data/DATA_CARD.md.
"""
import json
import os
import re

from tracing import tool, TOOLS  # noqa: F401

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "announcements.json")


def _load() -> list:
    with open(DATA_PATH, encoding="utf-8") as f:
        return json.load(f)


def extract_lab(text: str):
    """Hàm thuần (không phải công cụ): lấy mã lab từ câu hỏi, vd "hạn nộp lab 3" -> "3". Không thấy -> None."""
    m = re.search(r"\blab\s*[-#]?\s*(\d+|[a-z])\b", text.lower())
    return m.group(1) if m else None


@tool
def search_announcements(lab: str) -> list:
    """search_announcements — tra thông báo CHÍNH THỨC về hạn nộp của một lab.
    Input: lab (str, vd "3"). Output: danh sách thông báo {id, lab, date, deadline, url, title, text}
    chỉ gồm tin official, đúng lớp L3B và chưa bị thông báo khác thay thế (supersedes); mới nhất trước.
    Không tác động ra ngoài (chỉ đọc)."""
    items = [a for a in _load() if a["official"] and a["class"] == "L3B" and a["lab"] == str(lab).lower()]
    replaced = {a["supersedes"] for a in items if a.get("supersedes")}
    items = [a for a in items if a["id"] not in replaced]
    return sorted(items, key=lambda a: a["date"], reverse=True)


@tool
def escalate(question: str, reason: str) -> dict:
    """escalate — soạn BẢN NHÁP chuyển câu hỏi cho TA.
    Input: question (str, câu hỏi gốc), reason (str, vì sao không tự trả lời).
    Output: {"status": "draft_pending_review", "to": "TA", "message": str}.
    KHÔNG tự gửi tin Discord: chỉ tạo bản nháp, TA / người duyệt gửi."""
    return {"status": "draft_pending_review", "to": "TA",
            "message": "Học viên hỏi: \"%s\" — lý do chuyển: %s" % (question.strip()[:200], reason)}
