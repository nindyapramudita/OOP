class Sepatu: #template/blueprint sepatu
    def __init__(self, nama, warna, ukuran, harga, stock, terjual): #inisial
        #variabel intance/ variabel object
        self.nama = nama #atribut
        self.warna = warna
        self.ukuran = ukuran
        self.harga = harga
        self.stock = stock
        self.terjual = terjual

class Pendataan_sepatu: #template/blueprint pendataan sepatu
    def __init__(self): #inisial
        self.data_sepatu = [] #list data

    def tambah_data(self, nama, warna, ukuran, harga, stock, terjual): #method tambah data
        sepatu_baru = Sepatu(nama, warna, ukuran, harga, stock, terjual) #objek
        self.data_sepatu.append(sepatu_baru) #cara tambahkan data kedalam list
        print("Selamat data sepatu berhasil ditambahkan!\n")

    def tampilkan_data(self): #method tampilkan data sepatu yang ada
        if self.data_sepatu: #jika list sepatu
            for id_sepatu, sepatu in enumerate(self.data_sepatu, start=1): #buat id sepatunya biar mudah dicari
                print(f"ID: {id_sepatu}, Nama: {sepatu.nama}, Warna: {sepatu.warna}, Ukuran: {sepatu.ukuran}, Harga: {sepatu.harga}, Stock: {sepatu.stock}, Terjual: {sepatu.terjual}\n")#tampilan datanya
        else:
            print("Maaf belum ada data sepatu!\n") #ini notif kalau belum ada data sama sekali di list 

    def update_data(self, id_sepatu, field, value): #method untuk update datanya
        if 1 <= id_sepatu <= len(self.data_sepatu): #ini untuk periksa id yang dimasukkan itu ada pada jumlah data sepatu yang ada apa ngga.
            sepatu = self.data_sepatu[id_sepatu - 1] #ini id sepatu yang dimasukkan user dikurangi 1. biar sesuai dengan indexnya. kan index mulai dari 0
            if hasattr(sepatu, field): #hasattr ini untuk memeriksa apakah atribut sepatu ini sesuai dengan variabel yang tersimpan.
                setattr(sepatu, field, value) #setattr untuk mengubah nilai dari atribut object.
                print("Selamat data berhasil diupdate!\n")
            else:
                print("Maaf field tidak ada!\n")
        else:
            print("Maaf ID sepatu tidak valid!\n")

    def hapus_data(self, id_sepatu): #method hapus data
        if 1 <= id_sepatu <= len(self.data_sepatu): #ini untuk periksa id yang dimasukkan use itu ada pada jumlah data sepatu yang ada apa ngga.
            del self.data_sepatu[id_sepatu - 1] #ini id sepatu yang dimasukkan user dikurangi 1. biar sesuai dengan indexnya. kan index mulai dari 0
            print("Selamat data sepatu berhasil dihapus!\n")
        else:
            print("Maaf ID sepatu tidak valid!\n")

def menu_tampilan(): #funtion untuk _tampilan dan inputannya
    pendataan = Pendataan_sepatu() #variabel yang isinya class

    while True: #perulangan
        print("\n=================================")#judulnya
        print("  Welcome to King Shoes Branded ")
        print("     Owner Nindya Pramudita     ")
        print("=================================")
        print("1. Tambah Data Sepatu") #menunya
        print("2. Tampilkan Data Sepatu")
        print("3. Update Data Sepatu")
        print("4. Hapus Data Sepatu")
        print("5. Keluar")
        print("=================================")
        pilihan = input("Pilih Menu Yang tersedia: ") #inputan menu

        if pilihan == "1": 
            print("\n===========TAMBAH DATA===========")
            nama = input("Masukkan nama sepatu: ")
            warna = input("Masukkan warna sepatu: ")
            ukuran = int(input("Masukkan ukuran sepatu: "))
            harga = int(input("Masukkan harga sepatu: "))
            stock = int(input("Masukkan jumlah stock sepatu: "))
            terjual = int(input("Masukkan jumlah sepatu yang sudah terjual: "))
            pendataan.tambah_data(nama, warna, ukuran, harga, stock, terjual) #ini biar data masuk kedalam method tambah data

        elif pilihan == "2":
            print("\n===========DATA SEPATU===========")
            pendataan.tampilkan_data() #menampilkan data

        elif pilihan == "3":
            print("\n=======UPDATE DATA SEPATU=======")
            id_sepatu = int(input("Masukkan ID sepatu yang akan diupdate: ")) #inputan update
            field = input("Masukkan field yang akan diupdate (nama/warna/ukuran/harga/stock/terjual): ") #ini field yang berhubungan dengan hasattr
            value = input("Masukkan nilai baru: ") # ini value yang berhubungan dengan settatr
            pendataan.update_data(id_sepatu, field, value) #ini biar data yang diupdate masuk kedalam method update data

        elif pilihan == "4":
            id_sepatu = int(input("Masukkan ID sepatu yang akan dihapus: "))
            pendataan.hapus_data(id_sepatu) #cara hapus data

        elif pilihan == "5":
            print("Program selesai.")
            break #stop perulangan

        else:
            print("Pilihan tidak ada. Silakan coba lagi!")


menu_tampilan()
