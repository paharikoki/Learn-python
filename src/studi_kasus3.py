# Menghitung biaya total pengiriman barang di perusahaan Ekspedisi
# Lorena di Malang.
# 1. Biaya kirim ditentukan berdasarkan jarak per kilometernya.
# 2. Berikut ini pilihan kota tujuan pengiriman yang tersedia:
#  a. Surabaya (berjarak 169 km), ongkos kirim per km Rp 2500
#  b. Bandung (berjarak 452 km), ongkos kirim per km Rp 4000
# Data kota tujuan pengiriman
kota_tujuan = {
    'surabaya': {'jarak': 169, 'ongkos_per_km': 1500},
    'bandung': {'jarak': 452, 'ongkos_per_km': 2000},
    'jogja': {'jarak': 349, 'ongkos_per_km': 1500},
    'jakarta': {'jarak': 532, 'ongkos_per_km': 2500},
    'malang': {'jarak': 34, 'ongkos_per_km': 500},
    'bali': {'jarak': 210, 'ongkos_per_km': 2000},
}
def hitung_biaya_kirim(jarak, ongkos_per_km):
    return jarak * ongkos_per_km

while True:
    # Menampilkan pilihan kota tujuan pengiriman
    print("\n\nPilihan kota tujuan pengiriman:")
    for kota in kota_tujuan:
        print(f"- {kota.capitalize()}")

    # Meminta input kota tujuan dari pengguna
    tujuan = input("Masukkan kota tujuan pengiriman: ").lower()

    # Memeriksa apakah kota tujuan valid

    if tujuan in kota_tujuan:
        jarak = kota_tujuan[tujuan]['jarak']
        ongkos_per_km = kota_tujuan[tujuan]['ongkos_per_km']

        # Menghitung biaya kirim
        biaya_kirim = hitung_biaya_kirim(jarak, ongkos_per_km)

        # Menampilkan hasil perhitungan
        print(f"\nKota tujuan: {tujuan.capitalize()}")
        print(f"Jarak: {jarak} km")
        print(f"Ongkos per km: Rp {ongkos_per_km}")
        print(f"Biaya kirim: Rp {biaya_kirim}")
        pilihan = input("\nApakah anda ingin mengulang? (yes/no): ").lower()
        if pilihan == "n" or pilihan == "no":
            print("Terima kasih sudah menggunakan aplikasi ini.")
            break
            os.chdir('..')
        elif pilihan == "y" or pilihan == "yes":
            continue
    else:
            print("Pilihan tidak valid!, Silakan masukkan (y/n) ")
            continue
