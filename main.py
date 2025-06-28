import os
import sys
import json
import shutil
from datetime import datetime
from modules import menu, bill, stats, export, planner, user

def load_data(file_path, default):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default

def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def backup_data():
    """Sao lưu dữ liệu"""
    backup_dir = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    data_files = ["menu_data.json", "user_data.json", "hoadon_data.json", 
                  "ke_hoach.json", "lich_su.json"]
    
    for file in data_files:
        src = os.path.join("data", file)
        if os.path.exists(src):
            dst = os.path.join(backup_dir, file)
            shutil.copy2(src, dst)
    
    print(f"Đã sao lưu dữ liệu vào thư mục: {backup_dir}")

def restore_data():
    """Khôi phục dữ liệu từ backup"""
    backup_dirs = [d for d in os.listdir() if d.startswith("backup_")]
    if not backup_dirs:
        print("Không có bản sao lưu nào!")
        return
    
    print("Các bản sao lưu có sẵn:")
    for i, dir in enumerate(backup_dirs):
        print(f"{i+1}. {dir}")
    
    try:
        chon = int(input("Chọn bản sao lưu để khôi phục: ")) - 1
        if 0 <= chon < len(backup_dirs):
            backup_dir = backup_dirs[chon]
            data_files = ["menu_data.json", "user_data.json", "hoadon_data.json", 
                         "ke_hoach.json", "lich_su.json"]
            
            for file in data_files:
                src = os.path.join(backup_dir, file)
                if os.path.exists(src):
                    dst = os.path.join("data", file)
                    shutil.copy2(src, dst)
            
            print(f"Đã khôi phục dữ liệu từ: {backup_dir}")
        else:
            print("Lựa chọn không hợp lệ!")
    except ValueError:
        print("Vui lòng nhập số!")

def system_info():
    """Hiển thị thông tin hệ thống"""
    print("\n=== THÔNG TIN HỆ THỐNG ===")
    print(f"Thời gian hiện tại: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Đếm số lượng dữ liệu
    menu_count = len(menu.load_menu())
    user_count = len(user.load_users())
    bill_count = len(bill.load_hoadon())
    
    print(f"Số món ăn: {menu_count}")
    print(f"Số người dùng: {user_count}")
    print(f"Số hóa đơn: {bill_count}")
    
    # Kiểm tra dung lượng thư mục data
    data_size = 0
    if os.path.exists("data"):
        for file in os.listdir("data"):
            file_path = os.path.join("data", file)
            if os.path.isfile(file_path):
                data_size += os.path.getsize(file_path)
    
    print(f"Dung lượng dữ liệu: {data_size/1024:.2f} KB")

def main_menu():
    while True:
        print("\n" + "="*50)
        print("🍽️  HỆ THỐNG QUẢN LÝ THỰC ĐƠN ĂN UỐNG 🍽️")
        print("="*50)
        print("1. 📋 Quản lý món ăn")
        print("2. 🛒 Quản lý hóa đơn/giỏ hàng")
        print("3. 📊 Thống kê & báo cáo")
        print("4. 📅 Lập kế hoạch thực đơn")
        print("5. 👥 Quản lý người dùng")
        print("6. 📤 Xuất báo cáo")
        print("7. 💾 Sao lưu dữ liệu")
        print("8. 🔄 Khôi phục dữ liệu")
        print("9. ℹ️  Thông tin hệ thống")
        print("0. 🚪 Thoát")
        print("-"*50)
        
        try:
            chon = input("🎯 Chọn chức năng: ")
            if chon == "1":
                menu.menu_cli()
            elif chon == "2":
                bill.bill_cli()
            elif chon == "3":
                stats.stats_cli()
            elif chon == "4":
                planner.planner_cli()
            elif chon == "5":
                user.user_cli()
            elif chon == "6":
                export.export_cli()
            elif chon == "7":
                backup_data()
            elif chon == "8":
                restore_data()
            elif chon == "9":
                system_info()
            elif chon == "0":
                print("👋 Tạm biệt! Hẹn gặp lại!")
                break
            else:
                print("❌ Lựa chọn không hợp lệ!")
        except KeyboardInterrupt:
            print("\n👋 Tạm biệt! Hẹn gặp lại!")
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    # Tạo thư mục data nếu chưa có
    if not os.path.exists("data"):
        os.makedirs("data")
        print("📁 Đã tạo thư mục data")
    
    # Kiểm tra các file dữ liệu cần thiết
    required_files = ["menu_data.json", "user_data.json", "hoadon_data.json", 
                     "ke_hoach.json", "lich_su.json"]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join("data", file)):
            missing_files.append(file)
    
    if missing_files:
        print(f"⚠️  Thiếu các file dữ liệu: {', '.join(missing_files)}")
        print("📝 Vui lòng tạo các file này hoặc chạy lại chương trình")
    
    main_menu() 