#Harga Awal Daging / Kg
Harga_Daging_perKg = 100000
Jumlah_total_daging = 0
Mau_beli_berapa = int(input("Masukkan jumlah daging yang ingin dibeli (dalam Kg):"))
Jumlah_total_daging += Mau_beli_berapa

Pertanyaan = "Ya"
while Pertanyaan != 'Cukup':
  
   # if Pertanyaan == 'Ya':
       
    Jumlah_total_daging  += Mau_beli_berapa 
       
    #elif Pertanyaan == 'Cukup':
        #print("Ngokheyy Hatur Nuhun")
       # break
    
    Pertanyaan = input ("Mau nambah lagi ga nih? (Ya/Cukup)")

        #Harga Daging Setelah Mendapatkan Diskon
    if Jumlah_total_daging >= 5:
        print("Anda mendapatkan diskon 7000")
        diskon = 7000
        Harga_total_setelah_diskon = Harga_total - diskon
        print("Harga total setelah diskon adalah : Rp.", Harga_total_setelah_diskon)
    elif Jumlah_total_daging >= 2:
        print("Anda mendapatkan diskon 5000")
        diskon = 5000
        Harga_total_setelah_diskon = Harga_total - diskon
        print("Harga total setelah diskon adalah : Rp.", Harga_total_setelah_diskon)
    else:
        print("Tidak ada diskon yang diberikan")
        Harga_total_setelah_diskon = Harga_total
        print("Harga total yang harus dibayar adalah : Rp.", Harga_total_setelah_diskon)
    #Jumlah_total_daging  += Mau_beli_berapa 
    Harga_total = Harga_Daging_perKg * Jumlah_total_daging
    Mau_beli_berapa = int(input("Masukkan jumlah daging tambahan yang ingin dibeli (dalam Kg):"))
    Harga_total = Harga_Daging_perKg * (Jumlah_total_daging)
#print ("Harga total yang harus dibayar adalah : Rp.", Harga_total)
print ("Harga total yang harus dibayar adalah : Rp.", Harga_total - diskon)
print ("Jumlah total daging yang dibeli adalah : ", Jumlah_total_daging, "Kg")
#Materi Looping

    