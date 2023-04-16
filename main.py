# Memanggil modul Cashier
from cashier import Cashier
cashier = Cashier()

# Memanggil fungsi untuk welcome_page
cashier.welcome_page()
cashier.print_name()

cancel_transaction = False
while True:
    '''
    Melakukan looping untuk penambahan barang sampai jadi list final yang sudah siap
    untuk dihitung total harga dengan diskon
    '''
    cashier.add_item()

    sesuai = input('Apakah barang yang Anda masukkan sudah sesuai? (ya/tidak)')
    if sesuai.lower() == "ya":
        cashier.show_current_item()
    elif sesuai.lower() == "tidak":
        print("1. Ubah nama item yang dibeli\n2. Ubah jumlah item yang dibeli\n3. Ubah harga item yang dibeli\n4. Hapus item\n5. Batalkan transaksi")

        menu = int(input('Menu apa yang ingin dipilih?'))
        if menu == 1:
            existing_name = input('Masukkan nama item yang ingin diubah: ')
            new_name = input('Masukkan nama item yang baru: ')
            cashier.edit_name(existing_name,new_name)
        elif menu == 2:
            try: 
                item_name = input('Masukkan nama item yang ingin diubah jumlahnya: ')
                new_qty = int(input('Masukkan jumlah item yang baru: '))
                cashier.edit_qty(item_name, new_qty)
            except:
                print("Input yang Anda masukkan tidak sesuai")
        elif menu == 3:
            try: 
                item_name = input('Masukkan nama item yang ingin diubah harganya: ')
                new_price = float(input('Masukkan harga item yang baru: Rp '))
                cashier.edit_price(item_name, new_price)
            except:
                print("Input yang Anda masukkan tidak sesuai")
        elif menu == 4:
            item_name = input('Masukkan nama item yang ingin dihapus: ')
            cashier.remove_item(item_name)
        elif menu == 5:
            cashier.cancel_transaction()
            cancel_transaction = True
            break
    print("Input yang Anda masukkan salah")    

    selesai = input('Apakah Anda ingin menyelesaikan transaksi Anda? (ya/tidak)')
    if selesai.lower() == "ya":
        break
        
if cancel_transaction == False:
    '''
    melakukan pengecekan & perhitungan diskon
    '''
    total = 0
    for item in cashier.items:
        total += item[1]*item[2]
    if total > 500_000:
        total = total * 0.90
        print(f'Anda telah berbelanja lebih dari Rp 500.000, Anda mendapatkan diskon 10%.\nTotal yang harus dibayarkan Rp {total}')
    elif total > 300_000:
        total = total * 0.92
        print(f'Anda telah berbelanja lebih dari Rp 300.000, Anda mendapatkan diskon 8%.\nTotal yang harus dibayarkan Rp {total}')
    elif total > 200_000:
        total = total * 0.95
        print(f'Anda telah berbelanja lebih dari Rp 500.000, Anda mendapatkan diskon 5%.\nTotal yang harus dibayarkan Rp {total}')
    else:
        print(f'Total yang harus dibayarkan Rp {total}')