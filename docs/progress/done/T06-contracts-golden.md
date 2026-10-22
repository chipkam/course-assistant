# T06 · 🔧 Cố định I/O giữa các tầng: hợp đồng + golden test

- **Trạng thái:** xong
- **Phụ trách:** Phúc
- **Ngày xong / Commit:** 22/10/2026 · commit chứa file này

## Đã làm

- [x] `docs/contracts.md`: cứng / lỏng cho từng tầng; bảng 26 nhánh → intent / entity / slots;
      bảng `kind` → `data` / `sources`; cấu trúc `KnowledgeBase`; luật dialogue; quy trình đổi
      hợp đồng.
- [x] `tools/make_golden.py`: chạy code nhánh `sample` (đóng băng) với `src/data/` hiện tại, ghi
      golden vào `src/tests/golden/` (2049 câu tokenizer/parser, 2027 cây → frame, 192 frame →
      result/answer, 6 hội thoại, 50 câu end-to-end, `kb.json`).
- [x] `src/tests/test_contract_*.py` (8 file) + `contract_support.py`: mỗi tầng test độc lập trên
      đầu vào golden của nó; tầng chưa làm → skip.
- [x] Sửa 3 kết quả của sample trong golden: output Phần II/III/IV phải `found = False`.
- [x] Hằng `NOT_FOUND` trong `answer.py` theo nguyên văn đề ("…trong dữ liệu **của** môn học.").

## Kiểm chứng

- Chạy bộ test bằng code sample: pass hết, trừ đúng 3 bản ghi bug đã sửa (test bắt được bug).
- Chạy trên skeleton `main`: toàn bộ test hợp đồng skip, không fail.

## Ghi chú

- Đổi `src/data/` (grammar, KB, câu test) → chạy lại `python tools/make_golden.py`.
- Không sửa tay golden; đổi hợp đồng theo `docs/contracts.md` §10.
