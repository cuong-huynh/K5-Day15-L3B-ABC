# Reflection — Nguyễn Phan Tuấn Đức

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Mình phụ trách mảng bằng chứng người dùng (CP2–CP3) và mô phỏng chi phí (CP4) trong cặp Y cùng Tùng: viết và chuẩn hóa phỏng vấn học viên L3B ngoài nhóm (`evidence/interviews/P1.md`–`P3.md`, trực tiếp hỏi và ghi `P1.md`), tổng hợp bằng chứng đạt ngưỡng ≥3 người và 6 trích dẫn nguyên văn trong `evidence/summary.md`, rà khớp số liệu lên `spec.md` §1–§2. Ở CP4, mình thiết lập `cost/personas.yaml` (3 persona từ P1–P3, 3 kịch bản quy mô lớp L3 và 3 mức giá model), chạy mô phỏng 50 phiên (`cost/simulate-1.csv`, `cost/simulate-1-summary.md`), hoàn thiện `cost/cost-estimate.md` (kèm độ nhạy 90%/80%), và phụ trách trình bày phần Pain & Impact (slide 1–2).

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Mình dùng coding agent (Antigravity) để rà cấu trúc câu hỏi phỏng vấn tránh dẫn dắt, kiểm tra tính nhất quán giữa `evidence/summary.md` với `cost/personas.yaml`, và tra/đối chiếu biểu giá API chính thức cho các mức model (chi tiết ở `docs/ai-usage.md`). Chỗ phải sửa lại: cấu hình mẫu ban đầu vẫn còn chú thích chứa chuỗi `(ví dụ)` khiến script `simulate.py` cảnh báo, đồng thời tỷ lệ phân bổ `share` và `turns_per_session` là giả định chưa đo trực tiếp nên mình phải ghi rõ `(tự ước tính)` theo đúng luật minh bạch dữ liệu, không gán nguồn phỏng vấn cho những số chưa hỏi.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   Dù lượt 1 đạt 24/24 trên `eval/benchmark.csv`, nhóm vẫn phát hiện nhóm soft-fail ở các câu `B15`–`B21` (hỏi về Gate, LMS, nộp nhầm file, lỗi hệ thống Phoenix): bot chuyển TA đúng nhưng dùng chung một lý do “ngoài phạm vi điểm/điểm danh…”, dễ làm học viên và TA khó hiểu đúng vấn đề cần xử lý. Ngoài ra, khi xem bộ stress test 50 câu của Duy, các câu viết số bằng chữ như “lab ba” (`S06`) hay “LAB SIX” (`S14`) từng bị hỏi lại “lab nào?”. Mình học được rằng “đạt 100% pass/fail” chưa đủ nếu trải nghiệm handoff còn chung chung, và dữ liệu từ cách hỏi thật của người dùng luôn quan trọng hơn bộ câu tự nghĩ ra.
