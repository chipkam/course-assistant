# 🔧 Evaluation (Phần IV)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/evaluate.py`
- **Output:** `src/output/evaluation.txt`
- **Nghiệm thu:** `tests.test_contract_pipeline` pass — mọi câu sample làm đúng vẫn đúng; số câu
  cải tiến (C007, C008) được in ra (hợp đồng: `docs/contracts.md` §8)

## Việc cần làm
- [ ] Chạy `src/data/scaffolding/sample_queries.txt`, so EXPECTED (intent, entity, query status,
      answer facts), tính accuracy.
- [ ] Chạy riêng `challenge_queries.txt` cho error analysis.
- [ ] Phân tích ca sai theo tầng: grammar thiếu mẫu / semantic sai intent / entity sai / query sai.
- [ ] Mở rộng bộ test cho đủ loại đề yêu cầu (mục 6): câu hợp lệ, **nhiều cách diễn đạt** của cùng
      một yêu cầu (dùng các cách hỏi mới của phase 1), câu ngoài phạm vi, câu KB không có, câu ngữ
      cảnh. Câu tự viết đặt trong `challenge_queries.txt` hoặc file mới, **ghi rõ nguồn** (đề 7.2).
      Thêm câu thì chạy lại `python tools/make_golden.py`.

## Ghi chú
- Mốc tham chiếu (đo bằng code sample với grammar phase 1): 42/42 câu mẫu, 6/8 câu thách thức.
- Lý thuyết: `docs/knowledge/08-evaluation.md`.
