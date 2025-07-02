#!
#* Thống kê
import json
import os
from collections import Counter
from modules.menu import load_menu
from modules.bill import load_hoadon
import matplotlib.pyplot as plt
from datetime import datetime

def thong_ke_doanh_thu():
    hoadon_list = load_hoadon()
    doanh_thu = sum(hd.tong_tien for hd in hoadon_list)
    print(f"Tổng doanh thu: {doanh_thu}")

def thong_ke_mon_pho_bien():
    hoadon_list = load_hoadon()
    all_items = []
    for hd in hoadon_list:
        for item in hd.items:
            all_items.extend([item['ten']] * item['so_luong'])
    counter = Counter(all_items)
    print("Món phổ biến:")
    for ten, sl in counter.most_common(5):
        print(f"{ten}: {sl} lần")

def thong_ke_calo_chiphi():
    hoadon_list = load_hoadon()
    menu_list = load_menu()
    calo_ngay = {}
    chiphi_ngay = {}
    for hd in hoadon_list:
        calo = 0
        for item in hd.items:
            mon = next((m for m in menu_list if m.id == item['id']), None)
            if mon:
                calo += mon.calo * item['so_luong']
        calo_ngay[hd.ngay] = calo_ngay.get(hd.ngay, 0) + calo
        chiphi_ngay[hd.ngay] = chiphi_ngay.get(hd.ngay, 0) + hd.tong_tien
    print("Calo/ngày:", calo_ngay)
    print("Chi phí/ngày:", chiphi_ngay)
    # Vẽ biểu đồ
    if calo_ngay:
        plt.figure(figsize=(10,5))
        plt.bar(calo_ngay.keys(), calo_ngay.values())
        plt.title('Calo theo ngày')
        plt.ylabel('Calo')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    if chiphi_ngay:
        plt.figure(figsize=(10,5))
        plt.bar(chiphi_ngay.keys(), chiphi_ngay.values())
        plt.title('Chi phí theo ngày')
        plt.ylabel('VNĐ')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def stats_cli():
    while True:
        print("\n--- THỐNG KÊ & BÁO CÁO ---")
        print("1. Thống kê doanh thu")
        print("2. Món phổ biến")
        print("3. Thống kê calo/chi phí và vẽ biểu đồ")
        print("0. Quay lại")
        chon = input("Chọn: ")
        if chon == "1":
            thong_ke_doanh_thu()
        elif chon == "2":
            thong_ke_mon_pho_bien()
        elif chon == "3":
            thong_ke_calo_chiphi()
        elif chon == "0":
            break
        else:
            print("Không hợp lệ!") 