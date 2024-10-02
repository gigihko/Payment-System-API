def hitung_kembalian(total_belanja, uang_dibayar):
    # Daftar pecahan uang yang tersedia
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    
    # Cek apakah uang yang dibayarkan cukup
    if uang_dibayar < total_belanja:
        print(False, "kurang bayar")  # Kurang bayar
        return  # Menghentikan fungsi jika kurang bayar
    
    # Hitung kembalian
    kembalian = uang_dibayar - total_belanja
    
    # Bulatkan kembalian ke bawah ke kelipatan 100
    kembalian_bulat = (kembalian // 100) * 100
    
    # Cetak kembalian
    print(f"Kembalian yang harus diberikan kasir: {kembalian}, dibulatkan menjadi {kembalian_bulat}")
    
    # Menghitung pecahan uang yang akan diberikan
    pecahan_dicetak = {}
    sisa_kembalian = kembalian_bulat
    
    for pecahan in pecahan_uang:
        if sisa_kembalian >= pecahan:
            jumlah_pecahan = sisa_kembalian // pecahan
            pecahan_dicetak[pecahan] = jumlah_pecahan
            sisa_kembalian -= jumlah_pecahan * pecahan
    
    # Cetak pecahan uang yang akan diberikan
    print("Pecahan uang yang diberikan:")
    for pecahan, jumlah in pecahan_dicetak.items():
        if pecahan >= 1000:
            print(f"{jumlah} lembar {pecahan}")
        else:
            print(f"{jumlah} koin {pecahan}")

# Contoh pemanggilan fungsi
hitung_kembalian(700649, 800000)
# hitung_kembalian(575650, 580000)
# hitung_kembalian(657650, 600000)
