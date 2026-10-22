# 🔧 Answer + not-found (Phần II)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/answer.py`
- **Output:** `src/output/answer.txt`
- **Nghiệm thu:** `tests.test_contract_answer` pass (hợp đồng: `docs/contracts.md` §6 — đúng loại
  câu trả lời + đủ dữ kiện bắt buộc; câu chữ tự do). Test dùng frame + result golden.

## Việc cần làm
- [ ] Đổ template tiếng Việt cho từng `kind` (bảng `data` ở §5).
- [ ] Không có dữ kiện → báo lịch sự, **không bịa**; dùng đúng 1 trong 3 hằng fallback.
- [ ] `found = True` thì không bao giờ trả câu fallback. Bug của sample (output Phần II/III/IV:
      `found = True` nhưng answer "không tìm thấy") được sửa ở tầng query (§5) — answer không cần
      tự đoán.

## Ghi chú
- KB không có thông tin giảng viên → `Ai dạy NLP?` phải ra not-found (đúng như sample).
