import os
import subprocess

# Daftar file yang akan dijalankan
# Mendefinisikan direktori tempat file-file disimpan
folder = "src"

# Mendapatkan daftar file dalam direktori
files  = [file for file in os.listdir(folder) if file.endswith('.py') and file != '__init__.py']

# Menampilkan pilihan file
print("Pilihan file:")
for i, file in enumerate(files, start=1):
    # Menghilangkan ekstensi .py
    file_name = os.path.splitext(file)[0]
    print(f"{i}. {file_name}")
print("\n0. Keluar")
# Meminta input pilihan pengguna
pilihan = int(input("Masukkan nomor file yang ingin dijalankan: "))

try:
    if pilihan == 0 :
        print("Terima kasih sudah menggunakan aplikasi ini.")
        exit()
    # Menjalankan file terpilih menggunakan subprocess
    print("\n\n\n")
    subprocess.run(['python', os.path.join(folder, files[pilihan - 1])])
except ValueError:
    print("Nomor file harus berupa angka!")
except IndexError:
    print("Nomor file tidak valid!")
except KeyboardInterrupt:
    print("Dibatalkan oleh pengguna!")
os.system('python main.py')