# Knowledge — bài giảng pipeline NLP cổ điển

Đọc theo thứ tự: mỗi "nấc" là một trạm của pipeline, hai bài "ngang" là khái niệm chạy xuyên
nhiều trạm.

| Bài | Loại | Nội dung |
| --- | --- | --- |
| [00-background](00-background.md) | nền | vì sao pipeline cổ điển có 5 trạm |
| [01-what-is-language](01-what-is-language.md) | nấc 1 | ngôn ngữ vô hạn ↔ máy hữu hạn |
| [02-cfg-and-generation](02-cfg-and-generation.md) | nấc 2+3 | CFG, sinh câu, cây |
| [03-grammar-vs-kb](03-grammar-vs-kb.md) | ngang | entity nối grammar ↔ KB; design-time ↔ run-time |
| [04-parser](04-parser.md) | nấc 4 | câu → cây, backtracking, `()` |
| [05-semantic-intent-entity](05-semantic-intent-entity.md) | nấc 5 | cây → predicate (intent + entity) |
| [kb-loader](kb-loader.md) | ngang | đọc `src/data/kb/*.txt` thành tủ tra — nền của nấc 6 |
| [06-query-kb-answer](06-query-kb-answer.md) | nấc 6 | predicate → KB → câu trả lời, not-found |
| [07-generator](07-generator.md) | nấc 7 | grammar → câu mẫu |
| [08-evaluation](08-evaluation.md) | nấc 8 | chấm accuracy, phân tích ca sai |
| [09-optional-extensions](09-optional-extensions.md) | nấc 9 | Phần III (ngữ cảnh), RAG, đóng gói |
| [architecture](architecture.md) | tổng | bắt buộc vs đã chọn, module, thứ tự build |

Áp vào code của nhóm: hợp đồng giữa các tầng ở `docs/contracts.md`, việc cần làm ở
`docs/progress/`.
