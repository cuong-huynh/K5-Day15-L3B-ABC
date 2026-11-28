"""Generate demo-slides.pdf (8 pages) at repo root."""
from __future__ import annotations

import os
from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
FONT = Path(r"C:\Windows\Fonts\arial.ttf")
OUT = ROOT / "demo-slides.pdf"


def main() -> None:
    if not FONT.is_file():
        raise SystemExit(f"Missing font: {FONT}")

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("ArialUni", "", str(FONT))

    pages: list[tuple[str, list[str]]] = [
        (
            "1. Người dùng & pain",
            [
                "Học viên L3B đang tìm hạn nộp lab trên Discord.",
                "Pain: thông báo rải / bản cũ / hỏi lại — P1–P3.",
                'Trích: "Mình search ra tin cũ trước, suýt nộp theo ngày đó luôn." (P1)',
                "Nguồn: evidence/summary.md — 3/3 gap pain, ~2–4 lần/tháng, 10–30 phút/lần.",
            ],
        ),
        (
            "2. Vì sao chọn bài này",
            [
                "Hướng chọn: A2 hỏi hạn lab từ thông báo Discord (hẹp).",
                "Impact ~ 1 × 3 lần × 15 phút = ~45 phút/tháng/học viên (P1–P3).",
                "Loại: A1 tutor (pain khác); bot ôm hết logistics (không kịp).",
                "Nguồn: spec.md §2.",
            ],
        ),
        (
            "3. Giải pháp",
            [
                "Lát cắt: 1 HV L3B · hỏi hạn lab X · chỉ trả lời khi đúng 1 căn cứ official + link, không thì chuyển TA.",
                "Hình dạng: workflow cố định (parse → search → quyết định).",
                "AI tự làm khi chắc; chuyển người khi mâu thuẫn / thiếu / ngoài phạm vi.",
                "Nguồn: spec.md §4.",
            ],
        ),
        (
            "4. Demo live",
            [
                "Thường: hạn nộp lab 3 → AN-04 29/11 + link.",
                "Khó: lab 4 mâu thuẫn AN-05/AN-06 → chuyển TA; hoặc câu Gate/LMS → lý do escalate cụ thể.",
                "Video dự phòng: điền link Drive/YouTube khi quay xong.",
            ],
        ),
        (
            "5. Đánh giá thế nào",
            [
                "Bộ 24 câu (thường 4 · khó 14 · từ_chối 6). Chuẩn đạt: ≥70% + 100% tu_choi.",
                "Lượt 1: 24/24 — run-1@20261128-064545 (Groq gpt-oss-20b).",
                "Cải tiến: out_of_scope_reason() cho B15–B21.",
                "Lượt 2: 24/24 — run-2@20261128-132500 (FPT DeepSeek-V4.1-Flash).",
                "Nguồn: eval/report.md, eval/README.md.",
            ],
        ),
        (
            "6. Chi phí khi dùng thật",
            [
                "Đo token: DeepSeek-V4.1-Flash · 50 phiên (simulate-1).",
                "Chi phí / task thành công (cơ sở): ~$0.00030 (deepseek-flash).",
                "/ người / tháng (cơ sở 700 HV): ~$0.001 (~24 VND).",
                "Độ nhạy nếu đạt 90%/80%: task ~$0.00033 / $0.00038.",
                "Nguồn: cost/cost-estimate.md.",
            ],
        ),
        (
            "7. Kết luận",
            [
                "Go / iterate: pain có bằng chứng; eval đạt chuẩn 2 lượt; chi phí API rất thấp vs 45 phút/tháng.",
                "Iterate: lý do handoff TA, dữ liệu thông báo thật, Discord gửi thật sau duyệt.",
            ],
        ),
        (
            "8. Nếu thêm 1 tuần",
            [
                "1) Held-out ~20% câu thử.",
                "2) Nối Discord thật (gửi tin sau TA duyệt).",
                "3) Đo A/B lý do escalate với TA + validation 2–3 HV.",
            ],
        ),
    ]

    for title, lines in pages:
        pdf.add_page()
        pdf.set_font("ArialUni", size=18)
        pdf.multi_cell(0, 10, title)
        pdf.ln(4)
        pdf.set_font("ArialUni", size=12)
        for line in lines:
            pdf.multi_cell(0, 7, line)
            pdf.ln(1)

    pdf.output(str(OUT))
    print(f"wrote {OUT} pages={len(pdf.pages)}")


if __name__ == "__main__":
    os.chdir(ROOT)
    main()
