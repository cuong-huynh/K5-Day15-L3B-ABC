# Reflection — Vũ Lương Duy

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Mình làm bản chạy thử của lát cắt A2 (cặp X cùng Cường): `codebase/tools.py` (công cụ `search_announcements` chỉ đọc, `escalate` chỉ soạn bản nháp, không tự gửi), `codebase/agent.py` (workflow cố định: model phân loại ý định → code tìm thông báo → trả lời kèm link hoặc hỏi lại / chuyển TA), nhánh gọi Groq trong `codebase/ai.py`. Mình cũng chạy lượt 1 (`eval/run-1.csv`, 24 câu) và bộ kiểm tải phụ 50 câu trong `eval/stress/`. Commit chính trên nhánh `duy`: `8746155`, `7f3e187`, `007f2b1`, `5eefd12`.

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Mình dùng Claude Code để viết khung code, prompt phân loại và script kiểm tra; một LLM khác để sinh 50 câu kiểm tải (chi tiết ở `docs/ai-usage.md`). Chỗ phải sửa lại: lần đầu để model vừa phân loại vừa diễn đạt lại câu trả lời (2 lần gọi, ~520 token vào mỗi câu) nhưng câu của model thường bị bỏ vì không giữ đúng hạn/link, nên mình đổi sang dựng câu trả lời thẳng từ dữ liệu, chỉ còn một lần gọi (~290 token). Bản đầu cũng để tên model sai (`llama-3.3-70b-versatile` không có trong tài khoản), phải hỏi danh sách model rồi đổi sang `openai/gpt-oss-20b`.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   Trong bộ kiểm tải, "lab ba deadline khi nào thế mn" (S06) và "deadline LAB SIX?" (S14) bị hệ thống hỏi lại "lab nào?" dù học viên đã nói rõ. Nguyên nhân là code chỉ nhận mã lab dạng số, còn bước kiểm lại kết quả model cũng bắt mã lab phải xuất hiện nguyên văn trong câu hỏi. Mình học được rằng lớp kiểm tra "để an toàn" cũng có thể gây lỗi, và bộ câu thử tự viết dễ bỏ sót cách người thật gõ (viết chữ, viết tắt, không dấu). Mình đã sửa trong `tools.py` (nhận số bằng chữ tiếng Việt và tiếng Anh) và cũng học thêm rằng nên chạy lại cả bộ benchmark sau mỗi lần sửa để chắc không hồi quy (24/24 hành vi không đổi so với `run-1`).
