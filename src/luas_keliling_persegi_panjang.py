while True:
    print("Selamat datang di aplikasi cek keliling persegi panjang!")
    def cek_keliling(panjang, lebar):
        print('Menu Cek Keliling dan Luas Persegi Panjang')
        print('1. Keliling Persegi Panjang')
        print('2. Luas Persegi Panjang')
        print('3. Luas Dan Keliling Persegi Panjang')
        print('0. Keluar')
        pilihan =input("Masukkan operasi bilangan : ")
        if not pilihan.isdigit():
            print("Pilihan harus berupa angka!")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            keliling = 2 * (panjang + lebar)
            print("Keliling persegi panjang dengan panjang {} dan lebar {} adalah {}".format(panjang, lebar, keliling))
            return
        elif pilihan == 2:
            input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            luas = panjang * lebar
            print("Luas persegi panjang dengan panjang {} dan lebar {} adalah {}".format(panjang, lebar, luas))
            return
        elif pilihan == 3:
            input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            keliling = 2 * (panjang + lebar)
            luas = panjang * lebar
            print("Keliling persegi panjang dengan panjang {} dan lebar {} adalah {}".format(panjang, lebar, keliling))
            print("Luas persegi panjang dengan panjang {} dan lebar {} adalah {}".format(panjang, lebar, luas))
            return
        elif pilihan == 0:
            print("Terima kasih sudah menggunakan aplikasi ini.")
            return
        else:
            print("Pilihan tidak valid! ")
            return
    print("Masukkan nilai panjang dan lebar persegi panjang anda untuk mengetahui kelilingnya.")
    cek_keliling(input("Masukkan panjang: "), input("Masukkan lebar: "))
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