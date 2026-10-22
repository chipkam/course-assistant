# 🔧 Ghép pipeline + CLI + ghi output (`run.py all`)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/pipeline.py` (`CourseAssistant.from_paths`), `cli.py`,
  `output.py`, `utils.py`, `src/run.py`
- **Output:** cả 9 file trong `src/output/`
- **Nghiệm thu:** `tests.test_contract_pipeline` pass; `python run.py all` (trong `src/`) sinh đủ
  9 file từ `input/sentences.txt`

Cần trước: các tầng còn lại (ít nhất tokenizer, parser, semantic, KB, query, answer).

## Việc cần làm
- [ ] `CourseAssistant.from_paths`: load grammar, lexicon, KB (+ `validate()`), dựng các tầng.
- [ ] `cli.py`: lệnh `all`, `parse`, `answer`, `generate`, `evaluate` (+ `interactive` nếu kịp).
- [ ] Reader của `input/sentences.txt`: bỏ dòng trống và dòng bắt đầu bằng `#`; chạy theo thứ tự,
      **giữ ngữ cảnh** giữa các dòng (câu "Nó…", "Phần đó…" tham chiếu câu trước).
- [ ] `output.py`: `write_grammar`, `write_samples` (≤ 10 000), `write_pipeline_outputs`
      (`parse-results.txt` in `()` cho câu ngoài văn phạm, `semantic.txt`, `intent-entity.txt`,
      `query.txt`, `answer.txt`), cùng `dialogue.txt`, `evaluation.txt` (từ `evaluate.py`).
- [ ] **Chốt định dạng 9 file** (`docs/contracts.md` §9 để lỏng): theo placeholder hiện có trong
      `src/output/` (ví dụ `query.txt` = `ID<TAB>query<TAB>status<TAB>source`) hay theo sample.
      Ghi lại quyết định vào §9.

## Ghi chú
- Tham khảo định dạng của sample: `git show sample:docs/sample-src/output/<file>.txt`.
