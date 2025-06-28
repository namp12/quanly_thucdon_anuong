import json
import os
from datetime import datetime
from modules.menu import load_menu

DATA_FILE = "data/hoadon_data.json"

class HoaDon:
    def __init__(self, id, user_id, items, tong_tien, ngay):
        self.id = id
        self.user_id = user_id
        self.items = items  # list of dict: {id, ten, so_luong, gia}
        self.tong_tien = tong_tien
        self.ngay = ngay

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return HoaDon(d['id'], d['user_id'], d['items'], d['tong_tien'], d['ngay'])

def load_hoadon():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [HoaDon.from_dict(item) for item in data]
    return []

def save_hoadon(hoadon_list):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump([h.to_dict() for h in hoadon_list], f, ensure_ascii=False, indent=4)

def tao_hoadon():
    menu_list = load_menu()
    items = []
    tong_tien = 0
    while True:
        id_mon = input("Nhập ID món (0 để kết thúc): ")
        if id_mon == "0":
            break
        so_luong = int(input("Số lượng: "))
        mon = next((m for m in menu_list if m.id == id_mon), None)
        if mon:
            items.append({"id": mon.id, "ten": mon.ten, "so_luong": so_luong, "gia": mon.gia})
            tong_tien += mon.gia * so_luong
        else:
            print("Không tìm thấy món!")
    if items:
        user_id = input("Nhập ID người dùng: ")
        hd = HoaDon(
            id=str(int(datetime.now().timestamp())),
            user_id=user_id,
            items=items,
            tong_tien=tong_tien,
            ngay=datetime.now().strftime("%Y-%m-%d")
        )
        hoadon_list = load_hoadon()
        hoadon_list.append(hd)
        save_hoadon(hoadon_list)
        print(f"Tạo hóa đơn thành công! Tổng tiền: {tong_tien}")
    else:
        print("Chưa chọn món nào!")

def hien_thi_hoadon():
    hoadon_list = load_hoadon()
    for hd in hoadon_list:
        print(f"\nHóa đơn ID: {hd.id} | Người dùng: {hd.user_id} | Ngày: {hd.ngay}")
        for item in hd.items:
            print(f"  {item['ten']} x{item['so_luong']} - {item['gia']} đ")
        print(f"Tổng tiền: {hd.tong_tien}")

def bill_cli():
    while True:
        print("\n--- QUẢN LÝ HÓA ĐƠN/GIỎ HÀNG ---")
        print("1. Tạo hóa đơn mới")
        print("2. Hiển thị hóa đơn")
        print("0. Quay lại")
        chon = input("Chọn: ")
        if chon == "1":
            tao_hoadon()
        elif chon == "2":
            hien_thi_hoadon()
        elif chon == "0":
            break
        else:
            print("Không hợp lệ!") 