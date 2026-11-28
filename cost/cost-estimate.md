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
  - `openai/gpt-oss-20b` (Groq): vào `$0.075` · ra `$0.30` — nguồn `https://groq.com/pricing` · xem 28/11/2026 (model chạy thật ở `eval/run-1.csv`).
  - `openai/gpt-oss-120b` (Groq): vào `$0.15` · ra `$0.60` — nguồn `https://groq.com/pricing` · xem 28/11/2026.
  - `gemini-3.5-flash` (Google): vào `$1.50` · ra `$9.00` — nguồn `https://ai.google.dev/gemini-api/docs/pricing` · xem 28/11/2026 (model đo token mô phỏng).
  - Tỷ giá quy đổi: `1 USD = 26.030 ₫` (Vietcombank tỷ giá bán ra · xem 28/11/2026).
- **Tỉ lệ đạt** dùng để tính: `24/24 (100%)` — lượt **`eval/run-2.csv`** (`run-2@20261128-135201`, `openai/gpt-oss-20b` · Groq). CP4 lấy **lượt 2** theo rubric R6. Kèm bảng độ nhạy 90% và 80% ở mục 4.
- Đo token trên model `gemini-3.5-flash` (lượt `simulate-1`), tính giá cho `openai/gpt-oss-20b`, `openai/gpt-oss-120b` và `gemini-3.5-flash`. *(Lưu ý trung thực: eval lượt 2 cùng họ model giá `openai/gpt-oss-20b`; mô phỏng đo token trên Gemini vì 429/DNS — chỉ 8/50 phiên OK tính trung bình. Khác bộ tách token nên số token thật trên Groq có thể lệch nhẹ. Muốn đo token đúng model run-2 sẽ lưu `cost/simulate-2.csv`.)*

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` (`cost/simulate-1-summary.md`, `traces/simulate-1.jsonl`) · run ID `simulate-1@20261128-132804` · `50` phiên · seed `42`

| Persona | Số phiên mô phỏng thành công | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| `dung_it` | 4 | 1 | 278 | 16 | 1.0 | 1.2 |
| `dung_vua` | 4 | 2 | 557 | 35 | 2.0 | 2.0 |
| `dung_nhieu` | 0 | 3 | — | — | — | — |

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng — thấp (300) | / tháng — cơ sở (700) | / tháng — cao (1.000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `openai/gpt-oss-20b` (vào 0.075 · ra 0.3 $/1M) | $0.000039 (≈ 1 ₫) | $0.000039 (≈ 1 ₫) | $0.000026 (≈ 1 ₫) | $0.0342 (≈ 891 ₫) | $0.0799 (≈ 2.080 ₫) | $0.1142 (≈ 2.972 ₫) | $0.00011 (≈ 3 ₫) |
| `openai/gpt-oss-120b` (vào 0.15 · ra 0.6 $/1M) | $0.000078 (≈ 2 ₫) | $0.000078 (≈ 2 ₫) | $0.000052 (≈ 1 ₫) | $0.0685 (≈ 1.783 ₫) | $0.1598 (≈ 4.160 ₫) | $0.2283 (≈ 5.943 ₫) | $0.00023 (≈ 6 ₫) |
| `gemini-3.5-flash` (vào 1.5 · ra 9.0 $/1M) | $0.00085 (≈ 22 ₫) | $0.00085 (≈ 22 ₫) | $0.00057 (≈ 15 ₫) | $0.7520 (≈ 19.574 ₫) | $1.75 (≈ 45.674 ₫) | $2.51 (≈ 65.248 ₫) | $0.0025 (≈ 65 ₫) |

- **Ghi chú trung thực về lượt `simulate-1`:** có `42/50` phiên lỗi (rớt DNS/mạng tạm thời ở `S003`–`S012` và chạm hạn mức miễn phí `HTTP 429` của Google AI Studio từ `S014`/`S022`), nên chỉ có `8/50` phiên không lỗi được tính vào trung bình (`dung_it`: 4, `dung_vua`: 4; `dung_nhieu`: 0 nên khung tự lấy chi phí trung bình chung cho persona này). Nếu chạy lại bằng tài khoản trả phí hoặc key Groq (trùng model `eval/run-2.csv`), nhóm sẽ lưu thành `cost/simulate-2.csv` (không ghi đè `simulate-1`).
- Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%** (xem bảng độ nhạy 90% / 80% ở mục 4).

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ **45 phút/tháng/học viên** (~3 lần/tháng × 15 phút tìm & đối chiếu hạn, đồng thời tránh rủi ro nộp muộn mất điểm lab — nguồn P1–P3).
- Chi phí / người / tháng (cơ sở 700 học viên):
  - Với `openai/gpt-oss-20b`: **$0.00011 (≈ 3 ₫/người/tháng)** — tổng cả lớp 700 người ≈ **$0.0799 (≈ 2.080 ₫/tháng)**.
  - Với `gemini-3.5-flash` (mức đắt nhất trong 3 model): **$0.0025 (≈ 65 ₫/người/tháng)** — tổng cả lớp 700 người ≈ **$1.75 (≈ 45.674 ₫/tháng)**.
- **Kết luận một dòng — đáng làm không:** **Rất đáng làm** — chi phí model chỉ khoảng **3 ₫ đến 65 ₫ / học viên / tháng** (dưới 50.000 ₫/tháng cho cả lớp 700 người ngay cả ở model mạnh), quá nhỏ so với ~45 phút tiết kiệm/người/tháng và rủi ro nộp muộn mất điểm lab; chi phí thực tế cần để ý không phải token mà là công TA duyệt ca `escalate` và vận hành bot.

## 4. Độ nhạy & chi phí ngoài model

- **Độ nhạy theo tỉ lệ đạt** *(vì `eval/run-2.csv` đạt 100%, kiểm tra khi tỉ lệ đạt thực tế giảm xuống 90% và 80%)*:

| Kịch bản tỉ lệ đạt | Chi phí / task thành công (`openai/gpt-oss-20b`) | Chi phí / task thành công (`openai/gpt-oss-120b`) | Chi phí / task thành công (`gemini-3.5-flash`) | Ghi chú |
|---|---:|---:|---:|---|
| Thực đo `run-2` (100%) | $0.000039 (≈ 1 ₫) | $0.000078 (≈ 2 ₫) | $0.00085 (≈ 22 ₫) | % từ run-2; token/phiên từ `cost/simulate-1-summary.md` |
| Giả định 90% *(độ nhạy)* | $0.000043 (≈ 1 ₫) | $0.000086 (≈ 2 ₫) | $0.00095 (≈ 25 ₫) | `chi_phi_phien ÷ 0.90` — dự phòng câu ngoài phân bố |
| Giả định 80% *(độ nhạy)* | $0.000049 (≈ 1 ₫) | $0.000097 (≈ 3 ₫) | $0.0011 (≈ 28 ₫) | `chi_phi_phien ÷ 0.80` — kịch bản bảo thủ sát chuẩn đạt (≥70%) |

- **Chi phí ngoài model:** chưa tính vào bảng trên — khi đưa vào dùng thật cần cộng thêm hosting bot Discord / API nhỏ (~5–10 USD/tháng) và thời gian TA duyệt các ca `escalate` (bản nháp chờ duyệt).
- **Cần gạt tối ưu đã áp dụng / có thể thêm:** workflow đã cắt từ 2 lần gọi xuống 1 lần gọi model (~280–300 token vào/câu) vì dựng câu trả lời trực tiếp từ JSON thông báo; nếu dùng thật có thể thêm cache theo mã lab để giảm tiếp số lần gọi model.
