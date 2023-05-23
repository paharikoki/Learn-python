#cek tingkat usia
# jika umur 60 tahun ke atas maka statusnya Lansia
# jika umur di antara 35 DAN 59 maka statusnya Dewasa
# jika umur di antara 18 DAN 34 maka statusnya Pemuda
# jika umur di antara 15 DAN 17 maka statusnya Remaja

def cek_usia(usia):
    if not usia.isdigit():
        print("Usia harus berupa angka!")
    else:
        usia = int(usia)
        if usia > 60:
            print("Status anda: Lansia")
        elif usia >=35:
            print("Status anda: Dewasa")
        elif usia >= 18:
            print("Status anda: Pemuda")
        elif usia >= 15:
            print("Status anda: Remaja")
        else:
            print("Status anda: Anak-anak")
cek_usia(input("Masukkan usia: "))
while True:
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        cek_usia(input("\nMasukkan usia: "))
    else:
        print("Pilihan tidak valid!, Silakan masukkan (y/n) ")
