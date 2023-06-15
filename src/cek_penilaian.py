#cek penilaian dengan huruf
while True:
    print("Selamat datang di aplikasi cek penilaian!")
    print("Masukkan nilai anda untuk mengetahui penilaian anda.")
    print("Nilai dalam bentuk angka. 0-100")
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
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
        os.chdir('..')
    elif pilihan == "y" or pilihan == "yes":
        print("\n\n\n\n")
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break