# 🔧 Các quyết định đang treo

- **Trạng thái:** chưa làm
- **Phụ trách:** Phúc (+ cả nhóm)

Chốt trước khi giao việc code; ghi kết quả vào đây rồi chuyển file sang `done/`.

## Việc cần làm
- [ ] **Thành viên có được đọc code nhánh `sample` không?** Golden test đã đủ để nghiệm thu mà không
      cần đọc. Đọc thì nhanh nhưng dễ thành chép; không đọc thì hiểu bài hơn (đề mục 8: phải hiểu và
      giải thích lại được code).
- [ ] **Độ chặt của golden KB** (`docs/contracts.md` §4): đang khớp tuyệt đối `kb.json` (kể cả kiểu,
      ví dụ `chapter_number` là int). Giữ nguyên, hay nới thành "đúng khoá + kiểu"?
- [x] **Hướng Phần II**: Lựa chọn 1 — Classical (luật/keyword). **Không làm** Lựa chọn 2
      (LLM/RAG): đề cho chọn 1 trong 2, và LLM/RAG không thay được phần NLP cốt lõi (đề 7.3, 9).
- [x] **Codebase chuẩn**: skeleton trên `main` (theo `sample`), không dùng code PR #2 làm nền —
      `done/pr2-pipeline-decision.md`.
- [x] **Định dạng 9 file output**: theo sample — ghi tại `docs/contracts.md` §9.
- [ ] **Phân công đợt code**: ai nhận task nào trong `undone/`.
