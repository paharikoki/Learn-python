while True:
    print("Selamat datang di aplikasi konversi waktu!")
    def detik_to_menit(detik):
        return detik / 60
    def detik_to_jam(detik):
        return detik / 3600
    def detik_to_hari(detik):
        return detik / 86400
    def detik_to_minggu(detik):
        return detik / 604800
    def detik_to_bulan(detik):
        return detik / 2628000
    def detik_to_tahun(detik):
        return detik / 31536000
    def menit_to_detik(menit):
        return menit * 60
    def menit_to_jam(menit):
        return menit / 60
    def menit_to_hari(menit):
        return menit / 1440
    def menit_to_minggu(menit):
        return menit / 10080
    def menit_to_bulan(menit):
        return menit / 43800
    def menit_to_tahun(menit):
        return menit / 525600
    def jam_to_detik(jam):
        return jam * 3600
    def jam_to_menit(jam):
        return jam * 60
    def jam_to_hari(jam):
        return jam / 24
    def jam_to_minggu(jam):
        return jam / 168
    def jam_to_bulan(jam):
        return jam / 730
    def jam_to_tahun(jam):
        return jam / 8760
    def hari_to_detik(hari):
        return hari * 86400
    def hari_to_menit(hari):
        return hari * 1440
    def hari_to_jam(hari):
        return hari * 24
    def hari_to_minggu(hari):
        return hari / 7
    def hari_to_bulan(hari):
        return hari / 30
    def hari_to_tahun(hari):
        return hari / 365
    def minggu_to_detik(minggu):
        return minggu * 604800
    def minggu_to_menit(minggu):
        return minggu * 10080
    def minggu_to_jam(minggu):
        return minggu * 168
    def minggu_to_hari(minggu):
        return minggu * 7
    def minggu_to_bulan(minggu):
        return minggu / 4
    def minggu_to_tahun(minggu):
        return minggu / 52
    def bulan_to_detik(bulan):
        return bulan * 2628000
    def bulan_to_menit(bulan):
        return bulan * 43800
    def bulan_to_jam(bulan):
        return bulan * 730
    def bulan_to_hari(bulan):
        return bulan * 30
    def bulan_to_minggu(bulan):
        return bulan * 4
    def bulan_to_tahun(bulan):
        return bulan / 12
    def tahun_to_detik(tahun):
        return tahun * 31536000
    def tahun_to_menit(tahun):
        return tahun * 525600
    def tahun_to_jam(tahun):
        return tahun * 8760
    def tahun_to_hari(tahun):
        return tahun * 365
    def tahun_to_minggu(tahun):
        return tahun * 52
    def tahun_to_bulan(tahun):
        return tahun * 12


    def convert_temperature():
        print("Konversi Waktu")
        print("1. Detik")
        print("2. Menit")
        print("3. Jam")
        print("4. Hari")
        print("5. Minggu")
        print("6. Bulan")
        print("7. Tahun")
        print("0. Keluar")
        pilihan = input("Masukkan pilihan anda : ")
        if not pilihan.isdigit():
            print("Pilihan tidak valid!, silahkan coba lagi")
            return
        pilihan = int(pilihan)
        if pilihan == 1:
            print("1. Detik ke Menit")
            print("2. Detik ke Jam")
            print("3. Detik ke Hari")
            print("4. Detik ke Minggu")
            print("5. Detik ke Bulan")
            print("6. Detik ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_menit(detik), "menit")
                return
            elif pilihan == 2:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_jam(detik), "jam")
                return
            elif pilihan == 3:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_hari(detik), "hari")
                return
            elif pilihan == 4:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_minggu(detik), "minggu")
                return
            elif pilihan == 5:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_bulan(detik), "bulan")
                return
            elif pilihan == 6:
                detik = input("Masukkan detik : ")
                if not detik.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                detik = int(detik)
                print(detik, "detik adalah", detik_to_tahun(detik), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 2:
            print("1. Menit ke Detik")
            print("2. Menit ke Jam")
            print("3. Menit ke Hari")
            print("4. Menit ke Minggu")
            print("5. Menit ke Bulan")
            print("6. Menit ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_detik(menit), "detik")
                return
            elif pilihan == 2:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_jam(menit), "jam")
                return
            elif pilihan == 3:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_hari(menit), "hari")
                return
            elif pilihan == 4:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_minggu(menit), "minggu")
                return
            elif pilihan == 5:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_bulan(menit), "bulan")
                return
            elif pilihan == 6:
                menit = input("Masukkan menit : ")
                if not menit.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                menit = int(menit)
                print(menit, "menit adalah", menit_to_tahun(menit), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 3:
            print("1. Jam ke Detik")
            print("2. Jam ke Menit")
            print("3. Jam ke Hari")
            print("4. Jam ke Minggu")
            print("5. Jam ke Bulan")
            print("6. Jam ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_detik(jam), "detik")
                return
            elif pilihan == 2:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_menit(jam), "menit")
                return
            elif pilihan == 3:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_hari(jam), "hari")
                return
            elif pilihan == 4:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_minggu(jam), "minggu")
                return
            elif pilihan == 5:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_bulan(jam), "bulan")
                return
            elif pilihan == 6:
                jam = input("Masukkan jam : ")
                if not jam.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                jam = int(jam)
                print(jam, "jam adalah", jam_to_tahun(jam), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 4:
            print("1. Hari ke Detik")
            print("2. Hari ke Menit")
            print("3. Hari ke Jam")
            print("4. Hari ke Minggu")
            print("5. Hari ke Bulan")
            print("6. Hari ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_detik(hari), "detik")
                return
            elif pilihan == 2:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_menit(hari), "menit")
                return
            elif pilihan == 3:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_jam(hari), "jam")
                return
            elif pilihan == 4:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_minggu(hari), "minggu")
                return
            elif pilihan == 5:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_bulan(hari), "bulan")
                return
            elif pilihan == 6:
                hari = input("Masukkan hari : ")
                if not hari.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                hari = int(hari)
                print(hari, "hari adalah", hari_to_tahun(hari), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 5:
            print("1. Minggu ke Detik")
            print("2. Minggu ke Menit")
            print("3. Minggu ke Jam")
            print("4. Minggu ke Hari")
            print("5. Minggu ke Bulan")
            print("6. Minggu ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                minggu= input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_detik(minggu), "detik")
                return
            elif pilihan == 2:
                minggu = input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_menit(minggu), "menit")
                return
            elif pilihan == 3:
                minggu = input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_jam(minggu), "jam")
                return
            elif pilihan == 4:
                minggu = input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_hari(minggu), "hari")
                return
            elif pilihan == 5:
                minggu = input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_bulan(minggu), "bulan")
                return
            elif pilihan == 6:
                minggu = input("Masukkan minggu : ")
                if not minggu.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                minggu = int(minggu)
                print(minggu, "minggu adalah", minggu_to_tahun(minggu), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 6:
            print("1. Bulan ke Detik")
            print("2. Bulan ke Menit")
            print("3. Bulan ke Jam")
            print("4. Bulan ke Hari")
            print("5. Bulan ke Minggu")
            print("6. Bulan ke Tahun")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_detik(bulan), "detik")
                return
            elif pilihan == 2:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_menit(bulan), "menit")
                return
            elif pilihan == 3:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_jam(bulan), "jam")
                return
            elif pilihan == 4:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_hari(bulan), "hari")
                return
            elif pilihan == 5:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_minggu(bulan), "minggu")
                return
            elif pilihan == 6:
                bulan = input("Masukkan bulan : ")
                if not bulan.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                bulan = int(bulan)
                print(bulan, "bulan adalah", bulan_to_tahun(bulan), "tahun")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 7:
            print("1. Tahun ke Detik")
            print("2. Tahun ke Menit")
            print("3. Tahun ke Jam")
            print("4. Tahun ke Hari")
            print("5. Tahun ke Minggu")
            print("6. Tahun ke Bulan")
            print("0. Kembali")
            pilihan = input("Masukkan pilihan anda : ")
            if not pilihan.isdigit():
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
            pilihan = int(pilihan)
            if pilihan == 1:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_detik(tahun), "detik")
                return
            elif pilihan == 2:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_menit(tahun), "menit")
                return
            elif pilihan == 3:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_jam(tahun), "jam")
                return
            elif pilihan == 4:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_hari(tahun), "hari")
                return
            elif pilihan == 5:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_minggu(tahun), "minggu")
                return
            elif pilihan == 6:
                tahun = input("Masukkan tahun : ")
                if not tahun.isdigit():
                    print("Input tidak valid!, silahkan coba lagi")
                    return
                tahun = int(tahun)
                print(tahun, "tahun adalah", tahun_to_bulan(tahun), "bulan")
                return
            elif pilihan == 0:
                return
            else:
                print("Pilihan tidak valid!, silahkan coba lagi")
                return
        elif pilihan == 0:
            return
        else:
            print("Pilihan tidak valid!, silahkan coba lagi")
            return


    convert_temperature()
    ulagi = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if ulagi == "n" or ulagi == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif ulagi == "y" or ulagi == "yes":
        print("\n\n\n\n")
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break