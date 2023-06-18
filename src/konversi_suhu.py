while True:
    print("Selamat datang di aplikasi konversi suhu!")

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9 / 5 + 32
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5 / 9 + 273.15

    def convert_temperature():
        print("Konversi Suhu")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Kelvin to Celsius")
        print("4. Celsius to Kelvin")
        print("5. Kelvin to Fahrenheit")
        print("6. Fahrenheit to Kelvin")


        option = input("Silahkan pilih konversi yang diinginkan: ")
        if not option.isdigit():
            print("Pilihan harus berupa angka!")
            return
        else:
            option = int(option)
            if option == 1:
                celsius = float(input("Masukkan suhu dalam Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print("Suhu dalam Celsius:", fahrenheit)
            elif option == 2:
                fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print("Suhu dalam Celsius:", celsius)
            elif option == 3:
                kelvin = float(input("Masukkan suhu dalam Kelvin: "))
                celsius = kelvin_to_celsius(kelvin)
                print("Suhu dalam Celsius:", celsius)
            elif option == 4:
                celsius = float(input("Masukkan suhu dalam Celsius: "))
                kelvin = celsius_to_kelvin(celsius)
                print("Suhu dalam Kelvin:", kelvin)
            elif option == 5:
                kelvin = float(input("Masukkan suhu dalam Kelvin: "))
                fahrenheit = kelvin_to_fahrenheit(kelvin)
                print("Suhu dalam Fahrenheit:", fahrenheit)
            elif option == 6:
                fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
                kelvin = fahrenheit_to_kelvin(fahrenheit)
                print("Suhu dalam Kelvin:", kelvin)
            else:
                print("Pilihan tidak valid!, silahkan ulangi kembali")

    convert_temperature()

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
