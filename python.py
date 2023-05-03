
import pandas as pd
import numpy as np
import os

# Yêu cầu người dùng nhập đường dẫn đến file Excel
excel_path = input("Nhập đường dẫn đến file Excel: ")

# Sử dụng chuỗi nối để tạo ra đường dẫn đầy đủ đến file Excel
sogd = "sogd.xlsx"
bachoc = "bachoc.xlsx"
loaihinh = "loaihinh.xlsx"
loaitruong = "loaitruong.xlsx"
phonggd = "phonggd.xlsx"
gdtx_excel = "gdtx.xlsx"
mamnon_excel = "mamnon.xlsx"
tieuhoc_excel = "tieuhoc.xlsx"
thcs_excel = "thcs.xlsx"
thpt_excel = "thpt.xlsx"
sogd_full = os.path.join(excel_path, sogd)
bachoc_full = os.path.join(excel_path, bachoc)
loaihinh_full = os.path.join(excel_path, loaihinh)
loaitruong_full = os.path.join(excel_path, loaitruong)
phonggd_full = os.path.join(excel_path, phonggd)
gdtx_full = os.path.join(excel_path, gdtx_excel)
mamnon_full = os.path.join(excel_path, mamnon_excel)
tieuhoc_full = os.path.join(excel_path, tieuhoc_excel)
thcs_full = os.path.join(excel_path, thcs_excel)
thpt_full = os.path.join(excel_path, thpt_excel)



# Sử dụng pd.read_excel() để đọc file Excel và trả về DataFrame của pandas
thongtinsogd = pd.read_excel(sogd_full)
thongtincapbac = pd.read_excel(bachoc_full)
thongtinloaihinh = pd.read_excel(loaihinh_full)
thongtinloaitruong = pd.read_excel(loaitruong_full)
thongtinphonggd = pd.read_excel(phonggd_full)

gdtx = pd.read_excel(gdtx_full)
mamnon = pd.read_excel(mamnon_full)
tieuhoc = pd.read_excel(tieuhoc_full)
thcs = pd.read_excel(thcs_full)
thpt = pd.read_excel(thpt_full)


dcapbac = {}
dloaihinh = {}
dloaitruong = {}
dphonggd = {}




def xx(leng):
    ans = ''
    for i in range(leng):
        ans += 'X'
    return ans


def insert(a, f, table, leng, d):
    for index, row in a.iterrows():
        ma = str(row["ma" + table])
        ten = str(row[ "ten" + table])
        if (ten == 'nan'):
            ten = 'NULL'
            f.write('INSERT INTO {} VALUES ("{}", NULL);\n'.format(table, ma))
        else:
            f.write('INSERT INTO {} VALUES ("{}", "{}");\n'.format(table, ma, ten))
        d[ten] = ma


f = open('/Users/benjamin/Code/C++/DATABASE/doan1/data/sogd.sql', 'w', encoding='utf-8')
f.write('USE truonghoc;\n')
f.write("INSERT INTO sogd (stt, sogd) VALUES ('1', 'Sở Giáo Dục Và Đào Tạo TPHCM');")
f.close()


def thongtintruong():
    f = open('/Users/benjamin/Code/C++/DATABASE/doan1/data/thongtintruong.sql', 'w', encoding='utf-8')
    f.write('USE truonghoc;\n')
    insert(thongtincapbac, f, 'bachoc', 2, dcapbac)
    insert(thongtinloaitruong, f, 'loaitruong', 6, dloaitruong)
    insert(thongtinloaihinh, f, 'loaihinh', 5, dloaihinh)
    insert(thongtinphonggd, f, 'phonggd', 3, dphonggd)
    f.close()



def ins(arr, name, cap):
    with open('/Users/benjamin/Code/C++/DATABASE/doan1/data/' + name + '.sql', 'w', encoding='utf-8') as f:
        f.write('USE truonghoc;\n')
        for index, row in arr.iterrows():
            matruong = str(row['matruong'])

            tentruong = str(row['tentruong'])

            diachi = str(row['diachi'])
            if (diachi == 'nan'):
                diachi = 'Không có'

            phonggd = str(row['phonggd'])
            if (phonggd == 'nan'):
                phonggd = 'NULL'
            phonggd = dphonggd[phonggd]

            loaihinh = str(row['loaihinh'])
            if (loaihinh == 'nan'):
                loaihinh = 'NULL'
                dloaihinh[loaihinh] = 'NULL'

            loaihinh = dloaihinh[loaihinh]

            loaitruong = str(row['loaitruong'])
            if (loaitruong == 'nan'):
                loaitruong = 'NULL'
            loaitruong = dloaitruong[loaitruong]

            f.write(
                'INSERT INTO thongtintruong VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}");\n'.format(matruong, tentruong, diachi, phonggd, loaihinh, loaitruong, cap))
        f.close()

#ta tiếp tục thêm thông tin
thongtintruong()
ins(gdtx, 'gdtx', 'TX')
ins(mamnon, 'mamnon', 'MN')
ins(tieuhoc, 'tieuhoc', 'TH')
ins(thcs, 'thcs', 'CS')
ins(thpt, 'thpt', 'PT')