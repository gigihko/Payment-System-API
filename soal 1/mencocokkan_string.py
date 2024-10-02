def find_matching_strings():
    # Input jumlah string
    N = int(input("Masukkan jumlah string: "))

    # Inisialisasi list untuk menyimpan string
    strings = []

    # Input string satu per satu
    for i in range(N):
        s = input().strip()
        strings.append(s.lower())  # Simpan string dalam huruf kecil (case insensitive)

    # Inisialisasi list untuk menyimpan kecocokan
    matches = []

    # Pencocokan string
    for i in range(N):
        temp_match = [i + 1]  # Simpan nomor string pertama
        for j in range(i + 1, N):
            if strings[i] == strings[j]:
                temp_match.append(j + 1)  # Tambahkan nomor string yang cocok
        if len(temp_match) > 1:
            matches.append(temp_match)

    # Jika ditemukan kecocokan, tampilkan set dengan jumlah kecocokan terbanyak
    if matches:
        longest_match = max(matches, key=len)
        print(*longest_match)
    else:
        # Jika tidak ditemukan string yang cocok
        print(False)

# Contoh pemanggilan fungsi
find_matching_strings()
