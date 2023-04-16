class Cashier:
    def welcome_page(self):
        '''
        to show welcome page
        '''
        print('-----------------------------------------------------------')
        print('-------------- Selamat Datang di Supermarket --------------')
        print('------------------  Self Service Cashier ------------------')
        print('-----------------------------------------------------------')
        
    def print_name(self):
        '''
        to print customer name as transaction ID
        '''
        name = input("Masukkan nama Anda: ")
        print(f'Hai, {name}! Silakan lakukan self service cashier untuk belanjaan Anda')
    
    def __init__(self):
        '''
        sebagai penampung item belanja
        '''
        self.items = []
        
        
    def add_item(self):
        '''
        Fungsi looping untuk menambahkan item ke dalam list.

        Params: item,jumlah, dan harga.
        '''
        list = []
        while True:
            # add = input("Apakah Anda ingin menambahkan item ke dalam list belanja? (ya/tidak)")
            if len(list) != 0:
                add = input("Apakah Anda ingin menambahkan item ke dalam list belanja lagi? (ya/tidak)")
            else:
                add = "ya"

            if add.lower() == 'tidak':
                break
            elif add.lower() == "ya":
                name = input("Masukkan barang belanja Anda: ")
                qty = int(input("Masukkan jumlah item: "))
                price = float(input("Masukkan harga item: Rp "))
                added_item = [name, qty, price]
                list.append(added_item)
                print(f"{name} dengan jumlah {qty} dan harga per item Rp {price} berhasil ditambahkan ke keranjang")
            else:
                print("Jawaban tidak sesuai, Anda harus memilih ya / tidak")

        self.items = list
        self.show_current_item()
    
    def show_current_item(self):
        '''
        untuk menunjukkan item apa saja yang sudah diinput
        '''
        print('='*82)
        print("Nama barang\t\tQuantity\t\tHarga barang\t\tSub Total")
        print('='*82)
        if len(self.items) == 0:
            print("-\t\t\t-\t\t\t-\t\t\t-")
        for list in self.items:
            sub_total = list[1]*list[2]
            print("{}\t\t\t{}\t\t\t{}\t\t\t{}".format(list[0], list[1], list[2], sub_total))
    
    def edit_name(self, existing_name, new_name):
        '''
        fungsi untuk edit nama item.
        '''
        for item in self.items:
            if item[0]== existing_name:
                item[0]= new_name
        self.show_current_item()
        
    def edit_qty(self, item_name, new_qty):
        '''
        fungsi untuk edit quantity item
        '''
        for item in self.items:
            if item[0]== item_name:
                item[1]= new_qty
        self.show_current_item()
        
    def edit_price(self, item_name, new_price):
        '''
        fungsi untuk edit harga item
        '''
        for item in self.items:
            if item[0]== item_name:
                item[2]= new_price
        self.show_current_item()
    
    def cancel_transaction(self):
        '''
        fungsi untuk membatalkan semua transaksi.
        jika transaksi dibatalkan, maka user akan mengakhiri proses self service cashier
        '''
        self.items = []
        print("Anda telah membatalkan transaksi")
        self.show_current_item()
        
    def remove_item(self, item_name):
        '''
        fungsi untuk menghapus item tertentu
        '''
        for item in self.items:
            if item[0]== item_name:
                self.items.remove(item)
        print(f"Anda telah menghapus {item_name} dari daftar belanja")
        self.show_current_item()