# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261128-064545 | 24/24 | 100% | 4/4 | 14/14 | 6/6 | đạt |
| 2 | run-2@20261128-132500 | 24/24 | 100% | 4/4 | 14/14 | 6/6 | đạt |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| *(lượt 1 không có câu `pass=0`)* | 0 | — |
| Soft-fail: lý do escalate quá chung | 7 | B15–B21 |

**≥3 lỗi cụ thể (soft — vẫn `pass=1` nhưng kém trải nghiệm TA):**

| Câu | Input (rút) | Output (vấn đề) | Vì sao sai / kém |
|---|---|---|---|
| B15 | Cách tính hạn Gate 1… | Chuyển TA với lý do “điểm / điểm danh / việc khác” | Nhầm loại việc; TA không biết là quy định Gate |
| B16 | nộp trên lms là nộp ở đâu | Cùng lý do chung | Không nêu LMS |
| B20 | nộp Gate 2 Phoenix thất bại | Cùng lý do chung | Không nêu lỗi hệ thống Phoenix |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: **lý do chuyển TA quá chung (B15–B21)** — vì sao đau với người dùng: học viên/TA đọc bản nháp không biết việc cần xử lý gì; dễ hiểu nhầm bot “lười” hoặc lẫn điểm số.
- Đã sửa gì: thêm `out_of_scope_reason()` trong `codebase/agent.py` — phân loại lý do Gate / LMS / Phoenix / nộp nhầm / lỗi refresh / điểm / điểm danh trước khi `escalate`.
- Kết quả: soft-fail B15–B21 có lý do cụ thể trong output · tổng **24/24 → 24/24** (100% → 100%) · vẫn đạt chuẩn §7.
- Câu nào **tệ đi** sau khi sửa: không có (cùng bộ câu thử, không câu `pass=0` mới).

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm: model `classify` vẫn có thể gắn `ngoai_pham_vi` rộng; lý do code đã bù. Nguy hiểm chính vẫn là bịa hạn — đã chặn bằng dựng hạn từ data.
- Nếu có thêm 1 tuần: held-out set · làm rõ hơn handoff Discord thật (sau duyệt) · đo A/B lý do escalate với TA.
