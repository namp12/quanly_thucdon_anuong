# Hệ thống Quản lý Thực đơn Ăn uống

## Mô tả
Hệ thống quản lý thực đơn ăn uống với các chức năng:
- Quản lý món ăn, thực đơn, chế độ ăn
- Lập kế hoạch thực đơn theo tuần
- Quản lý hóa đơn và giỏ hàng
- Thống kê doanh thu và calo
- Xuất báo cáo PDF/Excel
- Gửi email hóa đơn

## Cài đặt

1. Cài đặt Python 3.7+
2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

## Sử dụng

Chạy chương trình:
```bash
python main.py
```

## Cấu trúc thư mục
```
baitaplon_python/
├── main.py                 # File chính
├── requirements.txt        # Thư viện cần thiết
├── README.md              # Hướng dẫn
├── modules/               # Các module chức năng
│   ├── menu.py           # Quản lý món ăn
│   ├── bill.py           # Hóa đơn, giỏ hàng
│   ├── stats.py          # Thống kê
│   ├── export.py         # Xuất báo cáo
│   ├── planner.py        # Lập kế hoạch
│   └── user.py           # Quản lý người dùng
└── data/                 # Dữ liệu JSON
    ├── menu_data.json    # Danh sách món ăn
    ├── user_data.json    # Danh sách người dùng
    ├── hoadon_data.json  # Danh sách hóa đơn
    ├── ke_hoach.json     # Kế hoạch tuần
    └── lich_su.json      # Lịch sử món ăn
```

## Chức năng chính

### 1. Quản lý món ăn
- Thêm, sửa, xóa món ăn
- Tìm kiếm theo tên, loại, chế độ ăn
- Hiển thị thực đơn có lọc

### 2. Quản lý hóa đơn
- Tạo hóa đơn mới
- Thêm món vào hóa đơn
- Tính tổng tiền tự động

### 3. Thống kê & Báo cáo
- Thống kê doanh thu
- Món phổ biến
- Biểu đồ calo/chi phí

### 4. Lập kế hoạch
- Lập kế hoạch thực đơn tuần
- Lưu lịch sử món ăn ngày

### 5. Quản lý người dùng
- Thêm, sửa, xóa người dùng
- Phân quyền (admin/nhanvien/khach)

### 6. Xuất báo cáo
- Xuất hóa đơn PDF
- Xuất thực đơn Excel
- Gửi email

## Dữ liệu mẫu
Chương trình đã có sẵn dữ liệu mẫu:
- 8 món ăn đa dạng
- 5 người dùng với các quyền khác nhau
- 5 hóa đơn mẫu
- Kế hoạch thực đơn tuần
- Lịch sử món ăn 7 ngày

## Lưu ý
- Dữ liệu được lưu trong file JSON UTF-8
- Có thể mở rộng thêm chức năng theo nhu cầu
- Giao diện dòng lệnh dễ sử dụng 