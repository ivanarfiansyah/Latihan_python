# DAFTAR HARGA DAGING PER KILOGRAM
import os
import tkinter as tk

harga_daging = {
    "ayam": 20000,
    "sapi": 25000,
    "kalkun": 32000}
# Variabel penampung total selama transaksi
total_kotor = 0      # total sebelum diskon
total_diskon = 0     # total potongan diskon
nota = []            # daftar item yang dibeli, untuk dicetak nanti

print(" MONGGOH DIBELI DAGINGNYA ")
print("Beli Daging Apa:", ", ".join(harga_daging.keys()))
print("Ketik 'cukup' jika sudah selesai belanja.\n")

# 2. PERULANGAN (WHILE LOOP) 
while True:
    jenis = input("Mau Beli Daging Apa Lagi? ").lower()

    # Cek Pembeli Mau Beli lagi atau tidak
    if jenis == "cukup":
        break

    # CEK JENIS DAGING  
    if jenis not in harga_daging:
        print(">> Maaf, jenis daging tidak tersedia. Coba lagi.\n")
        continue  # langsung ulangi loop, minta input lagi

    # JUMLAH PEMBELIAN DAGING
    try:
        jumlah = float(input(f"Berapa Kg {jenis} yang ingin dibeli? "))
    except ValueError:
        print(">> Input jumlah harus berupa angka. Coba lagi.\n")
        continue

    if jumlah <= 0:
        print(">> Jumlah harus lebih dari 0. Coba lagi.\n")
        continue

    # Hitung subtotal untuk item ini
    harga_satuan = harga_daging[jenis]
    subtotal = harga_satuan * jumlah

    diskon = 0  # default tidak ada diskon

    if jenis == "ayam":
        if jumlah >= 5:
            diskon = subtotal * 0.10
    elif jenis == "sapi":
        if jumlah >= 2:
            diskon = subtotal * 0.15
    elif jenis == "kalkun":
        if jumlah >= 3:
            diskon = subtotal * 0.12

    subtotal_bersih = subtotal - diskon

    # Tambahkan ke total keseluruhan
    total_kotor += subtotal
    total_diskon += diskon

    # Simpan detail item untuk dicetak di nota nanti
    nota.append({
        "jenis": jenis,
        "jumlah": jumlah,
        "harga_satuan": harga_satuan,
        "subtotal": subtotal,
        "diskon": diskon ,
        "subtotal_bersih": subtotal_bersih
    })

    print(f">> {jumlah} Kg {jenis} ditambahkan. Subtotal: Rp{subtotal:,.0f} "
          f"(diskon: Rp{diskon:,.0f})\n")

# ===== 5. CETAK NOTA PEMBAYARAN =====
total_bersih = total_kotor - total_diskon

print("\n========= NOTA PEMBAYARAN =========")
if not nota:
    print("Tidak ada barang yang dibeli.")
else:
    for item in nota:
        print(f"{item['jenis'].capitalize():<6} | "
              f"{item['jumlah']:>5.2f} Kg x Rp{item['harga_satuan']:,} "
              f"= Rp{item['subtotal']:,.0f} "
              f"(diskon Rp{item['diskon']:,.0f})")

print("------------------------------------")
print(f"Total Kotor   : Rp{total_kotor:,.0f}")
print(f"Total Diskon  : Rp{total_diskon:,.0f}")
print(f"Total Bersih  : Rp{total_bersih:,.0f}")
print("====================================")
print("Terima kasih sudah berbelanja!")

