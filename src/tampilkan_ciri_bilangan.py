while True:
    print("Selamat datang di aplikasi cek Operasi Bilangan!")
    def cek_bilangan():
        # check if nilai is not numbers
        print('Menu Cek Bilangan \n'
              '1. Operasi bilangan Genap/Ganjil \n'
              '2. Operasi bilangan Positif/Negatif \n'
              '3. Operasi bilangan Prima \n'
              '4. Operasi bilangan Bulat')
        input("Masukkan operasi bilangan : ")

    print("Masukkan nilai anda untuk mengetahui apakah anda lulus atau tidak.")
    cek_bilangan()
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