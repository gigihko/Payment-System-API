from datetime import datetime, timedelta

def is_cuti_pribadi_valid(jumlah_cuti_bersama, tanggal_join, tanggal_rencana_cuti, durasi_cuti):
    # Konversi input tanggal dari string ke objek datetime
    tanggal_join = datetime.strptime(tanggal_join, '%Y-%m-%d')
    tanggal_rencana_cuti = datetime.strptime(tanggal_rencana_cuti, '%Y-%m-%d')

    # Hitung tanggal mulai cuti pribadi (180 hari setelah tanggal bergabung)
    tanggal_mulai_cuti_pribadi = tanggal_join + timedelta(days=180)

    # Jika tanggal rencana cuti sebelum tanggal mulai cuti pribadi
    if tanggal_rencana_cuti < tanggal_mulai_cuti_pribadi:
        return False, "Belum 180 hari sejak tanggal bergabung."

    # Hitung jumlah hari yang tersisa dalam tahun tersebut
    akhir_tahun = datetime(tanggal_join.year, 12, 31)
    jumlah_hari_dari_mulai_cuti = (akhir_tahun - tanggal_mulai_cuti_pribadi).days + 1

    # Hitung jumlah cuti pribadi yang bisa diambil (dibulatkan ke bawah)
    jumlah_cuti_pribadi_dapat_diambil = (jumlah_hari_dari_mulai_cuti * jumlah_cuti_bersama) // 365

    # Cek durasi cuti tidak lebih dari 3 hari
    if durasi_cuti > 3:
        return False, "Durasi cuti pribadi maksimal 3 hari berturut-turut."

    # Cek apakah durasi cuti lebih dari jumlah cuti pribadi yang tersedia
    if durasi_cuti > jumlah_cuti_pribadi_dapat_diambil:
        return False, f"Hanya boleh mengambil {jumlah_cuti_pribadi_dapat_diambil} hari cuti."

    return True, "Cuti pribadi dapat diambil."

# Contoh pengujian
input_cases = [
    (7, '2021-05-01', '2021-07-05', 1),  # False: Belum 180 hari
    (7, '2021-05-01', '2021-11-05', 3),  # False: Hanya boleh ambil 1 hari
    (7, '2021-01-05', '2021-12-18', 1),  # True
    (7, '2021-01-05', '2021-12-18', 3),  # True
]

for case in input_cases:
    jumlah_cuti_bersama, tanggal_join, tanggal_rencana_cuti, durasi_cuti = case
    result, alasan = is_cuti_pribadi_valid(jumlah_cuti_bersama, tanggal_join, tanggal_rencana_cuti, durasi_cuti)
    print(f"Input: {case}\nOutput: {result}\nAlasan: {alasan}\n")
