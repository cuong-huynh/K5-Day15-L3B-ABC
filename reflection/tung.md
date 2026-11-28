# Reflection — Cao Thanh Tùng

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Cặp Y (cùng Đức) + phần eval: mở rộng / rà `eval/benchmark.csv` (24 câu), `eval/metric_spec.yaml`, `data/DATA_CARD.md`, hỗ trợ chấm lượt và chạy `python run.py simulate`. CP4: người thứ hai chấm độc lập 5 output (B01, B05, B06, B09, B15) khớp 5/5 theo `pass_criterion` (ghi `eval/README.md`), trình bày slide đánh giá + chi phí khi demo.

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Dùng AI để gợi ý lưới độ phủ câu thử và so khớp `pass_criterion` với output; chỗ phải sửa lại là không để AI tự “chấm giúp” cả bộ — vẫn đọc từng output và ghi tay pass/ghi chú. Khi simulate báo 429, không xoá file lỗi mà giữ `simulate-1` và ghi rõ 8/50 phiên OK trong `cost-estimate.md`.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   Soft-fail kiểu B15 (Gate) từng bị gom vào “điểm/điểm danh” dù `pass=1`. Mình học được metric pass/fail cần `pass_criterion` đủ cụ thể, và chấm người thứ hai giúp bắt chỗ tiêu chí mơ hồ trước khi khóa chuẩn §7; sau cải tiến lý do escalate, cùng 5 câu chấm lại vẫn khớp 5/5.
