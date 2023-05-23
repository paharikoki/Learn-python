#Hitung nilai total dari pembelian monitor LCD LG dalam tipe yang disediakan:
# a. LG W15" Rp 1.050.000
# b. LG W16,5" Rp 1.150.000
# c. LG W17" Rp 1.250.000
# Syarat:
# 1. Terdapat inputan banyaknya pembelian
# 2. Jika lebih dari 3 unit tipe apapun diberikan diskon 25%
# 3. Dalam 1 transaksi Pembeli boleh membeli tipe yang berbeda-beda.
while True:
    print("Selamat datang di aplikasi hitung total transaksi pembelian Monitor LCD LG!")
    #Daftra Harga Monitor
    harga_monitor = {
        "LG W15": 1050000,
        "LG W16,5": 1150000,
        "LG W17": 1250000
    }

    #Tampilkan Pilihan Monitor
    print("Pilihan monitor:")
    for indeks, monitor in enumerate(harga_monitor, start=1):
        print(f"{indeks}. {monitor} : {harga_monitor[monitor]}")
    print("0. Keluar")
    #Input pilihan monitor berdasarkan index
    pilihan_monitor = input("Masukkan nomor pilihan monitor: ")
    if not pilihan_monitor.isdigit():
        print("Pilihan harus berupa angka!")
    elif pilihan_monitor == "0":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif int(pilihan_monitor) in range(1, len(harga_monitor)+1):
        pilihan_monitor = int(pilihan_monitor)
        if pilihan_monitor < 1 or pilihan_monitor > len(harga_monitor):
            print(f"Pilihan harus diantara 1 sampai {len(harga_monitor)}")
        else:
            # Input banyaknya monitor
            banyak_monitor = input("Masukkan banyaknya monitor: ")
            if not banyak_monitor.isdigit():
                print("Banyak monitor harus berupa angka!")
            else:
                banyak_monitor = int(banyak_monitor)
                if banyak_monitor < 1:
                    print("Banyak monitor harus lebih dari 0!")
                else:
                    # Hitung total harga
                    total_harga = harga_monitor[list(harga_monitor)[pilihan_monitor - 1]] * banyak_monitor
                    # Hitung diskon
                    if banyak_monitor > 3:
                        # Menampilkan diskon
                        print("Anda mendapatkan diskon 25%")
                        print(f"Total harga sebelum diskon: {total_harga}")
                        # Menampilkan total diskon
                        diskon = total_harga * 0.25
                        print(f"Diskon: {diskon}")
                        total_harga-= diskon
                    print(f"Total harga: {total_harga}")
                    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
                    if pilihan == "n" or pilihan == "no":
                        print("Terima kasih sudah menggunakan aplikasi ini.")
                        break
                    elif pilihan == "y" or pilihan == "yes":
                        continue
    else:
        print(f"Pilihan harus diantara 1 sampai {len(harga_monitor)}\n")
