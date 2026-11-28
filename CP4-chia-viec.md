# CP4 — Chia việc nhóm ABC · A2 Discord hạn lab

> **Hạn nộp form: 14:30 Thứ Bảy 28/11** · Demo Zone 14:30–16:00 (L3B: C401 / E403)  
> Đội trưởng: Huỳnh Văn Cường · mã `2A202603866`  
> Chuẩn “đạt” §7 **không được sửa**. Form BTC nhìn **`main`**. Branch: xem `BRANCHES.md`.

## Checklist nộp CP4

- [ ] Lượt 1 → lượt 2: `eval/run-2.csv` + chấm `pass` + `score` + cập nhật `eval/report.md` · `eval/README.md`
- [ ] Một lần cải tiến có ghi rõ nhóm lỗi (soft-fail B15–B21: lý do escalate quá chung)
- [ ] Chi phí: `cost/personas.yaml` · `python run.py simulate` (≥50 phiên) · `cost/cost-estimate.md` (3 kịch bản + chi phí / task thành công + tên model)
- [ ] `spec.md` §0–§9 đủ số (impact, kết quả 2 lượt, chi phí) · §10 changelog
- [ ] `demo-slides.pdf` ở **thư mục gốc** repo (8 trang theo `slides/outline.md`)
- [ ] Video **dự phòng** demo (dài hơn video CP3 30s) — Drive/YouTube, mở được ẩn danh
- [ ] Form CP4 nộp đúng hạn · khai phần chưa xong (nếu có)
- [ ] *(Bonus)* `validation/log.md` — 2–3 người dùng thử

---

## Cải tiến chốt (một nhóm lỗi)

Lượt 1 **24/24** — không câu `pass=0`. Nhắm soft-fail:

> **Lý do chuyển TA quá chung** trên câu kho ngoài hạn lab (`B15`–`B21`): đang ghi “ngoài phạm vi điểm/điểm danh…” thay vì Gate / LMS / lỗi hệ thống / nộp nhầm…

Sửa trong `codebase/agent.py` (handoff / phân loại lý do). **Không** sửa `expected`, **không** bỏ câu thử, **không** sửa số lượt 1.

---

## Timeline

| Khi | Việc | Ai |
|---|---|---|
| **Ngay đầu (~5–10')** | Đọc file này · chốt phân công | **Cả nhóm** |
| ~10:00–11:30 | Sửa agent (B15–B21) → `eval` lượt 2 → chấm + report | **Cặp X** (Duy sửa · Cường+Tùng chấm) |
| ~11:00–12:30 | `personas.yaml` từ P1–P3 → `simulate --try` → `simulate` ≥50 → `cost-estimate.md` | **Cặp Y** (Tùng+Đức · Cường hỗ trợ số impact) |
| ~12:30–13:30 | Điền `slides/outline.md` → xuất `demo-slides.pdf` · quay video dự phòng | **Cường + Duy** |
| ~13:30–14:15 | `spec` §8–§9 · `CP4-form-draft.md` · merge/push `main` · thử máy demo | **Cường** |
| **Trước 14:30** | Nộp form · vào phòng | **Cường** |
| **14:30–16:00** | Demo Zone: 1 câu thường + 1 câu khó · mỗi người ≥1 phần slide | **Cả nhóm** |
| 16:00–18:00 | Demo Phòng *(nếu được chọn)* | Theo BTC |
| → **23:59** | Sửa theo góp ý + `spec` §10 · mỗi người 1 file `reflection/` | **Cả nhóm** |

Hai cặp **làm song song** sau khi chốt file này (X không đợi Y xong cost mới sửa agent).

---

## Theo người / branch

### Cặp X — Duy (`duy`) + Cường (`cuong` / `main`)

| Ai | Việc CP4 | Xong khi |
|---|---|---|
| **Duy** | Sửa lý do escalate / handoff trong `codebase/agent.py` cho B15–B21 · giữ `answer()` ổn định cho eval | Output escalate nêu đúng loại việc (Gate/LMS/lỗi hệ thống/…) |
| **Duy** | `python run.py eval` → `eval/run-2.csv` + `traces/run-2.jsonl` (model thật, cùng benchmark) | File có run ID + model + token |
| **Cường + Tùng** | Chấm cột `pass` · `python run.py score eval/run-2.csv` | In được % theo `thuong` / `kho` / `tu_choi` |
| **Cường** | Cập nhật `eval/report.md` (lượt 1→2, ≥3 lỗi cụ thể dù soft, đã sửa gì) · bảng lượt 2 trong `eval/README.md` · `spec.md` §7 + §10 | Người ngoài đọc report hiểu đo gì / ra số nào |
| **Cường** | Điều phối · `CP4-form-draft.md` · merge `main` · nộp form · máy demo (`.env` không commit) | Form trước 14:30 · demo chạy được 1 câu trong vòng 1 giờ trước lên |

### Cặp Y — Đức (`duc`) + Tùng (`CTT/QA`)

| Ai | Việc CP4 | Xong khi |
|---|---|---|
| **Đức** | Điền `cost/personas.yaml`: ≥3 persona từ P1–P3 (~2–4 lần/tháng) · users low/base/high (track A ~ lớp L3, nguồn brief) · bỏ “(ví dụ)” · ≥2 mức giá model | `simulate` không nhắc còn sót ví dụ |
| **Tùng** | `python run.py simulate --try` rồi `python run.py simulate` (≥50) · hỗ trợ chấm run-2 | Có `cost/simulate-N.csv` |
| **Tùng + Đức** | Điền `cost/cost-estimate.md`: chi phí / task thành công · 3 kịch bản · so impact §2 · nếu lượt 2 = 100% thì thêm dòng độ nhạy 90%/80% | Mọi số truy được về simulate hoặc nguồn ghi rõ |
| **Đức** | *(Bonus)* điều phối 2–3 người dùng thử → `validation/log.md` | Mỗi người 1 dòng quan sát + 4 dòng tổng hợp |

### Cả nhóm — slides + demo

| Ai | Việc | Xong khi |
|---|---|---|
| **Cường** (chủ) + hỗ trợ | 8 trang theo `slides/outline.md` → PDF tên **`demo-slides.pdf`** ở gốc repo | File nằm đúng thư mục gốc, mỗi trang ≥1 số/trích |
| **Duy** | Quay video dự phòng: câu thường (lab 3) + câu khó (lab 4 mâu thuẫn hoặc ngoài phạm vi) trên FE hoặc `python run.py` | Link Drive/YouTube mở ẩn danh |
| **Cả nhóm** | Điền bảng “Ai nói trang nào” trong `slides/outline.md` | Mỗi người ≥1 phần |

Gợi ý phân trang nói (chỉnh lại nếu cần):

| Trang | Người nói (gợi ý) |
|---|---|
| 1–2 Pain & impact | Đức |
| 3–4 Giải pháp & demo live | Duy |
| 5 Đánh giá lượt 1→2 | Tùng |
| 6–7 Chi phí & kết luận | Cường |
| 8 Nếu thêm 1 tuần | Luân phiên / Đức |

---

## Lệnh cần nhớ

```bash
# Cải tiến + lượt 2 (Cặp X)
python run.py eval --try          # kiểm model thật
python run.py eval                # → eval/run-2.csv
python run.py score eval/run-2.csv

# Chi phí (Cặp Y)
python run.py simulate --try      # 10 phiên
python run.py simulate            # ≥50 phiên

# Kiểm nhanh
python run.py check
```

Demo live gợi ý:

1. Thường: `hạn nộp lab 3 là khi nào?` → hạn + link AN-04  
2. Khó: `lab 4 hạn bao giờ` → mâu thuẫn / chuyển TA **hoặc** câu ngoài phạm vi (Gate/LMS)

---

## Không làm

- Sửa `spec.md` §7 chuẩn đạt  
- Sửa / xóa câu thử hoặc `expected` cho khớp output  
- Sửa số liệu / kết quả **lượt 1** đã nộp  
- Commit `.env` / API key  
- Nộp slide bằng link thay vì `demo-slides.pdf` ở gốc repo  

---

## Sau CP4 → 23:59

- Góp ý demo → sửa + ghi `spec.md` §10 (giờ · đổi gì · vì sao)  
- Chạy thêm eval thì thành `run-3.csv` (không ghi đè lượt cũ)  
- Mỗi người 1 file: `reflection/cuong.md` · `reflection/duc.md` · `reflection/duy.md` · `reflection/tung.md` (tên không dấu)
