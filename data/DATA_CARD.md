# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · announcements (thông báo Discord mẫu)

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `search_announcements` · bộ câu thử A2 · không dùng để đào bằng chứng pain |
| Từ đâu | nhóm tự viết (synthetic), mô phỏng kênh announcements Discord khoá L3B |
| Xử lý những bước gì | viết tay · gắn `lab` / `class` / `official` · `supersedes` khi có bản thay · lọc tin không official khi tra hạn |
| Số dòng / số đoạn | 8 thông báo trong `data/announcements.json` |
| Phiên bản / ngày lấy | 2026-11-27 · nhánh prototype A2 (Duy) + DATA_CARD nhóm |
| Nhãn | `synthetic` |
| Giới hạn | Không phải thông báo Discord thật. Có: bản đổi hạn Lab 3 (AN-04 supersedes AN-03); mâu thuẫn Lab 4 (AN-05 vs AN-06); tin đồn Lab 5 (`official: false`); tin Lab 6 chứa chỉ dẫn chèn. |

**Data `synthetic` (nhóm tự sinh):** viết tay; người kiểm: nhóm ABC (Duy + Cường). Data tự dựng **không phải bằng chứng pain**.
