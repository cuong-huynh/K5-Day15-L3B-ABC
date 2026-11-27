# CP2 — Chia việc nhóm ABC · Track A2 (Trợ lý Discord)

> Mốc: **19:30 Thứ Sáu 27/11** · Đội trưởng nộp: **Huỳnh Văn Cường · 2A202603866**  
> Repo: https://github.com/cuong-huynh/K5-Day15-L3B-ABC  
> Đọc xong → làm đúng phần của mình → 19:00 họp chung.

## Lát cắt đang làm

Một học viên L3B · hỏi "hạn nộp lab X là khi nào" · hệ thống chỉ trả lời khi tìm được trong thông báo chính thức kèm link, không có thì chuyển TA · học viên không nhận hạn sai.

---

## Timeline

| Giờ | Việc | Ai |
|---|---|---|
| 17:00–17:25 | Mỗi người hỏi ≥1 bạn ngoài nhóm (lần gần nhất không chắc hạn/lịch trên Discord). 20 phút tổng hợp | Cả nhóm → **Đức** ghi file |
| 17:25–17:40 | Chốt thiết kế: workflow, AI tự đến đâu, sai thì sao | Cả nhóm → **Cường** ghi `spec.md` |
| 17:40–19:00 | Chia 2 cặp (bảng dưới) | 2 cặp |
| 19:00–19:15 | Đổi chéo review + `python run.py` + `python run.py check` | Cả nhóm |
| 19:15–19:30 | Cập nhật `canvas.md` · nộp form CP2 | **Cường** |

---

## Cặp X — Duy + Cường · bản chạy thử + spec

| Ai | Việc | File / output |
|---|---|---|
| **Vũ Lương Duy** | Khung bản chạy thử A2 (AI giả): tìm thông báo → trả lời kèm nguồn / hỏi lại / chuyển TA | `codebase/tools.py` · `codebase/agent.py` · `python run.py` chạy hết luồng |
| **Huỳnh Văn Cường** | Spec + sơ đồ + chuẩn đạt + canvas CP2 + nộp form | `spec.md` §3–§7 (có sơ đồ §4) · `canvas.md` · form CP2 |

## Cặp Y — Đức + Tùng · bằng chứng + bộ câu thử

| Ai | Việc | File / output |
|---|---|---|
| **Nguyễn Phan Tuấn Đức** | Phỏng vấn / ghi chép bằng chứng pain | `evidence/interviews/P1.md`… · cập nhật dòng 4 `canvas.md` (số đầu + 1 trích dẫn nếu có) |
| **Cao Thanh Tùng** | Bộ câu thử + metric + data card | `eval/benchmark.csv` ≥10 câu · `eval/metric_spec.yaml` ≥3 metric · `data/DATA_CARD.md` |

**Đổi chéo 19:00:** X đọc bộ câu thử của Y · Y chạy thử `python run.py` của X.

---

## Checklist nộp CP2 (đủ mới nộp)

- [ ] `canvas.md` cập nhật + dòng “Đã đổi gì so với CP1”
- [ ] Nguồn bằng chứng đang làm + đã đến đâu
- [ ] Link `spec.md` — §4 có sơ đồ kiến trúc
- [ ] Link `eval/benchmark.csv` ≥10 câu; đã có `eval/metric_spec.yaml` và `data/DATA_CARD.md`
- [ ] **Chuẩn “đạt”** chép từ `spec.md` §7 — **chốt tại CP2, không sửa sau**
- [ ] `python run.py` đi hết luồng với AI giả
- [ ] `python run.py check` — xem cảnh báo còn gì

## Gợi ý câu hỏi phỏng vấn (Đức + cả nhóm)

- Lần gần nhất bạn cần biết hạn nộp / lịch lab, bạn tìm ở đâu?
- Mất bao lâu? Có hỏi lại ai không?
- Đã bao giờ đọc nhầm thông báo cũ chưa? Chuyện gì xảy ra sau đó?

> Người trong nhóm **không** tính là bằng chứng. Phỏng vấn người **ngoài nhóm**.
