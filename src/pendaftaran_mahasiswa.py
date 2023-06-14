while True:
    print("Selamat datang di aplikasi cek kelulusan mahasiswa!")
    def form_mahasiswa():
        # check if nilai is not numbers
        nim = input("Masukkan NIM: ")
        if not nim.isdigit():
            print("Nilai Nim harus berupa angka!")
        else:
            nama = input("Masukkan Nama: ")
            umur = input("Masukkan Umur: ")
            if not umur.isdigit() or not nim.isdigit():
                print("Nilai Umur harus berupa angka!")
            else:
                umur = int(umur)
                print('Masukkan Jenis Kelamin')
                jk = input("Input L/P :")
                if jk == "L" or jk == "l":
                    jk = "Laki-laki"
                elif jk == "P" or jk == "p":
                    jk = "Perempuan"
                else:
                    jk = "Tidak diketahui"
                alamat = input("Masukkan Alamat: ")
                if nim == "" or nama == "" or umur == "" or jk == "" or alamat == "":
                    print("Data tidak boleh kosong!")
                else:
                    print("NIM: ", nim)
                    print("Nama: ", nama)
                    print("Umur: ", umur)
                    print("Jenis Kelamin: ", jk)
                    print("Alamat: ", alamat)

    print("Masukkan data anda untuk pendafataran mahasiswa baru.")
    form_mahasiswa()
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