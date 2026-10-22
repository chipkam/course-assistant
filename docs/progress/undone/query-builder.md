# 🔧 Query builder (Phần II)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/query.py` (`QueryEngine.execute`)
- **Output:** `src/output/query.txt`

- **Nghiệm thu:** `tests.test_contract_query` pass (hợp đồng: `docs/contracts.md` §5 — bảng
  `kind` / `data` / `sources`). Test dùng frame + KB golden nên **không phải chờ** semantic hay KB
  loader; chạy end-to-end mới cần hai task đó.

## Việc cần làm
- [ ] Predicate → truy vấn KB theo intent, **không đọc lại câu hỏi gốc**.
- [ ] Trả `QueryResult` có `found`, dữ kiện và nguồn (`kb/<file>.txt`).
- [ ] `found = False` khi dữ kiện rỗng — ví dụ output của Phần II/III/IV không có trong KB (bug
      của sample, golden đã sửa; xem §5).

## Ghi chú
- Lý thuyết: `docs/06-query-kb-answer.md`.
