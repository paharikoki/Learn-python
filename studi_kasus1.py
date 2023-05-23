# Hitung nilai total transaksi pembelian Printer Epson T20:
# 1. Terdapat inputan untuk mengisi banyaknya pembelian
# 2. Harga 1 printer Rp 660.000.
harga = 660000
diskon = 0.15
def hitung_total(jumlah):
    if not jumlah.isdigit():
        print("Total Pembelian harus berupa angka!")
    else:
        jumlah = int(jumlah)
        total_pembayaran =jumlah * harga
        # jika total_pembayaran lebih dari 15000000 maka mendapatkan diskon
        if total_pembayaran >= 1500000 :
            print(f"Pembelian {jumlah} Unit Printer Epson T20")
            print(f"Total Transaksi : {total_pembayaran}")
            total_diskon = total_pembayaran * diskon
            total_pembayaran -=total_diskon
            print(f"Selamat anda mendapatkan diskon sebesar {total_diskon}")
            print(f"Silakan Bayar dengan total : {total_pembayaran}")
        else:
            print(f"Pembelian {jumlah} Unit Printer Epson T20")
            print(f"Total Transaksi : {total_pembayaran}")

hitung_total(input("Masukkan Jumlah Unit: "))
while True:
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        hitung_total(input("\nMasukkan Jumlah Unit: "))
    else:
        print("Pilihan tidak valid!, Silakan masukkan (y/n) ")