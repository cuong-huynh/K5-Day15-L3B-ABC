# CP4 — Text dán form (nhóm ABC · A2)

> Đội trưởng nộp bằng mã **2A202603866** trước **14:30 Thứ Bảy 28/11**.  
> Kiểm lại: mở mọi link bằng **cửa sổ ẩn danh** · `python run.py check` · PDF + video mở được.  
> **File này là nháp để Cường check trên `main` — chưa tự nộp form.**

Repo: https://github.com/cuong-huynh/K5-Day15-L3B-ABC

---

## Ô · Kết quả lượt 1 → lượt 2 + cải tiến + run ID

```
Lượt 1: 24/24 (100%) — run-1@20261128-064545 · model openai/gpt-oss-20b (Groq).
Cải tiến: soft-fail B15–B21 — lý do escalate quá chung → thêm out_of_scope_reason() (Gate/LMS/Phoenix/nộp nhầm/refresh/điểm) trong codebase/agent.py. Không sửa expected / benchmark / chuẩn đạt §7.
Lượt 2: 24/24 (100%) — run-2@20261128-132500 · model DeepSeek-V4.1-Flash (FPT). ĐẠT chuẩn §7 (≥70% + 100% tu_choi).
CSV: https://github.com/cuong-huynh/K5-Day15-L3B-ABC/blob/main/eval/run-2.csv
Report: https://github.com/cuong-huynh/K5-Day15-L3B-ABC/blob/main/eval/report.md
```

---

## Ô · Chi phí khi dùng thật (simulate + estimate)

```
Mô phỏng: cost/simulate-1.csv · 50 phiên · seed 42 · simulate-1@20261128-132714. Token đo trên DeepSeek-V4.1-Flash; giá theo deepseek-flash + gemini-3.1-flash-lite.
Chi phí / task thành công (cơ sở): ~$0.00030 (deepseek-flash) · ~$0.00066 (gemini-3.1-flash-lite).
Chi phí / tháng (deepseek-flash): thấp ~$0.29 (300) · cơ sở ~$0.68 (700) · cao ~$0.97 (1000).
Độ nhạy (vì lượt 2 = 100%): 90% → ~$0.00033/task · 80% → ~$0.00038/task.
So impact §2 (~45 phút/người/tháng): đáng làm — API ~24₫/người/tháng (cơ sở).
Chi tiết: https://github.com/cuong-huynh/K5-Day15-L3B-ABC/blob/main/cost/cost-estimate.md
```

---

## Ô · Link demo-slides.pdf (8 trang)

```
https://github.com/cuong-huynh/K5-Day15-L3B-ABC/blob/main/demo-slides.pdf
```

---

## Ô · Video dự phòng demo (mở ẩn danh)

```
[ĐIỀN SAU KHI DUY/CƯỜNG QUAY XONG — Drive/YouTube, quyền Anyone with the link]
```

Gợi ý nội dung (≥ CP3 30s): câu thường lab 3 (AN-04) + câu khó lab 4 mâu thuẫn hoặc Gate/LMS escalate.

---

## Ô · Link spec.md (§0–§9 + §10)

```
https://github.com/cuong-huynh/K5-Day15-L3B-ABC/blob/main/spec.md
```

Chuẩn đạt (đã chốt CP2, **không sửa**):
```
Đạt khi ≥70% câu qua, và 100% câu tu_choi qua (không bịa hạn/nguồn; không chắc hoặc không có đúng một căn cứ thì hỏi lại hoặc chuyển TA).
```

---

## Ô · Phần chưa xong (khai thật)

```
Đã xong trên main: cải tiến escalate B15–B21, lượt 2 24/24, simulate-1 (50), cost-estimate, demo-slides.pdf, spec §8.
Chưa xong / đang làm: video dự phòng demo zone (quay + dán link); validation/log.md (bonus); reflection từng người → 23:59.
```

---

## Checklist trước khi bấm nộp

- [ ] Mã học viên đội trưởng: `2A202603866`
- [ ] Link repo / PDF / cost / eval trên **`main`** mở được ẩn danh
- [ ] Video dự phòng đã dán + mở được ẩn danh
- [ ] Số 24/24 × 2 lượt + run ID khớp CSV
- [ ] Cường đã đọc draft này và OK nộp
