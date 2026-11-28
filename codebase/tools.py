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


NUMBER_WORDS = {"một": "1", "hai": "2", "ba": "3", "bốn": "4", "tư": "4", "năm": "5", "sáu": "6", "bảy": "7",
                "tám": "8", "chín": "9", "mười": "10", "one": "1", "two": "2", "three": "3", "four": "4",
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
_LAB_RE = re.compile(r"\blab\s*[-#]?\s*(\d+|%s|[a-z])\b" % "|".join(sorted(NUMBER_WORDS, key=len, reverse=True)))


def extract_labs(text: str) -> list:
    """Hàm thuần (không phải công cụ): mọi mã lab khác nhau trong câu hỏi, theo thứ tự xuất hiện.
    "lab 03" -> "3"; "lab ba" / "lab SIX" -> "3" / "6"."""
    labs = []
    for m in _LAB_RE.finditer(text.lower()):
        g = m.group(1)
        lab = NUMBER_WORDS.get(g) or (str(int(g)) if g.isdigit() else g)
        if lab not in labs:
            labs.append(lab)
    return labs


def extract_lab(text: str):
    """Hàm thuần: mã lab đầu tiên trong câu hỏi, vd "hạn nộp lab 3" -> "3". Không thấy -> None."""
    labs = extract_labs(text)
    return labs[0] if labs else None


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
