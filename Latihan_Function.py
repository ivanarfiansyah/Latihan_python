import json

def muat_daftar_menu():
    """Fungsi untuk memuat daftar menu"""
    return daftar_daging, jasa_potong

def tampilkan_menu_daging():
    """Fungsi untuk menampilkan menu daging yang tersedia"""
    print("\n" + "="*50)
    print("DAFTAR DAGING YANG TERSEDIA:")
    print("="*50)
    for idx, daging in enumerate(daftar_daging, 1):
        print(f"{idx}. {daging['jenis_daging'].upper()} - Rp{daging['harga_per_kg']:,}/kg")
    print("="*50)


def pilih_daging():
    """Fungsi untuk pembeli memilih jenis daging (Step 1)"""
    tampilkan_menu_daging()
    
    while True:
        try:
            pilihan = int(input("Pilih nomor daging (1-3): "))
            if 1 <= pilihan <= len(daftar_daging):
                return daftar_daging[pilihan - 1]
            else:
                print("⚠ Nomor tidak valid! Silakan pilih 1-3.")
        except ValueError:
            print("⚠ Input tidak valid! Masukkan angka.")


def masukkan_jumlah_kg(jenis_daging):
    """Fungsi untuk memasukkan jumlah Kg yang dibeli (Step 2)"""
    print(f"\nAnda memilih: {jenis_daging['jenis_daging'].upper()}")
    
    while True:
        try:
            kg = float(input(f"Berapa Kg yang ingin dibeli? "))
            if kg > 0:
                harga_total = kg * jenis_daging['harga_per_kg']
                print(f"✓ Daging {jenis_daging['jenis_daging']}: {kg} Kg x Rp{jenis_daging['harga_per_kg']:,} = Rp{harga_total:,}")
                return kg, harga_total
            else:
                print("⚠ Jumlah Kg harus lebih dari 0!")
        except ValueError:
            print("⚠ Input tidak valid! Masukkan angka.")


def tanya_daging_tambahan():
    """Fungsi untuk menanyakan apakah ingin membeli daging tambahan (Step 3)"""
    while True:
        jawab = input("\nApakah ingin membeli daging tambahan? (ya/tidak): ").lower()
        if jawab in ['ya', 'tidak']:
            return jawab == 'ya'
        else:
            print("⚠ Input tidak valid! Ketik 'ya' atau 'tidak'.")


def tanya_jasa_potong(jenis_daging):
    """Fungsi untuk menanyakan apakah ingin jasa potong (Step 4 & 5)"""
    print(f"\nJasa Potong untuk {jenis_daging['jenis_daging'].upper()}:")
    
    # Tentukan jenis potong berdasarkan daging
    jenis_map = {
        'ayam': 'potong_ayam',
        'sapi': 'potong_sapi',
        'kalkun': 'potong_kalkun'
    }
    
    jenis_potong_key = jenis_map.get(jenis_daging['jenis_daging'].lower())
    
    # Cari harga jasa potong
    for jp in jasa_potong:
        if jp['jasa_potong'] == jenis_potong_key:
            harga_jasa = jp['harga']
            break
    
    print(f"Harga jasa potong: Rp{harga_jasa:,}")
    
    while True:
        jawab = input(f"Ingin jasa potong? (ya/tidak): ").lower()
        if jawab in ['ya', 'tidak']:
            if jawab == 'ya':
                return harga_jasa
            else:
                return 0
        else:
            print("⚠ Input tidak valid! Ketik 'ya' atau 'tidak'.")


def hitung_total_pembayaran(pembelian_list, jasa_list):
    """Fungsi untuk menghitung total harga pembelian dan jasa"""
    total_barang = 0
    total_jasa = 0
    
    # Hitung total barang
    for pembelian in pembelian_list:
        total_barang += pembelian['harga_total']
    
    # Hitung total jasa
    total_jasa = sum(jasa_list)
    
    total_pembayaran = total_barang + total_jasa
    
    return total_barang, total_jasa, total_pembayaran


def tampilkan_nota_pembayaran(pembelian_list, jasa_list, total_barang, total_jasa, total_pembayaran):
    """Fungsi untuk menampilkan nota pembayaran (Step 6)"""
    print("\n" + "="*60)
    print(" "*15 + "NOTA PEMBAYARAN KASIR DAGING")
    print("="*60)
    
    print("\nDETAIL PEMBELIAN:")
    print("-" * 60)
    no = 1
    for pembelian in pembelian_list:
        print(f"{no}. {pembelian['jenis'].upper()}")
        print(f"   Berat: {pembelian['kg']} kg @ Rp{pembelian['harga_per_kg']:,}/kg")
        print(f"   Subtotal: Rp{pembelian['harga_total']:,}")
        print()
        no += 1
    
    print("-" * 60)
    print(f"Total Barang: Rp{total_barang:,}")
    
    if jasa_list and any(jasa_list):
        print("\nDETAIL JASA POTONG:")
        print("-" * 60)
        no = 1
        for idx, jasa in enumerate(jasa_list):
            if jasa > 0:
                print(f"{no}. {pembelian_list[idx]['jenis'].upper()} - Rp{jasa:,}")
                no += 1
        print(f"Total Jasa: Rp{total_jasa:,}")
        print("-" * 60)
    
    print(f"TOTAL PEMBAYARAN: Rp{total_pembayaran:,}")
    print("="*60)


def hitung_kembalian(total_pembayaran):
    """Fungsi untuk menghitung kembalian uang (Step 7)"""
    print(f"\nTotal yang harus dibayar: Rp{total_pembayaran:,}")
    
    while True:
        try:
            uang_bayar = int(input("Uang yang dibayarkan (nominal): Rp"))
            if uang_bayar >= total_pembayaran:
                kembalian = uang_bayar - total_pembayaran
                print("\n" + "="*60)
                print("DETAIL PEMBAYARAN:")
                print("-" * 60)
                print(f"Total Pembayaran: Rp{total_pembayaran:,}")
                print(f"Uang Dibayarkan:  Rp{uang_bayar:,}")
                print(f"Kembalian:        Rp{kembalian:,}")
                print("="*60)
                
                if kembalian > 0:
                    print("\n✓ TERIMA KASIH! Selamat berbelanja lagi!")
                else:
                    print("\n✓ TERIMA KASIH! Pas pembayaran.")
                
                return kembalian
            else:
                kekurangan = total_pembayaran - uang_bayar
                print(f"⚠ Uang kurang! Kekurangan: Rp{kekurangan:,}")
        except ValueError:
            print("⚠ Input tidak valid! Masukkan angka nominal uang.")


def jalankan_kasir():
    """Fungsi utama untuk menjalankan sistem kasir (Main Program)"""
    print("\n" + "="*60)
    print(" "*15 + "SELAMAT DATANG DI KASIR DAGING")
    print("="*60)
    
    pembelian_list = []  # List untuk menyimpan semua pembelian
    jasa_list = []       # List untuk menyimpan jasa potong
    
    # Step 1-3: Loop pembelian daging
    lanjut = True
    while lanjut:
        # Step 1: Pilih daging
        daging_pilih = pilih_daging()
        
        # Step 2: Masukkan jumlah Kg
        kg, harga_total = masukkan_jumlah_kg(daging_pilih)
        
        # Simpan pembelian
        pembelian_list.append({
            'jenis': daging_pilih['jenis_daging'],
            'kg': kg,
            'harga_per_kg': daging_pilih['harga_per_kg'],
            'harga_total': harga_total
        })
        
        # Step 3: Tanya daging tambahan
        lanjut = tanya_daging_tambahan()
    
    # Step 4-5: Tanya jasa potong untuk setiap daging yang dibeli
    for pembelian in pembelian_list:
        # Buat dict daging untuk digunakan di fungsi tanya_jasa_potong
        daging_dict = next((d for d in daftar_daging if d['jenis_daging'] == pembelian['jenis']), None)
        jasa_harga = tanya_jasa_potong(daging_dict)
        jasa_list.append(jasa_harga)
    
    # Step 6: Hitung total dan tampilkan nota
    total_barang, total_jasa, total_pembayaran = hitung_total_pembayaran(pembelian_list, jasa_list)
    tampilkan_nota_pembayaran(pembelian_list, jasa_list, total_barang, total_jasa, total_pembayaran)
    
    # Step 7: Hitung kembalian
    hitung_kembalian(total_pembayaran)


# Main Program
if __name__ == '__main__':
    jalankan_kasir()
    
    # Tanya apakah ingin membuat transaksi baru
    while True:
        lagi = input("\n\nIngin melakukan transaksi baru? (ya/tidak): ").lower()
        if lagi == 'ya':
            jalankan_kasir()
        elif lagi == 'tidak':
            print("\n" + "="*60)
            print("TERIMA KASIH! Sampai jumpa lagi!")
            print("="*60 + "\n")
            break
        else:
            print("⚠ Input tidak valid!")