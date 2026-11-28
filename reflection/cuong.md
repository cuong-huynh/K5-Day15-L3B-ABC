# Reflection — Huỳnh Văn Cường

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
   Đội trưởng nhóm ABC (mã `2A202603866`): điều phối cặp X/Y, giữ `spec.md` / `canvas.md` / changelog §10, nộp form CP1–CP4, merge/`main`, máy demo (`.env` không commit). CP4: phối hợp chấm `eval/run-2.csv`, cập nhật `eval/report.md` · `eval/README.md`, xuất `demo-slides.pdf` ở gốc repo, soạn `CP4-form-draft.md`, trình bày slide chi phí/kết luận khi demo.

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
   Dùng coding agent (Cursor) để soạn dàn slide HTML/PDF, text form, và rà checklist rubric. Chỗ phải sửa lại: bản slide đầu quá dày chữ (giống báo cáo) nên rút còn tiêu đề + số/trích; lần commit agent từng gắn sai author → đã rewrite về `cuong-huynh`; số cost trên `spec` §8 lệch bản `cost-estimate` của cặp Y nên phải khớp lại với `simulate-1` thật.

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
   Không có câu `pass=0`, nhưng soft-fail B15–B21 (lý do escalate chung) cho thấy “đạt metric” chưa đủ cho TA. Mình học được phải đọc output như người nhận handoff, không chỉ cột pass; cải tiến `out_of_scope_reason()` rồi chạy lại cùng bộ câu mới đủ kể câu chuyện lượt 1 → lượt 2 ở demo.
