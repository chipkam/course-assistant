# T16 · 🔧 Ghép pipeline + CLI + ghi output (`run.py all`)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/pipeline.py` (`CourseAssistant.from_paths`), `cli.py`,
  `output.py`, `paths.py`, `utils.py`, `src/run.py`
- **Output:** cả 9 file trong `src/output/`
- **Nghiệm thu:** `tests.test_contract_pipeline` pass; `python run.py all` (trong `src/`) sinh đủ
  9 file từ `input/sentences.txt`

Cần trước: T08, T09, T11, T12, T13, T14 (T15 nếu làm Phần III).

## Việc cần làm
- [ ] Hàm cần viết: `ProjectPaths.discover`, `CourseAssistant.from_paths`, `write_grammar`, `write_samples`, `write_pipeline_outputs`; `cli.py` đã có khung lệnh.
- [ ] Test mẫu `src/tests/test_pipeline.py`: thay `skipTest` TODO chạy end-to-end `sample_queries.txt`.
- [ ] `ProjectPaths.discover()` — tìm project root không phụ thuộc cwd.
- [ ] `CourseAssistant.from_paths`: load grammar, lexicon, KB (+ `validate()`), dựng các tầng.
- [ ] `cli.py`: lệnh `all`, `parse`, `answer`, `generate`, `evaluate` (+ `interactive` nếu kịp).
- [ ] Reader của `input/sentences.txt`: bỏ dòng trống và dòng bắt đầu bằng `#`; chạy theo thứ tự,
      **giữ ngữ cảnh** giữa các dòng (câu "Nó…", "Phần đó…" tham chiếu câu trước).
- [ ] `output.py`: `write_grammar`, `write_samples` (≤ 10 000), `write_pipeline_outputs`
      (`parse-results.txt`, `semantic.txt`, `intent-entity.txt`, `query.txt`, `answer.txt`), cùng
      `dialogue.txt`, `evaluation.txt` (từ `evaluate.py`) — **định dạng đúng `docs/contracts.md` §9**
      (đã chốt theo sample).
- [ ] Chạy `python run.py all`, so từng file với bản của sample về định dạng.

## Ghi chú
- Tham khảo định dạng của sample: `git show sample:docs/sample-src/output/<file>.txt`.
