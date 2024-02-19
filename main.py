chuoi = "xin chao xin chao ban xin"
so_lan_xuat_hien = {}

for tu in chuoi.split():
    if tu in so_lan_xuat_hien:
        so_lan_xuat_hien[tu] += 1
    else:
        so_lan_xuat_hien[tu] = 1

print(so_lan_xuat_hien)