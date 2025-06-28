import json
import os
from typing import List, Dict

DATA_FILE = "data/menu_data.json"

class MonAn:
    def __init__(self, id, ten, loai, gia, calo, che_do_an, nguyen_lieu, mo_ta):
        self.id = id
        self.ten = ten
        self.loai = loai
        self.gia = gia
        self.calo = calo
        self.che_do_an = che_do_an  # list
        self.nguyen_lieu = nguyen_lieu  # list
        self.mo_ta = mo_ta

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(d):
        return MonAn(
            d['id'], d['ten'], d['loai'], d['gia'], d['calo'],
            d.get('che_do_an', []), d.get('nguyen_lieu', []), d.get('mo_ta', "")
        )

def load_menu() -> List[MonAn]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [MonAn.from_dict(item) for item in data]
    return []

def save_menu(menu_list: List[MonAn]):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump([m.to_dict() for m in menu_list], f, ensure_ascii=False, indent=4)

def them_mon_an():
    menu_list = load_menu()
    print("\n🍽️  THÊM MÓN ĂN MỚI")
    print("-" * 30)
    
    id = input("📝 ID món: ")
    # Kiểm tra ID đã tồn tại
    if any(m.id == id for m in menu_list):
        print("❌ ID món đã tồn tại!")
        return
    
    ten = input("🍴 Tên món: ")
    loai = input("📂 Loại món (chính/phụ/nước/tráng miệng): ")
    
    try:
        gia = float(input("💰 Giá (VNĐ): "))
        calo = float(input("🔥 Calo: "))
    except ValueError:
        print("❌ Giá và calo phải là số!")
        return
    
    che_do_an = input("🥗 Chế độ ăn (cách nhau dấu phẩy): ").split(',')
    nguyen_lieu = input("🥬 Nguyên liệu (cách nhau dấu phẩy): ").split(',')
    mo_ta = input("📝 Mô tả: ")
    
    mon = MonAn(id, ten, loai, gia, calo, [c.strip() for c in che_do_an], [n.strip() for n in nguyen_lieu], mo_ta)
    menu_list.append(mon)
    save_menu(menu_list)
    print("✅ Đã thêm món thành công!")

def sua_mon_an():
    menu_list = load_menu()
    print("\n✏️  SỬA MÓN ĂN")
    print("-" * 30)
    
    id = input("🔍 Nhập ID món cần sửa: ")
    for mon in menu_list:
        if mon.id == id:
            print(f"📝 Sửa món: {mon.ten}")
            print("-" * 20)
            
            mon.ten = input(f"🍴 Tên mới ({mon.ten}): ") or mon.ten
            mon.loai = input(f"📂 Loại mới ({mon.loai}): ") or mon.loai
            
            try:
                gia_input = input(f"💰 Giá mới ({mon.gia}): ")
                if gia_input:
                    mon.gia = float(gia_input)
                
                calo_input = input(f"🔥 Calo mới ({mon.calo}): ")
                if calo_input:
                    mon.calo = float(calo_input)
            except ValueError:
                print("❌ Giá và calo phải là số!")
                return
            
            che_do = input(f"🥗 Chế độ ăn mới ({','.join(mon.che_do_an)}): ")
            if che_do:
                mon.che_do_an = [c.strip() for c in che_do.split(',')]
            
            ngl = input(f"🥬 Nguyên liệu mới ({','.join(mon.nguyen_lieu)}): ")
            if ngl:
                mon.nguyen_lieu = [n.strip() for n in ngl.split(',')]
            
            mon.mo_ta = input(f"📝 Mô tả mới ({mon.mo_ta}): ") or mon.mo_ta
            
            save_menu(menu_list)
            print("✅ Đã cập nhật thành công!")
            return
    print("❌ Không tìm thấy món!")

def xoa_mon_an():
    menu_list = load_menu()
    print("\n🗑️  XÓA MÓN ĂN")
    print("-" * 30)
    
    id = input("🔍 Nhập ID món cần xóa: ")
    for mon in menu_list:
        if mon.id == id:
            print(f"⚠️  Bạn có chắc muốn xóa món: {mon.ten}?")
            confirm = input("Nhập 'yes' để xác nhận: ")
            if confirm.lower() == 'yes':
                menu_list = [m for m in menu_list if m.id != id]
                save_menu(menu_list)
                print("✅ Đã xóa thành công!")
            else:
                print("❌ Đã hủy xóa!")
            return
    print("❌ Không tìm thấy món!")

def tim_kiem_mon_an():
    menu_list = load_menu()
    print("\n🔍 TÌM KIẾM MÓN ĂN")
    print("-" * 30)
    print("1. 🔤 Tìm theo tên")
    print("2. 📂 Tìm theo loại")
    print("3. 🥗 Tìm theo chế độ ăn")
    print("4. 🔥 Tìm theo calo (≤)")
    print("5. 💰 Tìm theo giá (≤)")
    print("6. 🥬 Tìm theo nguyên liệu")
    
    chon = input("🎯 Chọn cách tìm: ")
    
    if chon == "1":
        kw = input("🔤 Nhập tên món: ").lower()
        kq = [m for m in menu_list if kw in m.ten.lower()]
    elif chon == "2":
        loai = input("📂 Nhập loại: ").lower()
        kq = [m for m in menu_list if loai in m.loai.lower()]
    elif chon == "3":
        cd = input("🥗 Nhập chế độ: ").lower()
        kq = [m for m in menu_list if cd in [c.lower() for c in m.che_do_an]]
    elif chon == "4":
        try:
            val = float(input("🔥 Nhập calo tối đa: "))
            kq = [m for m in menu_list if m.calo <= val]
        except ValueError:
            print("❌ Calo phải là số!")
            return
    elif chon == "5":
        try:
            val = float(input("💰 Nhập giá tối đa: "))
            kq = [m for m in menu_list if m.gia <= val]
        except ValueError:
            print("❌ Giá phải là số!")
            return
    elif chon == "6":
        ngl = input("🥬 Nhập nguyên liệu: ").lower()
        kq = [m for m in menu_list if any(ngl in n.lower() for n in m.nguyen_lieu)]
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    
    if kq:
        print(f"\n📋 Tìm thấy {len(kq)} món:")
        print("-" * 80)
        for m in kq:
            print(f"🆔 {m.id} | 🍴 {m.ten} | 📂 {m.loai} | 💰 {m.gia:,}đ | 🔥 {m.calo}cal")
            print(f"   🥗 {', '.join(m.che_do_an)} | 🥬 {', '.join(m.nguyen_lieu)}")
            print(f"   📝 {m.mo_ta}")
            print("-" * 80)
    else:
        print("❌ Không tìm thấy món nào!")

def goi_y_mon_an():
    menu_list = load_menu()
    print("\n💡 GỢI Ý MÓN ĂN")
    print("-" * 30)
    print("1. 🎯 Theo mục tiêu sức khỏe")
    print("2. 🌅 Theo buổi ăn")
    print("3. 🔥 Theo lượng calo")
    
    chon = input("🎯 Chọn loại gợi ý: ")
    
    if chon == "1":
        print("🎯 Mục tiêu: 1.Ăn chay 2.Giảm cân 3.Tăng cơ")
        muc_tieu = input("Chọn mục tiêu: ")
        if muc_tieu == "1":
            kq = [m for m in menu_list if "ăn chay" in [c.lower() for c in m.che_do_an]]
        elif muc_tieu == "2":
            kq = [m for m in menu_list if "giảm cân" in [c.lower() for c in m.che_do_an]]
        elif muc_tieu == "3":
            kq = [m for m in menu_list if "tăng cơ" in [c.lower() for c in m.che_do_an]]
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return
    
    elif chon == "2":
        print("🌅 Buổi ăn: 1.Sáng 2.Trưa 3.Tối")
        buoi = input("Chọn buổi: ")
        if buoi == "1":  # Sáng - nhẹ, ít calo
            kq = [m for m in menu_list if m.calo <= 300 and m.loai in ["nước uống", "món phụ"]]
        elif buoi == "2":  # Trưa - chính, nhiều calo
            kq = [m for m in menu_list if m.loai == "món chính"]
        elif buoi == "3":  # Tối - vừa phải
            kq = [m for m in menu_list if 200 <= m.calo <= 500]
        else:
            print("❌ Lựa chọn không hợp lệ!")
            return
    
    elif chon == "3":
        try:
            calo_min = float(input("🔥 Calo tối thiểu: "))
            calo_max = float(input("🔥 Calo tối đa: "))
            kq = [m for m in menu_list if calo_min <= m.calo <= calo_max]
        except ValueError:
            print("❌ Calo phải là số!")
            return
    
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    
    if kq:
        print(f"\n💡 Gợi ý {len(kq)} món:")
        print("-" * 80)
        for m in kq:
            print(f"🆔 {m.id} | 🍴 {m.ten} | 💰 {m.gia:,}đ | 🔥 {m.calo}cal")
            print(f"   📝 {m.mo_ta}")
            print("-" * 80)
    else:
        print("❌ Không có món phù hợp!")

def hien_thi_thuc_don():
    menu_list = load_menu()
    print("\n📋 HIỂN THỊ THỰC ĐƠN")
    print("-" * 30)
    print("1. 📂 Lọc theo loại")
    print("2. 🥗 Lọc theo chế độ ăn")
    print("3. 📋 Hiển thị tất cả")
    
    chon = input("🎯 Chọn cách hiển thị: ")
    
    if chon == "1":
        loai = input("📂 Nhập loại: ").lower()
        kq = [m for m in menu_list if loai in m.loai.lower()]
    elif chon == "2":
        cd = input("🥗 Nhập chế độ: ").lower()
        kq = [m for m in menu_list if cd in [c.lower() for c in m.che_do_an]]
    elif chon == "3":
        kq = menu_list
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    
    if kq:
        print(f"\n📋 Thực đơn ({len(kq)} món):")
        print("=" * 100)
        for m in kq:
            print(f"🆔 {m.id} | 🍴 {m.ten:<20} | 📂 {m.loai:<10} | 💰 {m.gia:>8,}đ | 🔥 {m.calo:>4}cal")
            print(f"   🥗 {', '.join(m.che_do_an)}")
            print(f"   🥬 {', '.join(m.nguyen_lieu)}")
            print(f"   📝 {m.mo_ta}")
            print("-" * 100)
    else:
        print("❌ Không có món nào!")

def menu_cli():
    while True:
        print("\n" + "="*50)
        print("🍽️  QUẢN LÝ MÓN ĂN")
        print("="*50)
        print("1. ➕ Thêm món ăn")
        print("2. ✏️  Sửa món ăn")
        print("3. 🗑️  Xóa món ăn")
        print("4. 🔍 Tìm kiếm món ăn")
        print("5. 💡 Gợi ý món ăn")
        print("6. 📋 Hiển thị thực đơn")
        print("0. 🔙 Quay lại")
        print("-"*50)
        
        try:
            chon = input("🎯 Chọn chức năng: ")
            if chon == "1":
                them_mon_an()
            elif chon == "2":
                sua_mon_an()
            elif chon == "3":
                xoa_mon_an()
            elif chon == "4":
                tim_kiem_mon_an()
            elif chon == "5":
                goi_y_mon_an()
            elif chon == "6":
                hien_thi_thuc_don()
            elif chon == "0":
                break
            else:
                print("❌ Lựa chọn không hợp lệ!")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Lỗi: {e}") 