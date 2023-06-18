while True:
    print("Selamat datang di aplikasi cek keliling Segitiga!")
    def cek_keliling():
        print('Menu Cek Keliling dan Luas segitiga')
        print('1. Keliling segitiga')
        print('2. Luas segitiga')
        print('3. Luas Dan Keliling segitiga Sama Sisi')
        print('4. Tinggi segitiga')
        print('5. Alas segitiga')
        print('0. Keluar')
        pilihan =input("Masukkan operasi bilangan : ")
        if not pilihan.isdigit():
            print("Pilihan harus berupa angka!")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            sisi1=input("Masukkan sisi1: ")
            if not sisi1.isdigit():
                print("Sisi1 harus berupa angka!")
                return
            sisi2=input("Masukkan sisi2: ")
            if not sisi2.isdigit():
                print("Sisi2 harus berupa angka!")
                return
            sisi3=input("Masukkan sisi3: ")
            if not sisi3.isdigit():
                print("Sisi3 harus berupa angka!")
                return
            sisi1 = int(sisi1)
            sisi2 = int(sisi2)
            sisi3 = int(sisi3)
            keliling = sisi1+sisi2+sisi3
            print("Keliling Segitiga dengan sisi A {}, sisi B {},sisi C {} adalah {}".format(sisi1,sisi2,sisi3,keliling))
            return
        elif pilihan == 2:
            alas= input("Masukkan alas: ")
            if not alas.isdigit():
                print("Alas harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            alas = int(alas)
            tinggi = int(tinggi)
            luas = (alas*0.5) * tinggi
            print("Luas Segitiga dengan alas {} dan tinggi {} adalah {}".format(alas, tinggi, luas))
            return
        elif pilihan == 3:
            alas=input("Masukkan alas: ")
            if not alas.isdigit():
                print("Alas harus berupa angka!")
                return
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            alas = int(alas)
            tinggi = int(tinggi)
            keliling = alas+alas+alas
            luas = (alas*0.5) * tinggi
            print("Keliling Segitiga sama sisi dengan alas {} adalah {}".format(alas, keliling))
            print("Luas Segitiga sama sisi dengan alas {} dan tinggi {} adalah {}".format(alas, tinggi, luas))
            return
        elif pilihan == 4:
            alas=input("Masukkan alas: ")
            if not alas.isdigit():
                print("Alas harus berupa angka!")
                return
            luas=input("Masukkan luas: ")
            if not luas.isdigit():
                print("Luas harus berupa angka!")
                return
            alas = int(alas)
            luas = int(luas)
            tinggi = (2*luas)/alas
            print("Tinggi Segitiga dengan alas {} dan luas {} adalah {}".format(alas, luas, tinggi))
            return
        elif pilihan == 5:
            tinggi=input("Masukkan tinggi: ")
            if not tinggi.isdigit():
                print("Tinggi harus berupa angka!")
                return
            luas=input("Masukkan luas: ")
            if not luas.isdigit():
                print("Luas harus berupa angka!")
                return
            tinggi = int(tinggi)
            luas = int(luas)
            alas = (2*luas)/tinggi
            print("Alas Segitiga dengan tinggi {} dan luas {} adalah {}".format(tinggi, luas, alas))
            # print("Luas persegi panjang dengan panjang {} dan lebar {} adalah {}".format(alas, tinggi, luas))
            return
        elif pilihan == 0:
            print("Terima kasih sudah menggunakan aplikasi ini.")
            return
        else:
            print("Pilihan tidak valid! ")
            return
    print("Masukkan nilai panjang dan lebar persegi panjang anda untuk mengetahui kelilingnya.")
    cek_keliling()
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