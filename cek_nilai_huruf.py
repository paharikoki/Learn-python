#cek nilai huruf

def cek_nilai(nilai):
    if not nilai.isdigit():
        print("Nilai harus berupa angka!")
    elif int(nilai) > 100:
        print("Nilai tidak boleh lebih dari 100!")
    else:
        nilai = int(nilai)
        if nilai > 80:
            print("Nilai anda: Baik Sekali")
        elif nilai >= 65:
            print("Nilai anda: Baik")
        elif nilai >= 55:
            print("Nilai anda: Cukup")
        elif nilai >= 40:
            print("Nilai anda: Kurang")
        else:
            print("Nilai anda: Kurang Sekali")
cek_nilai(input("Masukkan nilai: "))
while True:
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        cek_nilai(input("\nMasukkan nilai: "))
    else:
        print("Pilihan tidak valid!, Silakan masukkan (y/n) ")