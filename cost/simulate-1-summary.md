# Tóm tắt mô phỏng simulate-1@20261128-132714

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 19 | 1 | 413 | 170 | 1.0 | 1.3 |
| dung_vua | 23 | 2 | 831 | 338 | 2.0 | 2.2 |
| dung_nhieu | 8 | 3 | 1241 | 624 | 3.0 | 3.4 |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-2@20261128-132500

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-2.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| deepseek-flash (vào 0.15 · ra 0.6 $/1M) | $0.00030 (≈ 8 ₫) | $0.00030 (≈ 8 ₫) | $0.00017 (≈ 4 ₫) | $0.2919 (≈ 7.297 ₫) | $0.6810 (≈ 17.026 ₫) | $0.9729 (≈ 24.323 ₫) | $0.00097 (≈ 24 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00066 (≈ 17 ₫) | $0.00066 (≈ 17 ₫) | $0.00037 (≈ 9 ₫) | $0.6427 (≈ 16.067 ₫) | $1.50 (≈ 37.489 ₫) | $2.14 (≈ 53.556 ₫) | $0.0021 (≈ 54 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: DeepSeek-V4.1-Flash. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 25.000 ₫ ((tự ước tính) quy đổi minh họa ~25.000 VND/USD).
