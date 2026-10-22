# ⚙️ Paths, tokenizer, grammar loader

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/paths.py`, `tokenizer.py`, `grammar.py`, `tree.py`

Bước 1 trong thứ tự hiện thực của `src/README.md`; parser, generator và semantic đều cần.

## Việc cần làm
- [ ] `ProjectPaths.discover()` — tìm project root không phụ thuộc cwd.
- [ ] Tokenizer khớp với terminal trong `src/data/grammar.cfg`: lowercase, giữ dấu tiếng Việt,
      giữ `context-free`, `llm/rag`, `lo2.5` là **1 token**, tách dấu câu `? ! . , : ;`,
      chuẩn hoá `L.O.2.5` → `lo2.5`.
- [ ] Grammar loader: đọc `%start`, `->`, `|`, alternative rỗng = ε; báo lỗi non-terminal chưa định nghĩa.

## Ghi chú
- Grammar phase 1 được kiểm bằng tokenizer của nhánh `sample`. Đổi quy tắc tách token thì phải
  kiểm lại grammar (bài học PR #2: `"context" "-" "free"` → 232 câu không parse lại được).
