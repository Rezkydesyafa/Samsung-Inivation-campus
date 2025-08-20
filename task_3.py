#Tugas 3
harga_kopi = 18000.5
harga_roti = 10000
 
jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")

jumlah_kopi_int = int(jumlah_kopi_str)
jumlah_roti_int = int(jumlah_roti_str)

total_kopi = harga_kopi * jumlah_kopi_int
total_roti = harga_roti * jumlah_roti_int
total_belanja = total_kopi + total_roti

uang_bayar = 50000
kembalian = uang_bayar - total_belanja

print("Total harga kopi:", total_kopi)
print("Total harga roti:", total_roti)
print("Total belanja keseluruhan:", total_belanja)
print("Uang yang dibayarkan:", uang_bayar)
print("Kembalian:", kembalian)