while True:
    print("Selamat datang di aplikasi cek volume kubus!")
    def cek_volume():
        print('Menu Cek Volume dan Luas kubus')
        print('1. Volume kubus')
        print('2. Luas kubus')
        print('3. Volume dan Luas kubus')
        print('4. Luas Permukaan kubus')
        print('0. Keluar')
        pilihan =input("Masukkan operasi bilangan : ")
        if not pilihan.isdigit():
            print("Pilihan harus berupa angka!")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            sisi=input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            volume = sisi * sisi * sisi
            print("Volume kubus dengan sisi {} adalah {}".format(sisi, volume))
            return
        elif pilihan == 2:
            sisi=input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            luas = 6 * sisi * sisi
            print("Luas kubus dengan sisi {} adalah {}".format(sisi, luas))
            return
        elif pilihan == 3:
            sisi=input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            volume = sisi * sisi * sisi
            luas = 6 * sisi * sisi
            print("Volume kubus dengan sisi {} adalah {}".format(sisi, volume))
            print("Luas kubus dengan sisi {} adalah {}".format(sisi, luas))
            return
        elif pilihan == 4:
            sisi=input("Masukkan sisi: ")
            if not sisi.isdigit():
                print("Sisi harus berupa angka!")
                return
            sisi = int(sisi)
            luas = 6 * sisi * sisi
            print("Luas Permukaan kubus dengan sisi {} adalah {}".format(sisi, luas))
            return
        elif pilihan == 0:
            return
        else:
            print("Pilihan tidak valid!")
            return
    cek_volume()
    print("Terima kasih telah menggunakan aplikasi ini!")
    print("Apakah anda ingin mengulang? (y/n)")
    pilihan = input().lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        print("\n\n\n\n")
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        break
