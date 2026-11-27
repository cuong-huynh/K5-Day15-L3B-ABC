# Quy ước branch — nhóm ABC

> Cập nhật 27/11/2026. Mọi PR merge vào **`main`**. Form CP / BTC chỉ nhìn **`main`**.

## Sơ đồ

| Branch | Ai | Phần việc (ưu tiên sửa file này) |
|---|---|---|
| `main` | Cả nhóm (Cường merge) | Bản ổn định để nộp |
| `cuong` | Huỳnh Văn Cường (đội trưởng) | `spec.md` · `canvas.md` · `CP2-form-draft.md` · `TEAMS.md` · điều phối merge |
| `duc` | Nguyễn Phan Tuấn Đức | `evidence/interviews/` · `evidence/summary.md` · `evidence/hypothesis.md` |
| `duy` | Vũ Lương Duy | `codebase/` · `data/announcements.json` · `docs/connect-model.md` |
| `CTT/QA` | Cao Thanh Tùng | `eval/` · `data/DATA_CARD.md` · metric / benchmark |

## Cách làm hàng ngày

```bash
git checkout main
git pull origin main
git checkout <branch-cua-minh>
git merge main
# sửa → commit
git push -u origin <branch-cua-minh>
```

Rồi mở **Pull Request → `main`**. Cường review/merge (hoặc tự merge nếu đã thống nhất).

## Luật tránh conflict

1. Chỉ sửa file trong cột “Phần việc” của mình; cần đụng file chung thì báo Cường.
2. Trước khi PR: merge `main` vào branch mình.
3. Không push thẳng lên `main` trừ khi Cường đang hotfix nộp checkpoint.
4. Sau khi merge: xóa branch cũ nếu không còn dùng (tuỳ nhóm).

## Checkpoint

- Nộp form = link file trên **`main`**.
- Branch cá nhân chỉ là nơi làm dở; chưa merge thì BTC không thấy.
