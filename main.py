import random
import os

class Lagu:
    def __init__(self, genre, judul, artis, durasi):
        self.genre = genre # kategori 1
        self.judul = judul 
        self.artis = artis 
        self.durasi = durasi
        self.priority = random.random()  

    def __lt__(self, other):
        return self.priority < other.priority

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data
    
class PlaylistPlayer:
    def __init__(self):
        self.queue = LinkedList()
        self.stack = LinkedList()
        self.deque = LinkedList()
        self.genre_dict = {}
        self.genre_bst = None
        
    def add_song(self, genre, lagu, artis, durasi):
        lagu_baru = Lagu(genre, lagu, artis, durasi)
        self.queue.insert_at_end(lagu_baru)
        self.stack.insert_at_end(lagu_baru)
        self.deque.insert_at_end(lagu_baru)
        self._update_genre_dict(genre, lagu_baru)
        self._update_genre_bst(genre)

    def shuffle_songs(self):
        # Convert linked list to list for shuffling
        songs = []
        current = self.queue.head
        while current:
            songs.append(current.data)
            current = current.next
        random.shuffle(songs)
        # Rebuild the queue with shuffled songs
        self.queue = LinkedList()
        for song in songs:
            self.queue.insert_at_end(song)

    def play_songs(self):
        current = self.queue.head
        while current:
            print("Now playing:", current.data.judul)
            current = current.next

    def sort_by_newest(self):
        # Convert linked list to list for sorting
        songs = []
        current = self.stack.head
        while current:
            songs.append(current.data)
            current = current.next
        songs.sort(key=lambda x: x.priority, reverse=True)
        # Rebuild the stack with sorted songs
        self.stack = LinkedList()
        for song in songs:
            self.stack.insert_at_end(song)

    def sort_by_oldest(self):
        # Convert linked list to list for sorting
        songs = []
        current = self.stack.head
        while current:
            songs.append(current.data)
            current = current.next
        songs.sort(key=lambda x: x.priority)
        # Rebuild the stack with sorted songs
        self.stack = LinkedList()
        for song in songs:
            self.stack.insert_at_end(song)

    def play_next_song(self):
        if not self.deque.is_empty():
            song = self.deque.delete_at_beginning()
            self.deque.insert_at_end(song)
            print("Now playing:", song.judul)
        else:
            print("No next song in the queue.")

    def play_previous_song(self):
        if not self.deque.is_empty():
            current = self.deque.head
            prev = None
            while current.next:
                prev = current
                current = current.next
            if prev:
                prev.next = None
                self.deque.head = current
                current.next = self.deque.head
                print("Now playing:", current.data.judul)
            else:
                print("No previous song in the queue.")
                
    def display_stack(self):
        current = self.stack.head
        while current:
            print("Genre :", current.data.genre)
            print("Judul :", current.data.judul)
            print("Artis :", current.data.artis)
            print("Durasi:", current.data.durasi, "menit")
            print("="*25)
            current = current.next
            
    def _update_genre_dict(self, genre, song):
        if genre not in self.genre_dict:
            self.genre_dict[genre] = LinkedList()
        self.genre_dict[genre].insert_at_end(song)
    
    def _update_genre_bst(self, genre):
        if self.genre_bst is None:
            self.genre_bst = BinarySearchTree(genre)
        else:
            self.genre_bst.insert(genre)
    
    def search_by_genre(self, genre):
        genre = genre.lower()
        if genre in self.genre_dict:
            current = self.genre_dict[genre].head
            while current:
                print("Genre :", current.data.genre)
                print("Judul :", current.data.judul)
                print("Artis :", current.data.artis)
                print("Durasi:", current.data.durasi, "menit")
                print("="*25)
                current = current.next
        else:
            print("No songs found in the genre:", genre)

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)
            
p = PlaylistPlayer()
os.system('cls')
file = open("header.txt", "r")
print(file.read())

while True:
    print("Menu Utama")
    print("[1] Memainkan lagu")
    print("[2] Melihat daftar lagu")
    print("[3] Menambahkan lagu")
    print("[4] Menghapus lagu")
    print("[5] Mencari lagu")
    print("[6] Keluar")
    pilihan = input("Masukkan pilihan menu: ")

    if pilihan == "1":
        os.system('cls')
        p.play_songs
    
    elif pilihan == "2":
            os.system('cls')
            p.display_stack()
            choice = input("Sort by newest or oldest (1/2)\nX to back to main menu: ")
            if choice == "1":
                p.sort_by_newest()
            elif choice == "2":
                p.sort_by_oldest()
            else:
                print("Masukkan input yang sesuai")
            
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
        p.add_song(genre, judul, artis, durasi)
    
    elif pilihan == "4":
        os.system('cls')
        hapus_lagu = input("Judul lagu yang ingin dihapus: ")
        # Menghapus spesifik lagu dari stack, queue, dan deque
        
    elif pilihan == "5":
        os.system('cls')
        genre_lagu = input("Genre lagu yang ingin dicari: ")
        p.search_by_genre(genre_lagu)
        # Mencari lagu berdasarkan genre

    elif pilihan == "6":
        break
        # Keluar dari program
    
    else:
        print("Input yang anda masukkan tidak sesuai, silahkan coba lagi")
  
