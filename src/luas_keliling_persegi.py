while True:
    print("Selamat datang di aplikasi cek keliling persegi!")
    def cek_keliling():
        print('Menu Cek Keliling dan Luas Persegi')
        print('1. Keliling Persegi')
        print('2. Luas Persegi')
        print('3. Luas Dan Keliling Persegi')
        print('0. Keluar')
        pilihan =input("Masukkan operasi bilangan : ")
        if not pilihan.isdigit():
            print("Pilihan harus berupa angka!")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            sisi = input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            keliling = 4 * sisi
            print("Keliling persegi dengan sisi {} adalah {}".format(sisi, keliling))
            return
        elif pilihan == 2:
            sisi = input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            luas = sisi * sisi
            print("Luas persegi dengan sisi {} adalah {}".format(sisi, luas))
            return
        elif pilihan == 3:
            sisi = input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            keliling = 4 * sisi
            luas = sisi * sisi
            print("Keliling persegi dengan sisi {} adalah {}".format(sisi, keliling))
            print("Luas persegi dengan sisi {} adalah {}".format(sisi, luas))
            return
        elif pilihan == 0:
            print("Terima kasih sudah menggunakan aplikasi ini.")
            return
        else:
            print("Pilihan tidak valid! ")
            return
    print("Masukkan nilai sisi persegi anda untuk mengetahui kelilingnya.")
    cek_keliling()
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        print("\n\n\n\n")
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break