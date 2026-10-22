# Progress — theo dõi tiến độ BTL

Mỗi việc là **một file `.md`**:

- `undone/` — việc chưa xong (chưa làm hoặc đang làm).
- `done/` — việc đã xong, kèm kết quả và commit.

Xong một việc: `git mv docs/progress/undone/<việc>.md docs/progress/done/`, rồi điền
**Ngày xong**, **Commit** và **Kết quả** trong file. Việc mới phát sinh thì tạo file mới
trong `undone/`.

Legend dùng trong tiêu đề (giữ từ `docs/todo.md`): 🔥 tốn công/ăn điểm · ⚙️ chuẩn, làm 1 lần ·
🔧 plumbing · ✨ optional (điểm cộng).

## Mẫu file

```markdown
# 🔧 Tên việc

- **Trạng thái:** chưa làm | đang làm | xong
- **Phụ trách:** <tên> (chưa giao)
- **Output:** <file sinh ra, nếu có>
- **Ngày xong / Commit:** <điền khi chuyển sang done/>

## Việc cần làm
- [ ] ...

## Ghi chú
```

## Quy ước làm việc (rút từ review phase 1)

- **PR nhỏ, đúng phạm vi, rebase lên `main` trước khi mở.**
- **Grammar:** giữ đúng 26 nhánh `Q_*` của `QUESTION`. Câu mới = thêm alternative vào nhánh có
  sẵn, không thêm nhánh mới.
- **Dùng lại biến có sẵn, không định nghĩa lại biến đã có.** Biến dùng chung (`YES_NO`,
  `TOPIC_ENTITY`, `ASSIGNMENT_PART`, `ASSIGNMENT_ENTITY`, `CONTEXT_REFERENCE`, `COURSE_SUBJECT`)
  muốn sửa phải báo cả nhóm.
- **Tiêu chí nghiệm thu một nhánh grammar:** pass toàn bộ câu mẫu thuộc nhánh; không làm rớt câu
  nào đang pass; không sinh câu mơ hồ; đọc 20 câu sinh ngẫu nhiên không có câu vô nghĩa.
- **Nhánh `sample` là bản tham khảo, đóng băng** — không commit vào đó.
