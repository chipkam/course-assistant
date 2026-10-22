
# TODO — Course Assistant (CO3085)

> Cái nào **thầy cho sẵn**, cái nào **mình phải tự xây**. Đầu tư: **~70% vào
> Grammar + Cây→Intent**, 30% cho đường ống còn lại.

**Checklist đã chuyển sang [`docs/progress/`](progress/README.md)** — mỗi việc một file, nằm trong
`undone/` (chưa xong) hoặc `done/` (đã xong). File này chỉ giữ phần định hướng.

Legend: ✅ đã có · 🔨 phải xây · 🔥 tốn công/ăn điểm · ⚙️ chuẩn, làm 1 lần · 🔧 plumbing · ✨ optional (điểm cộng)

---

## Bản đồ việc → file

| Nhóm | Việc | File |
| --- | --- | --- |
| Thầy cho sẵn ✅ | intent, entity vocab, KB, test có đáp án | `done/provided-data.md` |
| Nền | 🔧 KB loader | `undone/kb-loader.md` |
| Nền | ⚙️ Paths, tokenizer, grammar loader | `undone/tokenizer-grammar-loader.md` |
| Phần I | 🔥 Grammar (CFG) — phase 1 | `done/phase1-grammar-merge.md` |
| Phần I | 🔥 Grammar — việc còn lại, `output/grammar.txt` | `undone/grammar-followups.md` |
| Phần I | ⚙️ Parser | `undone/parser.md` |
| Phần I | ⚙️ Generator | `undone/generator.md` |
| Phần II | 🔥 Cây → semantic + Intent/Entity | `undone/semantic-intent-entity.md` |
| Phần II | 🔧 Query builder | `undone/query-builder.md` |
| Phần II | 🔧 Answer + not-found | `undone/answer-not-found.md` |
| Phần IV | 🔧 Evaluation | `undone/evaluation.md` |
| Optional | ✨ Phần III — Dialogue | `undone/dialogue.md` |
| Optional | ✨ Phần II Lựa chọn 2 — RAG/LLM | `undone/rag-llm.md` |
| Đóng gói | 🔧 README, Dockerfile | `undone/readme.md`, `undone/dockerfile.md` |

(đường dẫn tính từ `docs/progress/`)

---

## Ai đọc KB khi nào (đừng lẫn)

- **Design time (bạn):** đọc `entities.txt` (schema + vocab) để viết grammar/intent.
- **Run time (máy):** bước intent **KHÔNG** đọc KB; chỉ bước **query** mới mở `data/kb/` — "có thì bóc, không thì rỗng".
