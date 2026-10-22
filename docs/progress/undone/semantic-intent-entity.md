# 🔥 Cây → semantic + Intent/Entity (Phần II)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/semantic.py`, `entities.py`
- **Output:** `src/output/semantic.txt`, `src/output/intent-entity.txt`

## Việc cần làm
- [ ] `SemanticInterpreter.interpret`: lấy nhánh `Q_*` con của `QUESTION` → intent; mỗi nhánh một
      handler rút slot, ví dụ `GET_SCHEDULE(week=WEEK_03)`.
- [ ] Đọc entity qua node có tên (`WEEK_ENTITY`, `CHAPTER_ENTITY`, `TOPIC_ENTITY`, `LO_ENTITY`,
      `ASSIGNMENT_PART`, `ASSIGNMENT_FEATURE`, `RESOURCE_TOPIC`, `RULE_TOPIC`, `EXAM_ENTITY`).
      Grammar phase 1 giữ nguyên các node này cho mọi cách hỏi mới.
- [ ] `EntityLexicon`: load `src/data/scaffolding/entities.txt`, resolve về ID chuẩn
      (`WEEK_NN`, `CHNN`, `LOx.y`, `PART_I..IV`, topic / resource / rule ID).
- [ ] **FEAT_\* (ý của Khoa):** handler `Q_ASSIGNMENT_FEATURE` đọc **nhãn** node con
      (`FEAT_PARSING` → `PART_I`, `FEAT_SEMANTIC` → `PART_II`, `FEAT_CONTEXT` → `PART_III`,
      `FEAT_EVAL` → `PART_IV`) thay vì tra cứng 5 từ như sample. Xong thì làm tiếp mục FEAT_* trong
      `grammar-followups.md`.
- [ ] **Alias mới cho lexicon:** `dịch máy` → `MACHINE_TRANSLATION` (resource);
      `thư viện có sẵn` → `EXTERNAL_LIBRARIES` (rule).

## Ghi chú
- `ASSIGNMENT_PART` chỉ có `phần` / `part` + số La Mã i–iv; câu deadline luôn hỏi deadline chung
  của BTL (không theo phần).
- Lý thuyết: `docs/05-semantic-intent-entity.md`.
