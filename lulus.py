print("=== Masukkan Data Siswa ===")
nama = input("Nama Lengkap : ")
kelas = input("Kelas : ")


try:
  nilai_ujian = int(input(f"Nilai Ujian {nama} : "))
  kehadiran = int(input(f"Persentase Kehadiran {nama} (%) : "))
except ValueError:
  print("Error: Nilai dan Kehadiran harus berupa angka (integer)!")
  exit()

if nilai_ujian >= 75 and kehadiran >= 75:
  status_lulus = True
else:
  status_lulus = False

print("\n=== Data Siswa ===")
print(f"Nama Lengkap : {nama}")
print(f"Kelas : {kelas}")
print(f"Nilai : {nilai_ujian}")
print(f"Kehadiran : {kehadiran}%")

if status_lulus:
  print("Status : Selamat, anda DINYATAKAN LULUS!!")
else:
  print("Status : Maaf, anda DINYATAKAN TIDAK LULUS.")