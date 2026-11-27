# CP3 — Chia việc nhóm ABC · A2 Discord hạn lab

> **Hạn nộp: 10:00 Thứ Bảy 28/11** · Đội trưởng: Huỳnh Văn Cường · mã `2A202603866`  
> Chuẩn “đạt” §7 **không được sửa**. Branch: xem `BRANCHES.md`.

## Checklist nộp CP3

- [ ] `evidence/summary.md` — pain đạt ngưỡng ≥1 nguồn + ≥5 trích dẫn
- [ ] `eval/benchmark.csv` — **20–30** câu (≥5 `kho`, ≥2 `tu_choi`)
- [ ] Video **30 giây** — chạy thử **AI thật** (Drive/YouTube, mở được ẩn danh)
- [ ] Lượt 1: `eval/run-1.csv` + % đạt + run ID
- [ ] `spec.md` §0–§7 đã cập nhật số bằng chứng / impact
- [ ] Form CP3 nộp đúng hạn

---

## Timeline

| Khi | Việc | Ai |
|---|---|---|
| **Tối T6 (ưu tiên trước ngủ)** | Nối model thật + `eval --try` token > 0 | **Duy** (+ Cường hỗ trợ key) |
| Tối T6 | Hỏi ≥3 người ngoài nhóm, sửa P1–P3 + ngày giờ | **Đức** (+ cả nhóm mỗi người ≥1 cuộc) |
| Tối T6 → sáng T7 | Mở rộng benchmark → 20–30 câu; gắn `nguoi_dung: P*` | **Tùng** |
| **Sáng T7 trước 09:00** | `run.py eval` → chấm `pass` → `score` = lượt 1 | **Cả nhóm** (Duy chạy, Tùng+Cường chấm) |
| Sáng T7 | Quay video 30s + cập nhật `spec` §1–§2 + summary | **Cường** (+ Duy demo) |
| **Trước 10:00** | Push `main` + nộp form | **Cường** |

---

## Theo người / branch

### Cặp X — Duy (`duy`) + Cường (`cuong` / `main`)

| Ai | Việc CP3 | Xong khi |
|---|---|---|
| **Duy** | `.env` (không commit) · nối model trong `codebase/ai.py` theo `docs/connect-model.md` · `python run.py` + `python run.py eval --try` | Token > 0, hỏi “hạn lab 3” ra câu thật |
| **Duy** | `python run.py eval` → `eval/run-1.csv` | File có run ID + model |
| **Cường** | Điều phối · cập nhật `spec.md` §1–§2 (bằng chứng, impact) · quay/up video 30s · soạn text form CP3 · merge PR · nộp | Form nộp trước 10:00 |

### Cặp Y — Đức (`duc`) + Tùng (`CTT/QA`)

| Ai | Việc CP3 | Xong khi |
|---|---|---|
| **Đức** | Phỏng vấn người **ngoài nhóm** · sửa `P1.md`–`P3.md` (điền ngày) · `evidence/summary.md` đủ ≥5 trích | ≥3 người thật, summary đánh dấu đạt ngưỡng phỏng vấn |
| **Tùng** | Thêm câu vào `benchmark.csv` đến 20–30 · ≥5 `kho` · ≥2 `tu_choi` · ≥1/3 `nguoi_dung`/`data_that` · `run.py check` | Check hết cảnh báo CP3 về số câu / nguồn |

---

## Lệnh cần nhớ

```bash
# Nối model (Duy)
copy .env.example .env   # điền key, không commit .env
python run.py
python run.py eval --try

# Bộ câu thử (Tùng)
python run.py check

# Lượt 1 (cả nhóm)
python run.py eval
python run.py score eval/run-1.csv
```

## Video 30 giây (gợi ý kịch bản)

1. Mở terminal → `python run.py`  
2. Hỏi: `hạn nộp lab 3 là khi nào?` → hiện hạn + link (AI thật)  
3. Hỏi thêm 1 câu khó (lab 4 mâu thuẫn hoặc thiếu mã lab) → hỏi lại / chuyển TA  

## Không làm

- Sửa `spec.md` §7 chuẩn đạt  
- Sửa `expected` cho khớp output sau khi chạy  
- Commit API key / `.env`  
- Dùng thành viên nhóm ABC làm “người được phỏng vấn”
