# Progress — theo dõi tiến độ BTL

> Cái nào **thầy cho sẵn**, cái nào **mình phải tự xây**. Đầu tư: **~70% vào
> Grammar + Cây→Intent**, 30% cho đường ống còn lại. Lý thuyết từng trạm: `docs/knowledge/`.

Mỗi việc là **một file `.md`**:

- `undone/` — việc chưa xong (chưa làm hoặc đang làm).
- `done/` — việc đã xong, kèm kết quả và commit.

Xong một việc: `git mv docs/progress/undone/<việc>.md docs/progress/done/`, rồi điền
**Ngày xong**, **Commit** và **Kết quả** trong file. Việc mới phát sinh thì tạo file mới
trong `undone/`.

Legend dùng trong tiêu đề: ✅ có sẵn · 🔥 tốn công/ăn điểm · ⚙️ chuẩn, làm 1 lần ·
🔧 plumbing · ✨ optional (điểm cộng).

## Bản đồ việc → file

| Nhóm | Việc | File |
| --- | --- | --- |
| Thầy cho sẵn ✅ | intent, entity vocab, KB, test có đáp án | `done/provided-data.md` |
| Nền | 🔧 Đồng bộ `src/data/` với data đầy đủ | `done/sync-src-data.md` |
| Nền | 🔧 KB loader | `undone/kb-loader.md` |
| Nền | ⚙️ Paths, tokenizer, grammar loader | `undone/tokenizer-grammar-loader.md` |
| Phần I | 🔥 Grammar (CFG) — phase 1 | `done/phase1-grammar-merge.md` |
| Phần I | 🔥 Grammar — việc còn lại, `output/grammar.txt` | `undone/grammar-followups.md` |
| Phần I | ⚙️ Parser | `undone/parser.md` |
| Phần I | ⚙️ Generator | `undone/generator.md` |
| Phần II | 🔥 Cây → semantic + Intent/Entity | `undone/semantic-intent-entity.md` |
| Phần II | 🔧 Query builder | `undone/query-builder.md` |
| Phần II | 🔧 Answer + not-found | `undone/answer-not-found.md` |
| Ghép | 🔧 Pipeline + CLI + ghi 9 file output (`run.py all`) | `undone/pipeline-cli-output.md` |
| Phần IV | 🔧 Evaluation + mở rộng bộ test | `undone/evaluation.md` |
| Optional | ✨ Phần III — Dialogue | `undone/dialogue.md` |
| Optional | ✨ Phần II Lựa chọn 2 — RAG/LLM | `undone/rag-llm.md` |
| Nộp bài | 🔥 Báo cáo (+ ghi nguồn, khai báo AI) | `undone/report.md` |
| Nộp bài | 🔧 Video demo + thuyết trình | `undone/demo-video.md` |
| Nộp bài | 🔧 README, Dockerfile, đóng gói zip | `undone/readme.md`, `undone/dockerfile.md`, `undone/submission.md` |
| Quy trình | 🔧 Hợp đồng giữa các tầng + golden test | `done/contracts-golden.md` |
| Quy trình | 🔧 Quyết định treo, codebase PR #2, đóng PR phase 1, script check grammar | `undone/open-decisions.md`, `undone/pr2-pipeline-decision.md`, `undone/close-phase1-prs.md`, `undone/check-grammar-script.md` |

## Ai đọc KB khi nào (đừng lẫn)

- **Design time (bạn):** đọc `entities.txt` (schema + vocab) để viết grammar/intent.
- **Run time (máy):** bước intent **KHÔNG** đọc KB; chỉ bước **query** mới mở `src/data/kb/` —
  "có thì bóc, không thì rỗng". Chi tiết: `docs/knowledge/03-grammar-vs-kb.md`.

## Mẫu file

```markdown
# 🔧 Tên việc

- **Trạng thái:** chưa làm | đang làm | xong
- **Phụ trách:** <tên> (chưa giao)
- **Output:** <file sinh ra, nếu có>
- **Ngày xong / Commit:** <điền khi chuyển sang done/>

## Việc cần làm
- [ ] ...

## Ghi chú
```

## Quy ước làm việc (rút từ review phase 1)

- **Trước khi code một tầng: đọc `docs/contracts.md`.** Nghiệm thu = test hợp đồng của tầng đó
  pass (`cd src && python -m unittest tests.test_contract_<tầng>`); ghi trong mục **Nghiệm thu**
  của từng file `undone/`. Cách làm bên trong tầng là tự do.
- **PR nhỏ, đúng phạm vi, rebase lên `main` trước khi mở.**
- **Grammar:** giữ đúng 26 nhánh `Q_*` của `QUESTION`. Câu mới = thêm alternative vào nhánh có
  sẵn, không thêm nhánh mới.
- **Dùng lại biến có sẵn, không định nghĩa lại biến đã có.** Biến dùng chung (`YES_NO`,
  `TOPIC_ENTITY`, `ASSIGNMENT_PART`, `ASSIGNMENT_ENTITY`, `CONTEXT_REFERENCE`, `COURSE_SUBJECT`)
  muốn sửa phải báo cả nhóm.
- **Tiêu chí nghiệm thu một nhánh grammar:** pass toàn bộ câu mẫu thuộc nhánh; không làm rớt câu
  nào đang pass; không sinh câu mơ hồ; đọc 20 câu sinh ngẫu nhiên không có câu vô nghĩa.
- **Nhánh `sample` là bản tham khảo, đóng băng** — không commit vào đó.
