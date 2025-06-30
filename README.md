# Hệ Thống Quản Lý Thực Đơn Ăn Uống

Đây là một ứng dụng quản lý thực đơn ăn uống được viết bằng Python, cho phép người dùng quản lý menu, hóa đơn, thống kê và nhiều chức năng khác.

## Cấu Trúc Thư Mục

```
baitaplon_python/
  ├── data/                  # Thư mục chứa dữ liệu
  │   ├── hoadon_data.json  # Dữ liệu hóa đơn
  │   ├── ke_hoach.json     # Dữ liệu kế hoạch thực đơn
  │   ├── lich_su.json      # Dữ liệu lịch sử
  │   ├── menu_data.json    # Dữ liệu menu
  │   └── user_data.json    # Dữ liệu người dùng
  ├── modules/               # Thư mục chứa các module chức năng
  │   ├── bill.py          # Module quản lý hóa đơn
  │   ├── export.py        # Module xuất báo cáo
  │   ├── menu.py          # Module quản lý menu
  │   ├── planner.py       # Module lập kế hoạch thực đơn
  │   ├── stats.py         # Module thống kê
  │   └── user.py          # Module quản lý người dùng
  ├── main.py               # File chính của ứng dụng
  └── requirements.txt      # File chứa các thư viện cần thiết
```

## Chi Tiết Các Module

### 1. File main.py

File chính của ứng dụng, chứa các chức năng:

#### Các Hàm Chính:

- `load_data(file_path, default)`: Đọc dữ liệu từ file JSON
- `save_data(file_path, data)`: Lưu dữ liệu vào file JSON
- `backup_data()`: Sao lưu toàn bộ dữ liệu
- `restore_data()`: Khôi phục dữ liệu từ bản sao lưu
- `system_info()`: Hiển thị thông tin hệ thống
- `main_menu()`: Menu chính của ứng dụng

#### Menu Chính Gồm Các Chức Năng:

1. Quản lý món ăn
2. Quản lý hóa đơn/giỏ hàng
3. Thống kê & báo cáo
4. Lập kế hoạch thực đơn
5. Quản lý người dùng
6. Xuất báo cáo
7. Sao lưu dữ liệu
8. Khôi phục dữ liệu
9. Thông tin hệ thống

### 2. Module menu.py

Module quản lý thực đơn với các chức năng:
- Thêm món ăn mới
- Sửa thông tin món ăn
- Xóa món ăn
- Hiển thị danh sách món ăn
- Tìm kiếm món ăn

### 3. Module bill.py

Module quản lý hóa đơn với các chức năng:
- Tạo hóa đơn mới
- Thêm món vào hóa đơn
- Tính tổng tiền
- Lưu và in hóa đơn
- Xem lịch sử hóa đơn

### 4. Module stats.py

Module thống kê với các chức năng:
- Thống kê doanh thu
- Thống kê món ăn bán chạy
- Phân tích xu hướng
- Báo cáo định kỳ

### 5. Module planner.py

Module lập kế hoạch thực đơn với các chức năng:
- Lập kế hoạch thực đơn theo ngày/tuần
- Quản lý thực đơn theo mùa
- Gợi ý món ăn
- Lưu và chỉnh sửa kế hoạch

### 6. Module user.py

Module quản lý người dùng với các chức năng:
- Thêm người dùng mới
- Sửa thông tin người dùng
- Xóa người dùng
- Phân quyền người dùng

### 7. Module export.py

Module xuất báo cáo với các chức năng:
- Xuất báo cáo doanh thu
- Xuất báo cáo thống kê
- Xuất danh sách món ăn
- Xuất lịch sử giao dịch

## Cấu Trúc Dữ Liệu

### 1. menu_data.json
```json
{
    "id": "string",
    "ten": "string",
    "gia": "number",
    "mo_ta": "string",
    "danh_muc": "string"
}
```

### 2. user_data.json
```json
{
    "id": "string",
    "ten": "string",
    "email": "string",
    "quyen": "string"
}
```

### 3. hoadon_data.json
```json
{
    "id": "string",
    "ngay": "datetime",
    "mon_an": ["array"],
    "tong_tien": "number",
    "khach_hang": "string"
}
```

### 4. ke_hoach.json
```json
{
    "ngay": "datetime",
    "thuc_don": ["array"],
    "ghi_chu": "string"
}
```

## Hướng Dẫn Sử Dụng

1. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

2. Chạy chương trình:
```bash
python main.py
```

3. Sử dụng menu để truy cập các chức năng

## Lưu Ý

- Đảm bảo tất cả các file JSON trong thư mục `data/` tồn tại trước khi chạy chương trình
- Nên sao lưu dữ liệu thường xuyên để tránh mất mát
- Kiểm tra quyền truy cập khi thực hiện các thao tác quan trọng 