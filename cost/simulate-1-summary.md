# Tóm tắt mô phỏng simulate-1@20261128-132804

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 4 | 1 | 278 | 16 | 1.0 | 1.2 |
| dung_vua | 4 | 2 | 557 | 35 | 2.0 | 2.0 |
| dung_nhieu | 0 | 3 | — | — | — | — |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-2@20261128-135201 (cập nhật CP4: dùng % lượt 2; token vẫn từ simulate-1)

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv. ⚠️ Mô phỏng đo token trên gemini-3.5-flash; eval lượt 2 model khác — ghi rõ trong cost/cost-estimate.md.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| openai/gpt-oss-20b (vào 0.075 · ra 0.3 $/1M) | $0.000039 (≈ 1 ₫) | $0.000039 (≈ 1 ₫) | $0.000026 (≈ 1 ₫) | $0.0342 (≈ 891 ₫) | $0.0799 (≈ 2.080 ₫) | $0.1142 (≈ 2.972 ₫) | $0.00011 (≈ 3 ₫) |
| openai/gpt-oss-120b (vào 0.15 · ra 0.6 $/1M) | $0.000078 (≈ 2 ₫) | $0.000078 (≈ 2 ₫) | $0.000052 (≈ 1 ₫) | $0.0685 (≈ 1.783 ₫) | $0.1598 (≈ 4.160 ₫) | $0.2283 (≈ 5.943 ₫) | $0.00023 (≈ 6 ₫) |
| gemini-3.5-flash (vào 1.5 · ra 9.0 $/1M) | $0.00085 (≈ 22 ₫) | $0.00085 (≈ 22 ₫) | $0.00057 (≈ 15 ₫) | $0.7520 (≈ 19.574 ₫) | $1.75 (≈ 45.674 ₫) | $2.51 (≈ 65.248 ₫) | $0.0025 (≈ 65 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.5) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 42/50.
- Tỷ giá: 1 USD = 26.030 ₫ (Vietcombank tỷ giá bán ra USD/VND · xem 28/11/2026).
