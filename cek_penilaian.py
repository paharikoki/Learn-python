#cek penilaian dengan huruf
def cek_nilai(nilai):
    if not nilai.isdigit():
        print("Nilai harus berupa angka!")
    elif int(nilai) > 100:
        print("Nilai tidak boleh lebih dari 100!")
    else:
        nilai = int(nilai)
        if nilai > 90:
            print("Nilai anda: A")
        elif nilai >= 81:
            print("Nilai anda: B")
        elif nilai >= 71:
            print("Nilai anda: C")
        elif nilai >= 51:
            print("Nilai anda: D")
        else:
            print("Nilai anda: E")
cek_nilai(input("Masukkan nilai: "))
while True:
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        cek_nilai(input("\nMasukkan nilai: "))
    else:
        print("Pilihan tidak valid!, Silakan masukkan (y/n) ")