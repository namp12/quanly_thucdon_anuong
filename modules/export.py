#!
#* Xuất Excel, PDF, Email
import os
import json
from modules.bill import load_hoadon
from modules.menu import load_menu
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def xuat_hoadon_pdf():
    hoadon_list = load_hoadon()
    if not hoadon_list:
        print("Không có hóa đơn!")
        return
    id_hd = input("Nhập ID hóa đơn: ")
    hd = next((h for h in hoadon_list if h.id == id_hd), None)
    if not hd:
        print("Không tìm thấy hóa đơn!")
        return
    pdf_path = f"hoadon_{hd.id}.pdf"
    c = canvas.Canvas(pdf_path)
    c.drawString(100, 800, f"HÓA ĐƠN ID: {hd.id}")
    c.drawString(100, 780, f"Ngày: {hd.ngay}")
    y = 760
    for item in hd.items:
        c.drawString(120, y, f"{item['ten']} x{item['so_luong']} - {item['gia']} đ")
        y -= 20
    c.drawString(100, y-20, f"Tổng tiền: {hd.tong_tien}")
    c.save()
    print(f"Đã xuất PDF: {pdf_path}")

def xuat_menu_excel():
    menu_list = load_menu()
    wb = Workbook()
    ws = wb.active
    ws.title = "Menu"
    ws.append(["ID", "Tên", "Loại", "Giá", "Calo", "Chế độ ăn", "Nguyên liệu", "Mô tả"])
    for m in menu_list:
        ws.append([m.id, m.ten, m.loai, m.gia, m.calo, ','.join(m.che_do_an), ','.join(m.nguyen_lieu), m.mo_ta])
    file_path = "menu_data.xlsx"
    wb.save(file_path)
    print(f"Đã xuất Excel: {file_path}")

def gui_email():
    file_path = input("Nhập đường dẫn file cần gửi: ")
    email = input("Nhập email nhận: ")
    subject = input("Tiêu đề: ")
    body = input("Nội dung: ")
    sender = input("Email gửi: ")
    password = input("Mật khẩu ứng dụng: ")
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    with open(file_path, 'rb') as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(file_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        msg.attach(part)
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print("Đã gửi email!")
    except Exception as e:
        print(f"Lỗi gửi email: {e}")

def export_cli():
    while True:
        print("\n--- XUẤT BÁO CÁO ---")
        print("1. Xuất hóa đơn ra PDF")
        print("2. Xuất thực đơn ra Excel")
        print("3. Gửi file qua Email")
        print("0. Quay lại")
        chon = input("Chọn: ")
        if chon == "1":
            xuat_hoadon_pdf()
        elif chon == "2":
            xuat_menu_excel()
        elif chon == "3":
            gui_email()
        elif chon == "0":
            break
        else:
            print("Không hợp lệ!") 