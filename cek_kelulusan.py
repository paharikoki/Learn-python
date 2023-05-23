# Cek kelulusan mahasiswa
def cek_kelulusan(nilai):
    # check if nilai is not numbers
    if not nilai.isdigit():
        print("Nilai harus berupa angka!")
    else:
        nilai = int(nilai)
        if nilai >= 60:
            print("Selamat, anda lulus!")
        else:
            print("Maaf, anda tidak lulus.")
cek_kelulusan(input("Masukkan nilai: "))
while True:
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        cek_kelulusan(input("\nMasukkan nilai: "))
    else:
        print("Pilihan tidak valid!, Silakan masukkan (y/n) ")