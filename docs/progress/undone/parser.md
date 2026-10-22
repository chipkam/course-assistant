# ⚙️ Parser (Phần I)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/parser.py` (`EarleyParser.parse`)
- **Output:** `src/output/parse-results.txt`
- **Test:** `src/tests/test_parser_generator.py`
- **Nghiệm thu:** `tests.test_contract_parser` pass (hợp đồng: `docs/contracts.md` §2)

Cần trước: `tokenizer-grammar-loader.md`.

## Việc cần làm
- [ ] Đi ngược câu → cây (Earley hoặc backtracking), dựng cây có nhãn để semantic đọc nhánh `Q_*`.
- [ ] Câu ngoài grammar xuất `()`.
- [ ] Ghi `parse-results.txt`.

## Ghi chú
- Grammar hiện tại không có câu mơ hồ (đã kiểm phase 1). Nếu sau này có, parser phải chọn cây
  một cách xác định (deterministic).
- Lý thuyết: `docs/04-parser.md`.
