while True:
    print("Selamat datang di aplikasi cek volume balok!")
    def cek_volume():
        print('Menu Cek Volume dan Luas balok')
        print('1. Volume balok')
        print('2. Luas balok')
        print('3. Volume dan Luas balok')
        print('4. Luas Permukaan balok')
        print('0. Keluar')
        pilihan =input("Masukkan operasi bilangan : ")
        if not pilihan.isdigit():
            print("Pilihan harus berupa angka!")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            panjang=input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            lebar=input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            tinggi = int(tinggi)
            volume = panjang * lebar * tinggi
            print("Volume balok dengan panjang {}, lebar {}, dan tinggi {} adalah {}".format(panjang, lebar, tinggi, volume))
            return
        elif pilihan == 2:
            panjang=input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            lebar=input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            tinggi = int(tinggi)
            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            print("Luas balok dengan panjang {}, lebar {}, dan tinggi {} adalah {}".format(panjang, lebar, tinggi, luas))
            return
        elif pilihan == 3:
            panjang=input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            lebar=input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            tinggi = int(tinggi)
            volume = panjang * lebar * tinggi
            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            print("Volume balok dengan panjang {}, lebar {}, dan tinggi {} adalah {}".format(panjang, lebar, tinggi, volume))
            print("Luas balok dengan panjang {}, lebar {}, dan tinggi {} adalah {}".format(panjang, lebar, tinggi, luas))
            return
        elif pilihan == 4:
            panjang=input("Masukkan panjang: ")
            if not panjang.isdigit():
                print("Panjang harus berupa angka!")
                return
            lebar=input("Masukkan lebar: ")
            if not lebar.isdigit():
                print("Lebar harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            panjang = int(panjang)
            lebar = int(lebar)
            tinggi = int(tinggi)
            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            print("Luas balok dengan panjang {}, lebar {}, dan tinggi {} adalah {}".format(panjang, lebar, tinggi, luas))
            return
    print("Masukkan nilai panjang, lebar, dan tinggi balok anda untuk mengetahui volumenya.")
    cek_volume()
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