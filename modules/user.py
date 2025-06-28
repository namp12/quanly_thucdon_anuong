import json
import os

DATA_FILE = "data/user_data.json"

class User:
    def __init__(self, id, ten, tuoi, can_nang, muc_tieu, quyen):
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.can_nang = can_nang
        self.muc_tieu = muc_tieu
        self.quyen = quyen  # admin/nhanvien/khach

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return User(d['id'], d['ten'], d['tuoi'], d['can_nang'], d['muc_tieu'], d['quyen'])

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(item) for item in data]
    return []

def save_users(user_list):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump([u.to_dict() for u in user_list], f, ensure_ascii=False, indent=4)

def them_user():
    user_list = load_users()
    id = input("ID: ")
    ten = input("Tên: ")
    tuoi = int(input("Tuổi: "))
    can_nang = float(input("Cân nặng: "))
    muc_tieu = input("Mục tiêu (giảm cân/tăng cơ...): ")
    quyen = input("Quyền (admin/nhanvien/khach): ")
    user = User(id, ten, tuoi, can_nang, muc_tieu, quyen)
    user_list.append(user)
    save_users(user_list)
    print("Đã thêm user!")

def sua_user():
    user_list = load_users()
    id = input("Nhập ID user cần sửa: ")
    for u in user_list:
        if u.id == id:
            u.ten = input(f"Tên mới ({u.ten}): ") or u.ten
            u.tuoi = int(input(f"Tuổi mới ({u.tuoi}): ") or u.tuoi)
            u.can_nang = float(input(f"Cân nặng mới ({u.can_nang}): ") or u.can_nang)
            u.muc_tieu = input(f"Mục tiêu mới ({u.muc_tieu}): ") or u.muc_tieu
            u.quyen = input(f"Quyền mới ({u.quyen}): ") or u.quyen
            save_users(user_list)
            print("Đã cập nhật!")
            return
    print("Không tìm thấy user!")

def xoa_user():
    user_list = load_users()
    id = input("Nhập ID user cần xóa: ")
    user_list = [u for u in user_list if u.id != id]
    save_users(user_list)
    print("Đã xóa!")

def hien_thi_users():
    user_list = load_users()
    for u in user_list:
        print(f"{u.id} | {u.ten} | {u.tuoi} | {u.can_nang}kg | {u.muc_tieu} | {u.quyen}")

def user_cli():
    while True:
        print("\n--- QUẢN LÝ NGƯỜI DÙNG ---")
        print("1. Thêm user")
        print("2. Sửa user")
        print("3. Xóa user")
        print("4. Hiển thị danh sách user")
        print("0. Quay lại")
        chon = input("Chọn: ")
        if chon == "1":
            them_user()
        elif chon == "2":
            sua_user()
        elif chon == "3":
            xoa_user()
        elif chon == "4":
            hien_thi_users()
        elif chon == "0":
            break
        else:
            print("Không hợp lệ!") 