class Node:
    def __init__(self, sepatu=None):
        self.sepatu = sepatu
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_di_awal(self, sepatu):
        new_node = Node(sepatu)
        new_node.next_node = self.head
        self.head = new_node

    def tambah_di_akhir(self, sepatu):
        new_node = Node(sepatu)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def tambah_di_tengah(self, sepatu, posisi):
        if posisi < 0:
            print("Posisi harus lebih besar dari 0")
            return
        if posisi == 0:
            self.tambah_di_awal(sepatu)
            return
        new_node = Node(sepatu)
        curr_node = self.head
        prev_node = None
        count = 0
        while curr_node and count != posisi:
            prev_node = curr_node
            curr_node = curr_node.next_node
            count += 1
        if curr_node is None:
            print("Posisi melebihi panjang linked list")
            return
        prev_node.next_node = new_node
        new_node.next_node = curr_node

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list kosong")
            return
        self.head = self.head.next_node

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list kosong")
            return
        if not self.head.next_node:
            self.head = None
            return
        second_last = self.head
        while second_last.next_node.next_node:
            second_last = second_last.next_node
        second_last.next_node = None

    def hapus_di_tengah(self, posisi):
        if posisi < 0:
            print("Posisi harus lebih besar dari 0")
            return
        if posisi == 0:
            self.hapus_di_awal()
            return
        curr_node = self.head
        prev_node = None
        count = 0
        while curr_node and count != posisi:
            prev_node = curr_node
            curr_node = curr_node.next_node
            count += 1
        if curr_node is None:
            print("Posisi melebihi panjang linked list")
            return
        prev_node.next_node = curr_node.next_node

class Sepatu:
    def __init__(self, nama, warna, ukuran, harga, stock, terjual):
        self.nama = nama
        self.warna = warna
        self.ukuran = ukuran
        self.harga = harga
        self.stock = stock
        self.terjual = terjual

class Pendataan_sepatu:
    def __init__(self):
        self.data_sepatu = LinkedList()

    def tambah_data(self, sepatu):
        self.data_sepatu.tambah_di_akhir(sepatu)
        print("Selamat data sepatu berhasil ditambahkan!\n")

    def tampilkan_data(self):
        curr_node = self.data_sepatu.head
        while curr_node:
            sepatu = curr_node.sepatu
            print(f"Nama: {sepatu.nama}, Warna: {sepatu.warna}, Ukuran: {sepatu.ukuran}, Harga: {sepatu.harga}, Stock: {sepatu.stock}, Terjual: {sepatu.terjual}\n")
            curr_node = curr_node.next_node

    def update_data(self, posisi, field, value):
        curr_node = self.data_sepatu.head
        count = 0
        while curr_node and count != posisi:
            curr_node = curr_node.next_node
            count += 1
        if curr_node:
            sepatu = curr_node.sepatu
            if hasattr(sepatu, field):
                setattr(sepatu, field, value)
                print("Selamat data berhasil diupdate!\n")
            else:
                print("Maaf field tidak ada!\n")
        else:
            print("Maaf posisi tidak valid!\n")

    def hapus_data(self, posisi):
        self.data_sepatu.hapus_di_tengah(posisi)
        print("Selamat data sepatu berhasil dihapus!\n")

def menu_tampilan():
    pendataan = Pendataan_sepatu()

    while True:
        print("\n=================================")
        print("  Welcome to King Shoes Branded ")
        print("     Owner Nindya Pramudita     ")
        print("=================================")
        print("1. Tambah Data Sepatu")
        print("2. Tampilkan Data Sepatu")
        print("3. Update Data Sepatu")
        print("4. Hapus Data Sepatu")
        print("5. Keluar")
        print("=================================")
        pilihan = input("Pilih Menu Yang tersedia: ")

        if pilihan == "1":
            print("\n===========TAMBAH DATA===========")
            nama = input("Masukkan nama sepatu: ")
            warna = input("Masukkan warna sepatu: ")
            ukuran = int(input("Masukkan ukuran sepatu: "))
            harga = int(input("Masukkan harga sepatu: "))
            stock = int(input("Masukkan jumlah stock sepatu: "))
            terjual = int(input("Masukkan jumlah sepatu yang sudah terjual: "))
            sepatu_baru = Sepatu(nama, warna, ukuran, harga, stock, terjual)
            pendataan.tambah_data(sepatu_baru)

        elif pilihan == "2":
            print("\n===========DATA SEPATU===========")
            pendataan.tampilkan_data()

        elif pilihan == "3":
            print("\n=======UPDATE DATA SEPATU========")
            posisi = int(input("Masukkan posisi data sepatu yang akan diupdate: "))
            field = input("Masukkan atribut sepatu yang akan diupdate (nama/warna/ukuran/harga/stock/terjual): ")
            value = input("Masukkan data sepatu yang baru: ")
            pendataan.update_data(posisi, field, value)

        elif pilihan == "4":
            print("\n=======HAPUS DATA SEPATU========")
            posisi = int(input("Masukkan posisi data sepatu yang akan dihapus: "))
            pendataan.hapus_data(posisi)

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak ada. Silakan coba lagi!")


menu_tampilan()
