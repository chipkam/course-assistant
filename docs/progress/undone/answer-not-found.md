# 🔧 Answer + not-found (Phần II)

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Code:** `src/hcmut/iaslab/nlp/app/answer.py`
- **Output:** `src/output/answer.txt`

## Việc cần làm
- [ ] Đổ template tiếng Việt cho từng loại `QueryResult`.
- [ ] Không có dữ kiện → báo lịch sự, **không bịa**.
- [ ] **`found` và câu trả lời phải khớp nhau.** Bug của sample cần tránh: hỏi output Phần III/IV
      (`Phần III cần xuất file gì?`) thì query báo `found=True` nhưng answer lại là "không tìm
      thấy". Nếu KB không có output của phần đó thì query phải trả `found=False`; nếu có thì
      template phải in ra.
- [ ] Thêm test cho đúng trường hợp trên.

## Ghi chú
- KB không có thông tin giảng viên → `Ai dạy NLP?` phải ra not-found (đúng như sample).
