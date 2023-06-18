import os

p =  # Memanggil object class

os.system('cls')
file = open("header.txt", "r")
print(file.read())

while True:
    print("\nGo-To Playlist")
    print("[1] Memainkan lagu")
    print("[2] Melihat daftar lagu")
    print("[3] Menambahkan lagu")
    print("[4] Menghapus lagu")
    print("[5] Mencari lagu")
    print("[6] Keluar")
    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        os.system('cls')
        # Memainkan lagu berdasarkan urutan playlist
    
    elif pilihan == "2":
        os.system('cls')
        # Memanggil method untuk melihat daftar queue
        # Menyortir urutan lagu berdasarkan terbaru dan terlama nya lagu ditambahkan
        # Memainkan lagu berdasarkan preferensi urutan playlist; newest, oldest, shuffl
       
    elif pilihan == "3":
        #Menambahkan sebuah lagu ke dalam stack, queue, dan deque
        os.system('cls')
        genre = input("Genre lagu: ")
        judul = input("Judul lagu: ")
        artis = input("Nama artis: ") 
        while True:
            try:
                durasi = int(input("Durasi waktu (dalam menit): "))
            except ValueError:
                print("Masukkan input berupa angka!")
            else:
                break

        # Tambahkan method menambahkan lagu disini
    
    elif pilihan == "4":
        os.system('cls')
        hapus_lagu = input("Judul lagu yang ingin dihapus: ")
        # Menghapus spesifik lagu dari stack, queue, dan deque
        
    elif pilihan == "5":
        os.system('cls')
        judul_lagu = input("Judul lagu yang ingin dicari: ")
        # Mencari lagu berdasarkan genre, artis, atau judul

    elif pilihan == "6":
        break
        # Keluar dari program
    
    else:
        print("Input yang anda masukkan tidak sesuai, silahkan coba lagi")
