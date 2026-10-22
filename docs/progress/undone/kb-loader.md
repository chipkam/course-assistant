# 🔧 KB loader

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/kb.py` (`KnowledgeBase.load`, `validate`)
- **Test:** `src/tests/test_kb.py`
- **Nghiệm thu:** `tests.test_contract_kb` pass — `KnowledgeBase` khớp tuyệt đối
  `src/tests/golden/kb.json`, `validate()` trả `[]` (hợp đồng: `docs/contracts.md` §4)

Nền của phần query — nên làm sớm, song song với Phần I.

## Việc cần làm
- [ ] Đọc 6 file `src/data/kb/*.txt` (mỗi file một format riêng) thành cấu trúc tra được (dict/index).
- [ ] Index theo ID chuẩn: `WEEK_NN`, `CHNN`, `LOx.y`, `PART_I..IV`, ID resource/rule.
- [ ] `validate()`: kiểm schema và tham chiếu chéo (chương trong lịch phải có trong topics, …).

## Ghi chú
- Tham khảo cách làm: `docs/knowledge/kb-loader.md`.
- Run time chỉ bước **query** mới mở KB; bước intent không đọc KB.
