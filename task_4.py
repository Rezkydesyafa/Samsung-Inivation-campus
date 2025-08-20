# TUGAS 4

nama_produk1 = "Kopi Pagi"
harga_produk1 = 18000.5

jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
jumlah_kopi_int = int(jumlah_kopi_str)
total_kopi = harga_produk1 * jumlah_kopi_int

nama_pelanggan = input("Masukkan nama pelanggan: ")
pesan_terima_kasih = "\nTerima kasih, " + nama_pelanggan + " sudah berbelanja di Coffee Shop Bahagia!\n"

garis = "*" * 25

print(garis)
print(pesan_terima_kasih)
print(garis)
print(f"Total harga {nama_produk1} adalah Rp{total_kopi}")