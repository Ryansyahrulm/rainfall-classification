# Simulasi Klasifikasi Intensitas Curah Hujan (Mini Computer)

Proyek mata kuliah **Organisasi dan Arsitektur Komputer** — Kelas E / Kelompok 12.

Program Python yang mensimulasikan Mini Computer sederhana untuk mengklasifikasikan curah hujan harian R (mm/hari). Klasifikasi dilakukan lewat instruksi mesin buatan (`LOAD`, `SUB`, `JN`, `PRINT`, `HALT`), bukan dengan `if-else` langsung.

## Anggota

- Ryan Syahrul Muharam (257006111135)
- Febriana Nugraha (257006111129)
- Muhamad Alfian Holidi (257006111136)
- Fahmi Miftahudin (257006111146)

## Cara Menjalankan

Membutuhkan Python 3.6+ tanpa library tambahan.

```bash
python main.py
```

Masukkan nilai R (koma desimal seperti `12,5` diterima), lalu jawab `y` untuk menghitung lagi atau `n` untuk keluar.

## Klasifikasi

| Rentang R (mm/hari) | Kategori |
|---------------------|----------|
| R < 0 | Input tidak valid |
| 0 ≤ R < 0,5 | Tidak hujan |
| 0,5 ≤ R < 20 | Hujan ringan |
| 20 ≤ R < 50 | Hujan sedang |
| 50 ≤ R < 100 | Hujan lebat |
| 100 ≤ R < 150 | Hujan sangat lebat |
| R ≥ 150 | Hujan ekstrem |

## Mini Computer

- **Register:** `ACC` (accumulator) dan `PC` (program counter).
- **Memory:** alamat 10 untuk R, 11–15 untuk batas (0,5; 20; 50; 100; 150), 20–26 untuk label keluaran.
- **Instruksi:**

| Instruksi | Fungsi |
|-----------|--------|
| `LOAD alamat` | Memuat nilai memory ke ACC |
| `SUB alamat` | ACC = ACC − nilai pada alamat |
| `JN baris` | Jika ACC < 0, lompat ke baris tujuan |
| `PRINT alamat` | Menampilkan nilai pada alamat |
| `HALT` | Mengakhiri program |

Pengecekan "R < batas" dilakukan dengan menghitung `R − batas` lalu menguji tandanya dengan `JN`. Program terdiri dari 30 baris, dan program menampilkan jejak setiap instruksi yang dijalankan.

## Contoh Keluaran

Input `35`: kategori **Hujan sedang** (12 instruksi dijalankan).

## Keterbatasan

Teks `nan` dan `inf` masih diterima sebagai input dan menghasilkan "Hujan ekstrem".
