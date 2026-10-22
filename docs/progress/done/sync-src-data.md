# 🔧 Đồng bộ `src/data/` với bộ dữ liệu của sample

- **Trạng thái:** xong
- **Phụ trách:** Phúc
- **Ngày xong / Commit:** 22/10/2026 · `687b9a0`

## Đã làm

- [x] Thay `src/data/kb/` và `src/data/scaffolding/` (trước đây là placeholder rút gọn, ví dụ
      `schedule.txt` 21 dòng) bằng nguyên bộ dữ liệu của nhánh `sample`
      (`docs/sample-src/data/`, `schedule.txt` 166 dòng).
- [x] `grammar.cfg` không thay ở bước này (grammar làm riêng — xem
      [phase1-grammar-merge.md](phase1-grammar-merge.md)).
- [x] Cập nhật `src/README.md` và `src/data/README.md` cho khớp.

## Ghi chú

- `data/` ở gốc repo là bản gốc cũ của đề; `src/data/` giờ là bản đầy đủ hơn: KB giống hệt,
  `sample_queries.txt` / `dialogues.txt` được mở rộng, thêm `challenge_queries.txt`.
- Code đọc data qua `ProjectPaths.from_root(root)` → `root/data/...`, với root là `src/`.
- PR #2 (Bách) có sửa `entities.txt`, `sample_queries.txt`, `dialogues.txt`,
  `challenge_queries.txt` theo format code riêng — sẽ conflict nếu merge PR đó sau commit này
  (xem `undone/pr2-pipeline-decision.md`).
