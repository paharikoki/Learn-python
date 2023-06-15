# Cek kelulusan mahasiswa

while True:
    print("Selamat datang di aplikasi cek kelulusan mahasiswa!")
    def cek_kelulusan(nilai):
        # check if nilai is not numbers
        if not nilai.isdigit():
            print("Nilai harus berupa angka!")
        else:
            nilai = int(nilai)
            if nilai >= 60:
                print("Selamat, anda lulus!")
            else:
                print("Maaf, anda tidak lulus.")
    print("Masukkan nilai anda untuk mengetahui apakah anda lulus atau tidak.")
    cek_kelulusan(input("Masukkan nilai: "))
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