# 🔧 Quyết định về pipeline trong PR #2 (Bách)

- **Trạng thái:** chưa làm
- **Phụ trách:** Phúc + cả nhóm

PR #2 tự hiện thực toàn bộ pipeline (loader, tokenizer, parser, semantic, KB, query, answer,
evaluate, CLI), 12 file docs, 9 file test (50 test pass) — ngoài phạm vi phase 1, chưa review.

## Việc cần làm
- [ ] Cả nhóm chọn **một** codebase/tokenizer làm chuẩn: code của Bách hay viết theo skeleton.
- [ ] Nếu dùng code của Bách: Bách mở PR riêng, rebase lên `main`, chỉnh tokenizer cho khớp
      `src/data/grammar.cfg` (`context-free` là 1 token).
- [ ] PR đó sẽ conflict với `src/data/scaffolding/` (Bách viết lại `entities.txt`,
      `sample_queries.txt`, `dialogues.txt`, `challenge_queries.txt` theo format riêng); giữ bản
      trên `main` trừ khi nhóm thống nhất đổi format. `kb/` và `faq.txt` giống hệt, không conflict.
- [ ] Cập nhật các task code trong `undone/` theo quyết định.
