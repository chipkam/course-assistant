# 🔧 Quyết định về pipeline trong PR #2 (Bách)

- **Trạng thái:** xong
- **Phụ trách:** Phúc (lead)
- **Ngày xong / Commit:** 22/10/2026 · commit chứa file này

PR #2 tự hiện thực toàn bộ pipeline (loader, tokenizer, parser, semantic, KB, query, answer,
evaluate, CLI), 12 file docs, 9 file test (50 test pass) — ngoài phạm vi phase 1.

## Quyết định

**Codebase chuẩn = skeleton trên `main`** (`src/hcmut/iaslab/nlp/app/`, dựng theo bản tham
khảo ở nhánh `sample`). Không dùng code của PR #2 làm nền; PR #2 đóng, không merge.

Lý do:
- Skeleton đã cố định I/O giữa các tầng (`docs/contracts.md`) và có golden test cho từng tầng —
  cả nhóm code theo một khung, nghiệm thu bằng máy.
- Tokenizer của PR #2 tách `context-free` thành 3 token, lệch grammar `src/data/grammar.cfg`
  (232 câu sinh ra không parse lại được); PR #2 cũng viết lại `entities.txt`,
  `sample_queries.txt`, `dialogues.txt` theo format riêng.

## Phần của PR #2 vẫn dùng được

- Phần grammar (entity list, `môn học`, `tài liệu tham khảo…`) đã gộp vào `main` —
  `phase1-grammar-merge.md` mục 3.2.
- Code trong PR có thể **chuyển dần vào đúng module của skeleton** khi Bách nhận task tầng
  tương ứng: cách làm bên trong mỗi tầng là tự do, miễn pass test hợp đồng của tầng đó
  (`docs/contracts.md`).
