# T10 · ⚙️ Generator (Phần I)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/generator.py`
- **Output:** danh sách câu cho `src/output/samples.txt` (ghi file ở T16)
- **Nghiệm thu:** mọi câu sinh ra parse lại được bằng parser của nhóm; ≤ 10 000 câu; đủ 26 nhánh
  (cách sinh là phần lỏng — `docs/contracts.md`)

## Việc cần làm
- [ ] Hàm cần viết: `SentenceGenerator.generate`.
- [ ] Sinh câu hợp lệ từ grammar, **≤ 10 000 câu**, chia đều giữa các nhánh `Q_*`.
- [ ] Mọi câu sinh ra phải parse lại được và không lộ tên non-terminal.
- [ ] Trả `GeneratorStats` (requested / produced / explored / truncated) cho T16 ghi file.

## Ghi chú
- Lý thuyết: `docs/knowledge/07-generator.md`.
