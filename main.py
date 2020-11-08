# DDP LAB-4
# Nama: Agung Mubarok - SI05
# NIM: 0110120196

# SOAL 1 - Mencetak nama
# Tuliskan program untuk Soal 1 di bawah ini
print("\t" * 6 ,"Mencetak Nama")
print("\t" * 4 , "=" * 30)

# Variabel nama untuk menampung nilai string yang di input
nama = str(input("Masukan nama : ")) 

# Variabel hitung menampung nilai panjang dari variabel nama menggunakan fungsi len
hitung = len(nama)
# Variabel mulai untuk memulai dari huruf awal
mulai = 0
# Mulai perulangan, mulai kurang dari sama dengan hitung yang artinya mulai hitung nama dari awal sampai akhir huruf pada nama
while mulai <= hitung:
  # Mencetak nama dimulai dari pertama
  print (nama[0:mulai])
  # Melakukan penambahan pada setiap baris
  mulai += 1


# SOAL 2 - Validasi teks
# Tuliskan program untuk Soal 2 di bawah ini
print("\t" * 6 ,"Validasi Teks")
print("\t" * 4 , "=" * 30)

while True:
  # Variabel teks yang berguna untuk menyimpan nilai dari inputan 
  teks = input("\nMasukan sebuah teks : ")
  # Variabel kTeks berguna untuk pengkonversian ke huruf kecil menggunakan fungsi lower
  kTeks = teks.lower()

  # validasi_1 untuk menaruh nilai panjang teks kurang dari 8
  validasi_1 = len(teks) < 8
  # validasi_2 untuk menghitung nilai yang mengandung frase nf yang sudah menggunakan fungsi lower, dan jika terdapat frase tersebut maka akan bernilai true
  validasi_2 = kTeks.count('nf') > 0
  # validasi_3 untuk membuat perintah agar teks diakhiri dengan YYY/yyy
  validasi_3 = teks.endswith("YYY") or teks.endswith("yyy")
  # validasi_4 untuk mengembalikan nilai true jika didalamnya berisi karakter alphabet
  validasi_4 = teks.isalpha()

  # Menjalakan validasi_1 teks minimal 8 huruf/kurang dari 8
  if validasi_1:
    # Maka Teks tidak valid dan akan menampilkan pesan
    print("\nTeks tidak valid")
    print("Pesan: Panjang teks minimal 8 huruf")
  # Menjalankan jika validasi 2 tidak mengandung frase NF/Nf/nF/nf
  elif not validasi_2:
    # Maka Teks tidak valid dan akan menampilkan pesan
    print("\nTeks tidak valid")
    print("Pesan: Teks mengandung minimal sebuah frase 'NF' (tidak harus kapital semua)")
  # Menjalankan jika validasi_3 tidak diakhiri dengan YYY/yyy
  elif not validasi_3:
    # Maka Teks tidak valid dan akan menampilkan pesan
    print("\nTeks tidak valid")
    print("Pesan: Teks diakhiri dengan 'YYY' atau 'yyy' (kapital semua atau huruf kecil semua)")
  # Menjalakan validasi_4 merupakan semua karakter alphabet
  elif validasi_4:
    # Maka Teks tidak valid dan akan menampilkan pesan
    print("\nTeks tidak valid")
    print("Pesan: Teks harus mengandung angka")
  # Menjalankan sesuai validasi dari 1-3 dan jika validasi_4 tidak semua berisi karakter alphabet
  elif validasi_1 or validasi_2 or validasi_3 or not validasi_4:
    # Maka Teks valid
    print("Teks valid")
    print("\n\nTerima Kasih")
    break
  # Jika tidak menjalankan validasi
  else:
    print("Teks tidak valid")
