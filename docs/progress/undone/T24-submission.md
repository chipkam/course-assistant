# T24 · 🔧 Đóng gói nộp bài

- **Trạng thái:** chưa làm
- **Phụ trách:** chưa giao
- **Yêu cầu:** đề mục 7.4

## Việc cần làm
- [ ] Tên file: `MSSV1-MSSV2-MSSV3-MSSV4.zip`, dung lượng **< 10 MB** (file lớn → upload nơi khác,
      để link trong README).
- [ ] Cấu trúc tối thiểu theo đề:
      ```
      project/
        src/  data/  models/  input/  output/
        README.md  Dockerfile
      ```
      Repo hiện để `data/`, `input/`, `output/`, `models/`, `Dockerfile`, `README.md` **bên trong
      `src/`** → khi đóng gói phải sắp lại cho đúng cấu trúc trên, và kiểm tra code vẫn tìm được
      data (`ProjectPaths`).
- [ ] Không đưa vào zip: `tests/golden/` (2,2 MB, chỉ dùng nội bộ), `docs/` nội bộ, `tools/`,
      `__pycache__/`, `data/` gốc cũ ở gốc repo.
- [ ] `output/` trong zip là kết quả chạy thật của code nhóm (`python run.py all`), không chép từ
      sample.
- [ ] Giải nén zip ra thư mục mới, build Docker và chạy thử trước khi nộp.
