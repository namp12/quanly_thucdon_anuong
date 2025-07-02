#!
#* Lập kế hoạch thực đơn
import json
import os
from datetime import datetime
from modules.menu import load_menu

KE_HOACH_FILE = "data/ke_hoach.json"
LICH_SU_FILE = "data/lich_su.json"

def load_ke_hoach():
    if os.path.exists(KE_HOACH_FILE):
        with open(KE_HOACH_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_ke_hoach(data):
    with open(KE_HOACH_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_lich_su():
    if os.path.exists(LICH_SU_FILE):
        with open(LICH_SU_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_lich_su(data):
    with open(LICH_SU_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def lap_ke_hoach_tuan():
    menu_list = load_menu()
    ke_hoach = {}
    for day in ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]:
        print(f"\n{day}:")
        ids = input("Nhập ID món (cách nhau dấu phẩy): ").split(',')
        ke_hoach[day] = [id.strip() for id in ids if id.strip()]
    save_ke_hoach(ke_hoach)
    print("Đã lưu kế hoạch tuần!")

def luu_lich_su_ngay():
    menu_list = load_menu()
    lich_su = load_lich_su()
    today = datetime.now().strftime("%Y-%m-%d")
    ids = input("Nhập ID món đã ăn hôm nay (cách nhau dấu phẩy): ").split(',')
    lich_su[today] = [id.strip() for id in ids if id.strip()]
    save_lich_su(lich_su)
    print("Đã lưu lịch sử ngày!")

def planner_cli():
    while True:
        print("\n--- LẬP KẾ HOẠCH & LỊCH SỬ ---")
        print("1. Lập kế hoạch thực đơn tuần")
        print("2. Lưu lịch sử món ăn ngày")
        print("0. Quay lại")
        chon = input("Chọn: ")
        if chon == "1":
            lap_ke_hoach_tuan()
        elif chon == "2":
            luu_lich_su_ngay()
        elif chon == "0":
            break
        else:
            print("Không hợp lệ!") 