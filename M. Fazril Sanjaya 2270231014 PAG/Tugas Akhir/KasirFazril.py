menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" Selamat Datang di Warung Fazril")
    print(" Silahkan Mau Beli apa")
 
    print(" ========================================")
    print(" 1. Rokok Filter : Rp 21.500")
    print(" 2. Cerelac nesle : Rp 2.000")
    print(" 3. Rexona Pria : Rp 3.000")
    print(" 4. Kopi Hitam Manis : Rp 4.000")
    print(" 5. Rokok Filter + Kopi Hitam : Rp. 24.000")
    print(" ========================================")
    listMenu=str(input(" Masukkan angka sesuai Yang ingin Anda Beli = "))
    jumlahPesanan=int(input(" Jumlah dibeli = "))
    if listMenu == "1":
        namaMenu= " Rokok Filter "
        harga=(21500*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga=int(harga)
        else:
            totalHarga=int(harga)
    elif listMenu == "2":
        namaMenu= " Cerelac nesle "
        harga = (2000*jumlahPesanan)
        if jumlahPesanan >= 5:
            totalHarga =int(harga)
        else:
            totalHarga =int(harga)
    elif listMenu == "3":
        namaMenu= " Rexona Pria "
        harga=int(20000*jumlahPesanan)
        totalHarga=int(harga)
    elif listMenu == "4":
        namaMenu= " Kopi Hitam Manis"
        harga=int(16000*jumlahPesanan)
        totalHarga = int(harga)
    elif listMenu == "5":
        namaMenu= " Rokok Filter + Kopi Hitam "
        harga=int(17000*jumlahPesanan)
        pajak = int(harga * 0.1)
        totalHarga = int(harga)
    else:
        menu=input(" Maaf,Menu yang dipilih tidak tersedia di restoran")
 
    print(" ------------------------------")
    print(" Menu :",namaMenu)
    print(" Jumlah Pesanan :", jumlahPesanan)
    print(" Harga :", harga)
    print(" ------------------------------")
    print(" Total Pembayaran :", totalHarga)
    print(" ------------------------------")
    menu = input(" Mau pesan lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N)")
    if menu == "N"or "n":
        break
    
    
