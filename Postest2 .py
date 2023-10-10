import os, time
from prettytable import PrettyTable

#List Barang Toko menggunakan PrettyTable
lining = PrettyTable()
lining.field_names = ["Item Code","Tipe Raket","Harga Raket"]
lining.add_row(["Ln121", "Li-Ning Windstorm 72", "530000"])
lining.add_row(["Ln122", "Li-Ning Calibar 300", "430000"])
lining.add_row(["Ln123", "Li-Ning XP Series", "470000"])
lining.add_row(["Ln124", "Li-Ning Superlite Max", "350000"])


yonex = PrettyTable()
yonex.field_names = ["Item Code", "Tipe Raket", "Harga Raket"]
yonex.add_row(["Yn121", "Yonex ArcSaber", "470000"])
yonex.add_row(["Yn122", "Yonex Nano Ray", "420000"])
yonex.add_row(["Yn123", "Yonex Carbonex 800N", "350000"])
yonex.add_row(["Yn124", "Yonex Doura Z-Strike", "550000"])

adidas = PrettyTable()
adidas.field_names = ["Item Code", "Tipe Raket", "Harga Jam"]
adidas.add_row(["Ads121", "Adidas Spieler E05", "730000"])
adidas.add_row(["Ads122", "Adidas Spieler P Aktiv", "650000"])
adidas.add_row(["Ads123", "Adidas Spieler P90", "550000"])
adidas.add_row(["Ads124", "Adidas Spieler E-Stark", "850000"])

saldo = 5000000

#Fungsi untuk memilih opsi menu khusus Admin
def admin():
    while True:
        print("=" * 50)
        print(" " * 20, "PILIH MENU ADMIN :")
        print("=" * 50)
        print("1. Lihat Stok Raket")
        print("2. Tambah Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("Pilih menu admin: ")

        if  pilihan == "1":
            print("Li-Ning")
            print(lining)
            print("Yonex")
            print(yonex)
            print("Adidas")
            print(adidas)
        elif pilihan == "2":
            tambah_data()
        elif pilihan == "3":
            hapus_data()
        elif pilihan == "4":
            ubah_data()
        elif pilihan == "5":
            break
        else :
            print("Menu Tidak Valid! Masukkan Menu Dengan Benar!")

#Fungsi Untuk Menambahkan Data ke Toko (Admin)
def tambah_data():
    print("Pilih Merk:")
    print("1. Li-Ning")
    print("2. Yonex")
    print("3. Adidas")
    nomor_merk = input("Masukkan nomor merk: ")

    if nomor_merk == "1":
        merk = "Li-Ning"
        tabel = lining
    elif nomor_merk == "2":
        merk = "Yonex"
        tabel = yonex
    elif nomor_merk == "3":
        merk = "Adidas"
        tabel = adidas
    else:
        print("Merk tidak valid!")
        return

    item_code = input("Masukkan Item Code: ")
    tipe_raket = input("Masukkan Jenis Raket: ")
    harga_raket = input("Masukkan Harga Raket: ")

    if merk == "Li-Ning":
        tabel.add_row([item_code, tipe_raket, harga_raket])
    elif merk == "Yonex":
        tabel.add_row([item_code, tipe_raket, harga_raket])
    elif merk == "Adidas":
        tabel.add_row([item_code, tipe_raket, harga_raket])
    else:
        print("Merk tidak valid!")
        

#Fungsi Menghapus Data Toko (Admin)
def hapus_data():
    print("Pilih Merk:")
    print("1. Li-Ning")
    print("2. Yonex")
    print("3. Adidas")
    nomor_merk = input("Masukkan nomor merk: ")

    if nomor_merk == "1":
        merk = "Li-Ning"
        tabel = lining
    elif nomor_merk == "2":
        merk = "Yonex"
        tabel = yonex
    elif nomor_merk == "3":
        merk = "Adidas"
        tabel = adidas
    else:
        print("Merk tidak valid!")
        return

    item_code = input("Masukkan Item Code yang akan dihapus: ")

    try:
        index = [row[0] for row in tabel._rows].index(item_code)
        tabel.del_row(index)
        print(f"Data dengan Item Code {item_code} pada merk {merk} berhasil dihapus.")
    except ValueError:
        print(f"Data dengan Item Code {item_code} pada merk {merk} tidak ditemukan.")

#Fungsi merubah Data Toko (Admin)
def ubah_data():
    print("Pilih Merk:")
    print("1. Li-Ning")
    print("2. Yonex")
    print("3. Adidas")
    merk_option = input("Masukkan nomor merk: ")

    if merk_option == "1":
        merk = "Li-Ning"
        tabel = lining
    elif merk_option == "2":
        merk = "Yonex"
        tabel = yonex
    elif merk_option == "3":
        merk = "Adidas"
        tabel = adidas
    else:
        print("Merk tidak valid!")
        return

    item_code = input("Masukkan Item Code yang akan diubah: ")

    if merk == "Li-Ning":
        try:
            index = [row[0] for row in tabel._rows].index(item_code)
            tipe_raket = input("Masukkan Tipe Baru: ")
            harga_raket = input("Masukkan Harga Baru: ")

            # Menghapus Baris Data Lama yang di pilih
            tabel.del_row(index)

            # Tambahkan Baris Data Baru yang di Input Admin
            tabel.add_row([item_code, tipe_raket, harga_raket])
            print(f"Data dengan Item Code {item_code} berhasil diubah.")
        except ValueError:
            print(f"Data dengan Item Code {item_code} tidak ditemukan.")
    elif merk == "Yonex":
        try:
            index = [row[0] for row in tabel._rows].index(item_code)
            tipe_raket = input("Masukkan Tipe Baru: ")
            harga_raket = input("Masukkan Harga Baru: ")

            # Menghapus Data Baris Lama yang di pilih
            tabel.del_row(index)

            # Tambahkan Baris Data Baru yang di Input Admin
            tabel.add_row([item_code, tipe_raket, harga_raket])
            print(f"Data dengan Item Code {item_code} berhasil diubah.")
        except ValueError:
            print(f"Data dengan Item Code {item_code} tidak ditemukan.")
    elif merk == "Adidas":
        try:
            index = [row[0] for row in tabel._rows].index(item_code)
            tipe_raket = input("Masukkan Tipe Raket Baru: ")
            harga_raket = input("Masukkan Harga Baru: ")

            # Menghapus Data Baris Lama yang di pilih
            tabel.del_row(index)

            # Tambahkan Baris Data Baru yang di Input Admin
            tabel.add_row([item_code, tipe_raket, harga_raket])
            print(f"Data dengan Item Code {item_code} berhasil diubah.")
        except ValueError:
            print(f"Data dengan Item Code {item_code} tidak ditemukan.")
    else:
        print("Merk tidak valid! Masukkan Data Merk Yang Benar!")


#Fungsi Login dengan Memilih Menu Terlebih Dahulu
def login():
    while True:
        print("=" * 95)
        print(" " * 30, "SELAMAT DATANG DI ")
        print(" " * 27, "DI TOKO RAKET BADMINTON")
        print("=" * 95)
        print("Menu Login Pilihan :")  #
        print("1. Admin")
        print("2. Pembeli")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            admin()
            print()
        elif pilihan == "2":
            pembeli()
            print()


#Fungsi Sebagai Menu Pilihan Pembeli

def pembeli():
    global saldo
    print("="*50)
    print(" " * 20, "PILIH MENU PEMBELI :")
    print("="*50)
    print("""
    1. Belanja
    2. Cek saldo
    3. Top up saldo
    """)
    print("="*50)
    print("")
    pilih = input("Pilih menu: ")
    if pilih == "1":
        print("Li-Ning")
        print("Yonex")
        print("Adidas")
        merk = input("Pilih Merk :")
        if merk == "Li-Ning":
            print("Raket Li-Ning")
            print(lining)
        elif merk == "Yonex":
            print("Raket Yonex")
            print(yonex)
        elif merk == "Adidas":
            print("Raket Adidas")
            print(adidas)
        else:
            print("Merk tidak valid.")
            return

        belanja = input("Pilih item code: ")
        kuantitas = int(input("Jumlah pembelian: "))


        # Menampilkan harga raket berdasarkan item code yang dipilih
        if merk == "Li-Ning":
            harga_peritem = {row[0]: int(row[2]) for row in lining._rows}
        elif merk == "Yonex":
            harga_peritem = {row[0]: int(row[2]) for row in yonex._rows}
        elif merk == "Adidas":
            harga_peritem = {row[0]: int(row[2]) for row in adidas._rows}
        else:
            harga_peritem = {}

        if belanja not in harga_peritem:
            print("Item code tidak valid.")
        else:
            harga = harga_peritem[belanja]
            totalharga = harga * kuantitas

        tanya = input("Ingin membeli raket? (ya/tidak): ")
        if tanya == "ya":
            print ("Total Bayar :", totalharga)
        elif tanya == "tidak":
            print (pembeli)
        time.sleep(1.0)
        if saldo >= totalharga:
            saldo -= totalharga
            print(f"Pembelian berhasil. Saldo Anda sekarang: {saldo}")
        else:
            print("Saldo tidak mencukupi untuk pembelian ini.")
            
#Menampilkan Jumlah Saldo Sebelum dan Sesudah di Top Up
    elif pilih == "2":
        print("Saldo anda :", saldo)
    elif pilih == "3":
        topup = int(input("Masukkan nominal top up : "))
        saldo = (saldo+topup)
        print("Jumlah Saldo anda sekarang adalah : ", saldo)
    else:
        print("Menu tidak valid.")

if __name__ == "__main__":
    login()