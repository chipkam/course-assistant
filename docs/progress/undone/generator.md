# ⚙️ Generator (Phần I)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/generator.py`, `output.py`
- **Output:** `src/output/samples.txt`
- **Nghiệm thu:** mọi câu sinh ra parse lại được bằng parser của nhóm; ≤ 10 000 câu; đủ 26 nhánh
  (cách sinh là phần lỏng — `docs/contracts.md`)

## Việc cần làm
- [ ] Sinh câu hợp lệ từ grammar, **≤ 10 000 câu**, chia đều giữa các nhánh `Q_*`.
- [ ] Mọi câu sinh ra phải parse lại được và không lộ tên non-terminal.
- [ ] Ghi `samples.txt`.

## Ghi chú
- Lý thuyết: `docs/knowledge/07-generator.md`.
