# menghitung total upah kerja buruh dengan syarat:
# 1. Total Upah kerja ditetapkan berdasarkan jumlah jam kerja.
# 2. Upah per jam Rp 2.500,-
# 3. Terdapat inputan berapa jumlah jam kerja.
# 4. Jika terdapat 1 pelanggaran  maka dikenakan pajak 15% nilai pelanggaran pajak berlipat ganda.
while True:
    print("Selamat datang di aplikasi menghitung total upah kerja buruh!")
    print("Masukkan total jam kerja anda untuk mengetahui total upah kerja anda.")
    print("Total jam kerja dalam bentuk angka.")
    pajak =0.05
    upahperjam =2500
    def hitung_upah(total_jam):
        if not total_jam.isdigit():
            print("Total jam harus berupa angka!")
        else:
            total_jam=int(total_jam)
            total_upah =total_jam * upahperjam
            pelanggaran =input("Apakah anda terdapat Pelanggaran? (yes/no): ").lower()
            if pelanggaran == "n" or pelanggaran == "no":
                print(f"Upah anda sebesar: {total_upah}")
            elif pelanggaran == "y" or pelanggaran == "yes":
                while True:
                    total_pelanggaran = input("Masukkan Total Pelanggaran: ")
                    if not total_pelanggaran.isdigit():
                        print("Total Pelanggaran harus berupa angka!")
                        print("Silakan ulangi lagi")
                        continue
                    else:
                        total_pelanggaran = int(total_pelanggaran)
                        total_upah_pelanggaran = (total_pelanggaran * pajak) *total_upah
                        print(f"Potong Gaji Pelanggaran: {total_upah_pelanggaran}")
                        total_upah -= total_upah_pelanggaran
                        print(f"Upah anda sebesar: {total_upah}")
                    break
    print("Aplikasi menghitung total upah kerja\n")
    hitung_upah(input("Masukkan Jam Kerja: \n"))
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
        os.chdir('..')
    elif pilihan == "y" or pilihan == "yes":
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        break


