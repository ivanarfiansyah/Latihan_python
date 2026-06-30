import json

def muat_daftar_menu ():
    with open('daftar_menu.json', 'r') as file:
        data = json.load(file)
    return data['daftar_daging'], data['jasa_potong']

harga_daging, harga_jasa = muat_daftar_menu()
def tampilkan_menu():
    print("Daftar Harga Daging:")
    for jenis, info in harga_daging.items():
        print(f"{info['jenis_daging'].capitalize()}: Rp {info['harga_per_kg']} per Kg")
    print("\nDaftar Harga Jasa Potong:")
    for jasa, info in harga_jasa.items():
        print(f"{info['jasa_potong'].replace('_', ' ').capitalize()}: Rp {info['harga']}")
        
print(" MONGGOH DIBELI DAGINGNYA ")
print("Beli Daging Apa:", ", ".join(harga_daging.keys()))
print("Ketik 'cukup' jika sudah selesai belanja.\n")

# 2. PERULANGAN (WHILE LOOP) 
while True:
    jenis = input("Mau Beli Daging Apa Lagi? ").lower()

    # Cek Pembeli Mau Beli lagi atau tidak
    if jenis == "cukup":
        break