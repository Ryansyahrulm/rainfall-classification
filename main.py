# ============================================================
# Simulasi Klasifikasi Intensitas Curah Hujan (Mini Computer)
# Mata Kuliah: Organisasi dan Arsitektur Komputer
# Kelas E / Kelompok 12
# ============================================================

# ---------------- a. Memory ----------------
memory = {
    10: 35,                      # curah_hujan (R, mm/hari)
    11: 0.5, 12: 20, 13: 50,     # batas_1 .. batas_3
    14: 100, 15: 150,            # batas_4 .. batas_5
    20: "Tidak hujan",
    21: "Hujan ringan",
    22: "Hujan sedang",
    23: "Hujan lebat",
    24: "Hujan sangat lebat",
    25: "Hujan ekstrem",
    26: "Input tidak valid",
}

# ---------------- b. Register ----------------
ACC = 0    # accumulator
PC = 1     # program counter (nomor baris program)

# ---------------- c. Daftar instruksi ----------------
# Program: Klasifikasi Intensitas Curah Hujan
# M[x] = isi memory alamat x, R = M[10] (curah hujan)
program = {
    # --- Validasi input ---
     1: ("LOAD", 10),   # ACC = M[10] (R)
     2: ("JN", 29),     # Jika ACC < 0 (R negatif) -> lompat ke baris 29

    # --- Cek 1: R < 0,5 ? ---
     3: ("SUB", 11),    # ACC = ACC - M[11] (R - 0,5)
     4: ("JN", 19),     # Jika ACC < 0 -> lompat ke baris 19 (Tidak hujan)

    # --- Cek 2: R < 20 ? ---
     5: ("LOAD", 10),   # ACC = M[10] (R dimuat ulang)
     6: ("SUB", 12),    # ACC = ACC - M[12] (R - 20)
     7: ("JN", 21),     # Jika ACC < 0 -> lompat ke baris 21 (Hujan ringan)

    # --- Cek 3: R < 50 ? ---
     8: ("LOAD", 10),   # ACC = M[10] (R dimuat ulang)
     9: ("SUB", 13),    # ACC = ACC - M[13] (R - 50)
    10: ("JN", 23),     # Jika ACC < 0 -> lompat ke baris 23 (Hujan sedang)

    # --- Cek 4: R < 100 ? ---
    11: ("LOAD", 10),   # ACC = M[10] (R dimuat ulang)
    12: ("SUB", 14),    # ACC = ACC - M[14] (R - 100)
    13: ("JN", 25),     # Jika ACC < 0 -> lompat ke baris 25 (Hujan lebat)

    # --- Cek 5: R < 150 ? ---
    14: ("LOAD", 10),   # ACC = M[10] (R dimuat ulang)
    15: ("SUB", 15),    # ACC = ACC - M[15] (R - 150)
    16: ("JN", 27),     # Jika ACC < 0 -> lompat ke baris 27 (Hujan sangat lebat)

    # --- R >= 150 ---
    17: ("PRINT", 25),  # Tampilkan M[25] ("Hujan ekstrem")
    18: ("HALT", None), # Hentikan program

    # --- Blok keluaran ---
    19: ("PRINT", 20),  # Tampilkan M[20] ("Tidak hujan")
    20: ("HALT", None), # Hentikan program
    21: ("PRINT", 21),  # Tampilkan M[21] ("Hujan ringan")
    22: ("HALT", None), # Hentikan program
    23: ("PRINT", 22),  # Tampilkan M[22] ("Hujan sedang")
    24: ("HALT", None), # Hentikan program
    25: ("PRINT", 23),  # Tampilkan M[23] ("Hujan lebat")
    26: ("HALT", None), # Hentikan program
    27: ("PRINT", 24),  # Tampilkan M[24] ("Hujan sangat lebat")
    28: ("HALT", None), # Hentikan program
    29: ("PRINT", 26),  # Tampilkan M[26] ("Input tidak valid")
    30: ("HALT", None), # Hentikan program
}


# ---------------- d. Proses eksekusi instruksi ----------------
def jalankan(R, jejak=True):
    global ACC, PC
    memory[10] = R          # isi input
    ACC, PC = 0, 1          # reset register
    jumlah = 0
    hasil = None

    if jejak:
        print("Baris | Instruksi  | ACC sebelum -> setelah | Keterangan")

    while True:
        instruksi, alamat = program[PC]
        acc_sebelum, baris = ACC, PC
        PC += 1                                  # default: baris berikutnya
        ket = ""

        if instruksi == "LOAD":
            ACC = memory[alamat]
        elif instruksi == "SUB":
            ACC = ACC - memory[alamat]
        elif instruksi == "JN":
            if ACC < 0:
                PC = alamat                      # lompat
                ket = f"ACC < 0, lompat ke baris {alamat}"
            else:
                ket = "ACC >= 0, tidak lompat"
        elif instruksi == "PRINT":
            hasil = memory[alamat]
            ket = f"Output: {hasil}"
        elif instruksi == "HALT":
            ket = "Selesai"

        jumlah += 1

        if jejak:
            nama = instruksi if alamat is None else f"{instruksi} {alamat}"
            print(f"{baris:>5} | {nama:<10} | "
                  f"   {round(acc_sebelum, 4):>6} -> {round(ACC, 4):<8}  | {ket}")

        if instruksi == "HALT":
            break

    return hasil, jumlah


# ---------------- e. Keterangan rentang klasifikasi ----------------
def tampilkan_rentang():
    print("=" * 56)
    print(" KETERANGAN KLASIFIKASI INTENSITAS CURAH HUJAN")
    print(" (R = curah hujan dalam mm/hari)")
    print("=" * 56)
    print(" R < 0\t\t\t: Input tidak valid")
    print(" 0 <= R < 0.5\t\t: Tidak hujan")
    print(" 0.5 <= R < 20\t\t: Hujan ringan")
    print(" 20 <= R < 50\t\t: Hujan sedang")
    print(" 50 <= R < 100\t\t: Hujan lebat")
    print(" 100 <= R < 150\t\t: Hujan sangat lebat")
    print(" R >= 150\t\t: Hujan ekstrem")
    print("=" * 56)
    print()


# ---------------- f. Input dari pengguna ----------------
def baca_input():
    """Minta R dari pengguna; ulangi sampai yang dimasukkan berupa angka."""
    while True:
        teks = input("Masukkan curah hujan R (mm/hari): ").strip()
        teks = teks.replace(",", ".")            # terima koma desimal (12,5)
        try:
            return float(teks)
        except ValueError:
            print("Input harus berupa angka, coba lagi.\n")


# ---------------- Program utama ----------------
if __name__ == "__main__":
    tampilkan_rentang()

    while True:
        R = baca_input()
        print(f"\n======================== Jejak eksekusi R = {R:g} ========================")
        hasil, n = jalankan(R)
        print(f"\nKategori: {hasil} ({n} instruksi dijalankan)\n")

        lagi = input("Hitung lagi? (y/n): ").strip().lower()
        print()
        if lagi != "y":
            print("Program selesai.")
            break