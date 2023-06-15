#cek nilai huruf
while True:
    print("Selamat datang di aplikasi cek nilai huruf!")
    print("Masukkan nilai anda untuk mengetahui nilai huruf anda.")
    print("Nilai dalam bentuk angka. 0-100")
    def cek_nilai(nilai):
        if not nilai.isdigit():
            print("Nilai harus berupa angka!")
        elif int(nilai) > 100:
            print("Nilai tidak boleh lebih dari 100!")
        else:
            nilai = int(nilai)
            if nilai > 90:
                print("Nilai anda: A")
            elif nilai >= 81:
                print("Nilai anda: B")
            elif nilai >= 71:
                print("Nilai anda: C")
            elif nilai >= 51:
                print("Nilai anda: D")
            else:
                print("Nilai anda: E")
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