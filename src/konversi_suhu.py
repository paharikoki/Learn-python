while True:
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    def kelvin_to_fahrenheit(kelvin):
        celsius = kelvin_to_celsius(kelvin)
        return celsius_to_fahrenheit(celsius)

    def fahrenheit_to_kelvin(fahrenheit):
        celsius = fahrenheit_to_celsius(fahrenheit)
        return celsius_to_kelvin(celsius)

    # Menampilkan pilihan konversi suhu
    print("Pilihan konversi suhu:")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Kelvin ke Celsius")
    print("4. Celsius ke Kelvin")
    print("5. Kelvin ke Fahrenheit")
    print("6. Fahrenheit ke Kelvin")

    # Meminta input pilihan konversi
    pilihan = int(input("Masukkan pilihan konversi: "))

    # Meminta input suhu yang akan dikonversi
    suhu = float(input("Masukkan suhu: "))

    # Melakukan konversi berdasarkan pilihan pengguna
    if pilihan == 1:
        hasil = celsius_to_fahrenheit(suhu)
        print(f"{suhu} derajat Celsius = {hasil} derajat Fahrenheit")
    elif pilihan == 2:
        hasil = fahrenheit_to_celsius(suhu)
        print(f"{suhu} derajat Fahrenheit = {hasil} derajat Celsius")
    elif pilihan == 3:
        hasil = kelvin_to_celsius(suhu)
        print(f"{suhu} Kelvin = {hasil} derajat Celsius")
    elif pilihan == 4:
        hasil = celsius_to_kelvin(suhu)
        print(f"{suhu} derajat Celsius = {hasil} Kelvin")
    elif pilihan == 5:
        hasil = kelvin_to_fahrenheit(suhu)
        print(f"{suhu} Kelvin = {hasil} derajat Fahrenheit")
    elif pilihan == 6:
        hasil = fahrenheit_to_kelvin(suhu)
        print(f"{suhu} derajat Fahrenheit = {hasil} Kelvin")
    else:
        print("Pilihan konversi tidak valid!")
    
    pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
    if pilihan == "n" or pilihan == "no":
        print("Terima kasih sudah menggunakan aplikasi ini.")
        break
    elif pilihan == "y" or pilihan == "yes":
        continue
    else:
        print("Pilihan Ulangi tidak valid! ")
        print("program telah berakhir")
        break
