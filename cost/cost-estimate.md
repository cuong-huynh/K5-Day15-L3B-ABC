# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu dựa trên phỏng vấn P1–P3 (`evidence/summary.md`, `spec.md` §2):
  - `dung_it`: tỉ lệ `40%` *(tự ước tính)* · `2` phiên/người/tháng (P3) · `1` lượt hỏi/phiên *(tự ước tính)* · loại câu `[thuong, kho]`.
  - `dung_vua`: tỉ lệ `40%` *(tự ước tính)* · `3` phiên/người/tháng (P1) · `2` lượt hỏi/phiên *(tự ước tính)* · loại câu `[thuong, kho]`.
  - `dung_nhieu`: tỉ lệ `20%` *(tự ước tính)* · `4` phiên/người/tháng (cận trên P2: 2–4 lần/tháng) · `3` lượt hỏi/phiên *(tự ước tính)* · loại câu `[thuong, kho, tu_choi]`.
  - Trung bình trọng số: `2,8` phiên/người/tháng (khớp ước lượng ~3 lần/tháng ở `spec.md` §2).
- **Số người dùng thật** 3 kịch bản: thấp `300` *(tự ước tính)* · cơ sở `700` (README hackathon AI20K: lớp L3 > 700 học viên) · cao `1.000` *(tự ước tính)*.
- **Giá** 3 mức model (USD / 1M token):
  - `openai/gpt-oss-20b` (Groq): vào `$0.075` · ra `$0.30` — nguồn `https://groq.com/pricing` · xem 28/11/2026 (model chạy thật).
  - `openai/gpt-oss-120b` (Groq): vào `$0.15` · ra `$0.60` — nguồn `https://groq.com/pricing` · xem 28/11/2026.
  - `gemini-4-hydrogen` (Google): vào `$1.50` · ra `$7.50` — nguồn `https://ai.google.dev/gemini-api/docs/pricing` · theo bảng giá repo đề 25/11/2026.
  - Tỷ giá quy đổi: `1 USD = 26.030 ₫` (Vietcombank tỷ giá bán ra · xem 28/11/2026).
- **Tỉ lệ đạt** dùng để tính: *(chờ chạy & chấm lượt 2 `eval/run-2.csv`; lượt 1 hiện là `24/24 = 100%` — `run-1@20261128-064545`)*
- Đo token trên model `openai/gpt-oss-20b` (Groq), tính giá cho `openai/gpt-oss-20b`, `openai/gpt-oss-120b` và `gemini-4-hydrogen` *(lưu ý: khác bộ tách token giữa các hãng nên số token thực tế trên Gemini có thể lệch)*.

## 2. Kết quả mô phỏng

> **Chờ chạy lệnh thật (cần `.env` có API key Groq):**
> `python3 run.py simulate --try` → `python3 run.py simulate --rate-from eval/run-2.csv` (hoặc `eval/run-1.csv` nếu chưa có lượt 2), rồi dán nguyên bảng từ `cost/simulate-1-summary.md` vào dưới đây.

Lượt mô phỏng: `cost/simulate-__.csv` · run ID `__` · `50` phiên · seed `42`

*(dán bảng từ `cost/simulate-1-summary.md` sau khi chạy)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (300) | / tháng — cơ sở (700) | / tháng — cao (1.000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `openai/gpt-oss-20b` | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* |
| `openai/gpt-oss-120b` | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* |
| `gemini-4-hydrogen` | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%** (xem bảng độ nhạy 90% / 80% ở mục 4 nếu lượt 2 đạt 100%).

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ **45 phút/tháng/học viên** (~3 lần/tháng × 15 phút tìm & đối chiếu hạn, tránh rủi ro nộp muộn mất điểm lab — nguồn P1–P3).
- Chi phí / người / tháng (cơ sở, model `openai/gpt-oss-20b`): *(điền sau khi có `cost/simulate-1-summary.md`)*
- **Kết luận một dòng — đáng làm không:** *(chốt sau khi có số từ `simulate-1-summary.md` — so trực tiếp chi phí/người/tháng với 45 phút tiết kiệm + giảm rủi ro sai hạn)*

## 4. Độ nhạy & chi phí ngoài model

- **Độ nhạy theo tỉ lệ đạt (nếu lượt 2 đạt 100% trên tập benchmark 24 câu):**

| Kịch bản tỉ lệ đạt | Chi phí / task thành công (`openai/gpt-oss-20b`) | Chi phí / task thành công (`openai/gpt-oss-120b`) | Chi phí / task thành công (`gemini-4-hydrogen`) | Ghi chú |
|---|---:|---:|---:|---|
| Thực đo (`run-2`, vd 100%) | *(chờ simulate)* | *(chờ simulate)* | *(chờ simulate)* | Lấy trực tiếp từ `simulate-1-summary.md` |
| Giả định 90% *(độ nhạy)* | `chi_phi_phien ÷ 0.90` | `chi_phi_phien ÷ 0.90` | `chi_phi_phien ÷ 0.90` | Dự phòng câu ngoài phân bố thực tế |
| Giả định 80% *(độ nhạy)* | `chi_phi_phien ÷ 0.80` | `chi_phi_phien ÷ 0.80` | `chi_phi_phien ÷ 0.80` | Kịch bản bảo thủ sát ngưỡng chuẩn đạt (≥70%) |

- **Chi phí ngoài model:** chưa tính vào bảng trên — khi đưa vào dùng thật cần cộng thêm hosting bot Discord / API nhỏ và thời gian TA duyệt các ca `escalate` (bản nháp chờ duyệt).
- **Cần gạt tối ưu đã áp dụng / có thể thêm:** workflow hiện đã cắt từ 2 lần gọi xuống 1 lần gọi model (~290 token vào/câu ở `run-1`) vì dựng câu trả lời trực tiếp từ JSON thông báo; nếu dùng thật có thể thêm cache theo mã lab để giảm tiếp số lần gọi model.
