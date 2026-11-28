# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code (Claude Sonnet 5.5) | Viết `codebase/tools.py` (`search_announcements`, `escalate`), `agent.py` (workflow cố định), nhánh gọi Groq trong `ai.py`, script `eval/stress/run_stress.py` | Duy chạy `python run.py`, `eval --try`, `eval` (lượt 1); đọc output từng ca; sửa lỗi sau khi chạy bộ 50 câu (mã lab viết chữ, nhiều lab trong một câu, xin gia hạn, lỗi LMS); bỏ lần gọi model thứ hai để giảm token (~520 → ~290 token vào mỗi câu) | Duy |
| Prompt / thiết kế lời gọi mô hình | Claude Code (Claude Sonnet 5.5) · model chạy thật: `openai/gpt-oss-20b` (Groq) | Soạn prompt phân loại ý định (`CLASSIFY_SYSTEM` trong `agent.py`); đề xuất code kiểm lại đầu ra model (mã lab phải có trong câu hỏi, hạn + link lấy thẳng từ dữ liệu, regex chặn lệnh chèn làm lớp dự phòng) | Duy quyết định giữ một lần gọi model; kiểm bằng 24 câu benchmark (không đổi hành vi so với `run-1`) và 50 câu stress | Duy |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | Antigravity (coding agent) | Chỉ rà câu dẫn dắt và đối chiếu độ đầy đủ giữa `P1.md`–`P3.md` với `evidence/summary.md` | Đức tự phỏng vấn trực tiếp người thật ngoài nhóm (P1), kiểm lại toàn bộ trích dẫn và số liệu — không dùng AI tạo câu trả lời | Đức |
| Mô phỏng chi phí (`cost/personas.yaml`, khung `cost/cost-estimate.md`) | Antigravity (coding agent) | Gợi ý cấu trúc 3 persona khớp P1–P3, tra cứu giá API công khai (Groq/Gemini) và rà cảnh báo của `cost/simulate.py` | Đức kiểm tra khớp nguồn P1–P3, gắn nhãn `(tự ước tính)` cho tham số chưa đo (`share`, `turns_per_session`, `low`/`high`), không điền tay số mô phỏng | Đức |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Bộ câu kiểm tải phụ `eval/stress/cases_50.json` (không thuộc `benchmark.csv`) | LLM khác (do Duy chạy prompt `eval/stress/gen_prompt.md`) | Sinh 50 câu thử + nhãn hành vi mong đợi | Nhãn do LLM sinh, chưa kiểm tay toàn bộ: đã xem tay các câu lệch (S36, S38 là nhãn chưa chuẩn / lỗi phát hiện, không phải lỗi bịa hạn) | Duy |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
