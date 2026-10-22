# 🔧 Script kiểm tra grammar dùng chung

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **File đề xuất:** `tools/check_grammar.py`

Hai lỗi nặng nhất phase 1 (#3 crash, #2 lệch tokenizer) script này bắt được ngay. Mỗi người chạy
trước khi mở PR.

## Việc cần làm
- [ ] Load grammar bằng code chuẩn của nhóm; báo non-terminal chưa định nghĩa / không dùng tới /
      định nghĩa 2 lần / terminal viết hoa; đếm đủ 26 nhánh.
- [ ] Chạy câu mẫu, câu thách thức và hội thoại; in câu rớt theo nhánh.
- [ ] Sinh câu → parse lại; đếm số cây parse (> 1 = mơ hồ).
- [ ] Chạy cả pipeline trên câu sinh ra: intent ≠ UNKNOWN, entity ≠ None, query tìm thấy.

## Ghi chú
- Các bước đã dùng để gộp phase 1: `done/phase1-grammar-merge.md`, mục "Cách kiểm tra". Khi code
  của nhóm chưa xong thì chạy bằng code của nhánh `sample`.
- `tools/make_golden.py` đã có sẵn phần lấy code `sample` qua `git archive` và chạy trên
  `src/data/` — dùng lại cách đó. Sau khi đổi grammar, chạy lại nó rồi chạy test hợp đồng.
