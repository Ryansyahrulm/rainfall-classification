import math

# Memory
memory = {
    10: 0,   # Nilai Curah Hujan                   
    11: 0.5,
    12: 20,
    13: 50,
    14: 100,
    15: 150,
    20: "Tidak hujan",
    21: "Hujan ringan",
    22: "Hujan sedang",
    23: "Hujan lebat",
    24: "Hujan sangat lebat",
    25: "Hujan ekstrem",
    26: "Input tidak valid",
}

# Daftar instruksi
program = {
    # --- Validasi input ---
     1: ("LOAD", 10), 
     2: ("JN", 29),   

    # --- Cek 1: R < 0,5 ? ---
     3: ("SUB", 11),
     4: ("JN", 19),

    # --- Cek 2: R < 20 ? ---
     5: ("LOAD", 10),
     6: ("SUB", 12),
     7: ("JN", 21),

    # --- Cek 3: R < 50 ? ---
     8: ("LOAD", 10),
     9: ("SUB", 13),
    10: ("JN", 23),

    # --- Cek 4: R < 100 ? ---
    11: ("LOAD", 10),
    12: ("SUB", 14),
    13: ("JN", 25),

    # --- Cek 5: R < 150 ? ---
    14: ("LOAD", 10),
    15: ("SUB", 15),
    16: ("JN", 27),

    # --- R >= 150 ---
    17: ("PRINT", 25),
    18: ("HALT", None),

    # --- Blok keluaran ---
    19: ("PRINT", 20),
    20: ("HALT", None),
    21: ("PRINT", 21),
    22: ("HALT", None),
    23: ("PRINT", 22),
    24: ("HALT", None),
    25: ("PRINT", 23),
    26: ("HALT", None),
    27: ("PRINT", 24),
    28: ("HALT", None),
    29: ("PRINT", 26),
    30: ("HALT", None),
}


# Proses eksekusi instruksi
def jalankan_simulator(R, jejak=True):
    # Register (variabel lokal)
    ACC = 0    # accumulator
    PC = 1     # program counter (nomor baris program)
    memory[10] = R
    jumlah = 0
    hasil = None

    if jejak:
        print("Baris | Instruksi  | ACC sebelum -> setelah | Keterangan")

    while True:
        instruksi, alamat = program[PC]
        acc_sebelum, baris = ACC, PC
        PC += 1                                 
        ket = ""

        if instruksi == "LOAD":
            ACC = memory[alamat]
        elif instruksi == "SUB":
            ACC = ACC - memory[alamat]
        elif instruksi == "JN":
            if ACC < 0:
                PC = alamat                      
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

    return {"kategori": hasil, "jumlah_instruksi": jumlah, "acc_akhir": ACC}

# Input dari pengguna
def baca_input():
    while True:
        teks = input("Masukkan curah hujan R (mm/hari): ").strip()
        teks = teks.replace(",", ".")
        try:
            R = float(teks)
        except ValueError:
            print("Input harus berupa angka, coba lagi.\n")
            continue
        if not math.isfinite(R):
            print("Input tidak boleh nan atau inf, coba lagi.\n")
            continue
        return R


# Program utama
if __name__ == "__main__":
    print("============================================")
    print("=== SIMULATOR MINI COMPUTER: CURAH HUJAN ===")
    print("============================================")
    while True:
        R = baca_input()
        print(f"\n======================== Hasil Perhitungan ========================")
        hasil = jalankan_simulator(R)
        print(f"\nKategori: {hasil['kategori']} ({hasil['jumlah_instruksi']} instruksi dijalankan)\n")

        lagi = input("Hitung lagi? (y/n): ").strip().lower()
        print()
        if lagi != "y":
            print("Program selesai.")
            break