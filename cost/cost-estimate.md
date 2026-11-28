# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): dung_it 40% · dung_vua 40% · dung_nhieu 20% — số lần/tháng từ P1–P3 (`evidence/interviews/`).
- **Số người dùng thật** 3 kịch bản: thấp **300** · cơ sở **700** · cao **1000**. Nguồn: track A — lớp L3 >700 (README hackathon); thấp/cao *(tự ước tính)*.
- **Giá** ≥2 mức: `deepseek-flash` 0.15/0.60 $/1M · `gemini-3.1-flash-lite` 0.25/1.50 $/1M (brief `model-prices.md` 25/11/2026).
- **Tỉ lệ đạt** dùng để tính: **24/24 (100%)** — lượt `run-2@20261128-132500`. Guide khuyên không “coi như 100%” mù quáng → thêm **độ nhạy** 90% / 80% ở mục 2b.
- Đo token trên model **DeepSeek-V4.1-Flash** (FPT); tính giá theo `deepseek-flash` và `gemini-3.1-flash-lite`.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-132714` · **50** phiên · seed **42**  
Tóm tắt: `cost/simulate-1-summary.md`

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (300) | / tháng — cơ sở (700) | / tháng — cao (1000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| deepseek-flash | $0.00030 | $0.00030 | $0.29 | $0.68 | $0.97 | $0.00097 (~24₫) |
| gemini-3.1-flash-lite | $0.00066 | $0.00066 | $0.64 | $1.50 | $2.14 | $0.0021 (~54₫) |

**Kịch bản cơ sở (nộp form):** chi phí / task thành công ≈ **$0.00030** trên giá `deepseek-flash` (đo token DeepSeek-V4.1-Flash).

### 2b. Độ nhạy tỉ lệ đạt (vì lượt 2 = 100%)

Chi phí / task = chi phí/phiên ÷ tỉ lệ. Với deepseek-flash ($0.00030/phiên):

| Tỉ lệ giả định | Chi phí / task thành công |
|---|---:|
| 100% (đo run-2) | $0.00030 |
| 90% | $0.00033 |
| 80% | $0.00038 |

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): ≈ **45 phút** tìm/hỏi lại hạn (1×3 lần×15 phút từ P1–P3).
- Chi phí model / người / tháng (cơ sở): ~**24–54₫** — rất nhỏ so với thời gian tiết kiệm.
- **Kết luận:** **đáng làm (go / iterate)** ở quy mô lớp — chi phí API không phải nút thắt; nút thắt là chất lượng căn cứ thông báo + handoff TA.
