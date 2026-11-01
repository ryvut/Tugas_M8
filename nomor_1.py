# Nomor 1
daftar_nilai = [80, 75, 90, 65]
for skor in daftar_nilai:
    skor_baru = skor + 5
    print(f"Selamat nilai anda bertambah sebanyak {skor_baru}")

print("-" * 40)

# Nomor 2
for angka in range(3, 31, 3):
    print(angka, end=" ")
print()

print("-" * 40)

# Nomor 3
kalimat = "STATISTIKA BISNIS"
for huruf in kalimat.lower():
    print(huruf)

print("-" * 40)

# Nomor 4
daftar_peserta = ["Ijul", "Chlea", "Reza", "Citra", "Budi"]
for nama_peserta in daftar_peserta:
    if nama_peserta == "Reza": 
        continue
    print(nama_peserta)

print("-" * 40)

# Nomor 5
prodi_list = ["Statbis", "Statistika", "Matematika"]
tahun_angkatan = [2025, 2026]
for prodi in prodi_list:
    for tahun in tahun_angkatan:
        print(f" Departemen : {prodi}, Angkatan : {tahun}")

print("-" * 40)

# Nomor 6
daftar_pelamar = [("Budi", 3.2, 5), ("Siti", 3.6, 3), ("Dodi", 3.8, 1)]
for nama, ipk, pengalaman in daftar_pelamar:
    if ipk >= 3.5 and pengalaman > 2:
        print(f"Selamat anda diterima {nama}")
    else:
        print(f"Anda ditolak {nama}")

print("-" * 40)

# Nomor 7
daftar_karyawan = [("Joko", "IT", 7000), ("Rina", "HR", 5000), ("Toni", "Data", 8000), ("Lia", "IT", 6500)]
total_gaji_gabungan = 0

for nama, divisi, gaji in daftar_karyawan:
    if divisi in ("IT", "Data"):
        total_gaji_gabungan += gaji

print(f"Total gaji karyawan IT dan Data adalah ${total_gaji_gabungan:,.2f}")

print("-" * 40)

# Soal baru
for baris in range(1, 5):
    for kolom in range(1, 5):
        print("*", end=" ")
    print("*")

print("-" * 40)

# Nomor 8
data_penjualan = [("Kopi", 60, False), ("Teh", 30, False), ("Boba", 80, True)]
ambang_batas = 50

for item, terjual, sedang_promo in data_penjualan:
    if terjual > ambang_batas and not sedang_promo:
        print(f"Selamat produk {item} laku keras dengan jumlah minuman sebanyak {terjual}")
    elif sedang_promo and terjual > ambang_batas:
        print(f"Maaf produk {item}, belum laris tanpa adanya promo, silakan jual lagi!")
    else:
        print(f"Produk {item} masih belum laris, silakan buat inovasi lagi!")