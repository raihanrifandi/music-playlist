import random
import os

class Lagu:
    def __init__(self, genre, judul, artis, durasi, priority):
        self.genre = genre 
        self.judul = judul 
        self.artis = artis 
        self.durasi = durasi
        self.priority = priority

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = current

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            temp.next = None
            return temp.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            if current.prev is not None:
                current.prev.next = None
            else:
                self.head = None
            current.prev = None
            return current.data

class PlaylistPlayer:
    def __init__(self):
        self.queue = DoublyLinkedList()
        self.stack = DoublyLinkedList()
        self.deque = DoublyLinkedList()
        self.genre_dict = {}
        self.current_song = None
        
    def add_song(self, genre, judul, artis, durasi):
        priority = self._get_next_priority()
        lagu_baru = Lagu(genre, judul, artis, durasi, priority)
        self.queue.insert_at_end(lagu_baru)
        self.stack.insert_at_end(lagu_baru)
        self.deque.insert_at_end(lagu_baru)
        self._update_genre_dict(genre, lagu_baru)

    def _get_next_priority(self):
        current = self.stack.head
        max_priority = 0
        while current:
            if current.data.priority > max_priority:
                max_priority = current.data.priority
            current = current.next
        return max_priority + 1

    def shuffle_songs(self):
        songs = []
        current = self.queue.head
        while current:
            songs.append(current.data)
            current = current.next
        random.shuffle(songs)
        current = self.queue.head
        for song in songs:
            current.data = song
            current = current.next

    def play_songs(self):
        if not self.queue.is_empty():
            print("Now playing:", self.queue.head.data.judul)
        else:
            print("No songs in the playlist.")

    def sort_by_newest(self):
        songs = []
        current = self.stack.head
        while current:
            songs.append(current.data)
            current = current.next
        songs.sort(key=lambda x: x.priority, reverse=True)
        # Rebuild the stack with sorted songs
        self.stack = DoublyLinkedList()
        for song in songs:
            self.stack.insert_at_end(song)

    def sort_by_oldest(self):
        songs = []
        current = self.stack.head
        while current:
            songs.append(current.data)
            current = current.next
        songs.sort(key=lambda x: x.priority)
        self.stack = DoublyLinkedList()
        for song in songs:
            self.stack.insert_at_end(song)

    def next_song(self):
        if self.current_song is None:
            self.current_song = self.queue.head
        else:
            if self.current_song.next is None:
                self.current_song = self.queue.head
            else:
                self.current_song = self.current_song.next

        if self.current_song is not None:
            print("Now playing:", self.current_song.data.judul)
        else:
            print("No more songs in the playlist.")
    
    def previous_song(self):
        if self.current_song is None:
            print("No previous song in the playlist.")
        else:
            self.current_song = self.current_song.prev

            if self.current_song is not None:
                print("Now playing:", self.current_song.data.judul)
            else:
                print("No previous song in the playlist.")
        
    def display_stack(self):
        current = self.stack.head
        while current:
            print("Genre:", current.data.genre)
            print("Judul:", current.data.judul)
            print("Artis:", current.data.artis)
            print("Durasi:", current.data.durasi, "menit")
            print("=" * 25)
            current = current.next

    def _update_genre_dict(self, genre, song):
        if genre not in self.genre_dict:
            self.genre_dict[genre] = DoublyLinkedList()
        self.genre_dict[genre].insert_at_end(song)

    def search_by_genre(self, genre):
        if genre in self.genre_dict:
            current = self.genre_dict[genre].head
            while current:
                print("Genre:", current.data.genre)
                print("Judul:", current.data.judul)
                print("Artis:", current.data.artis)
                print("Durasi:", current.data.durasi, "menit")
                print("=" * 25)
                current = current.next
        else:
            print("No songs found in the genre:", genre)

p = PlaylistPlayer()
os.system('cls')
# file = open("header.txt", "r")
# print(file.read())

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
        while True:
            print("1. Play current song")
            print("2. Play next song")
            print("3. Play previous song")
            print("4. Back to menu")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                p.play_songs()
            elif choice == 2:
                p.next_song()
            elif choice == 3:
                p.previous_song()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    elif pilihan == "2":
        os.system('cls')
        p.display_stack()
        choice = input("Sort by oldest or newest (1/2)\nX to go back to the main menu: ")
        if choice == "1":
            p.sort_by_oldest()
            
        elif choice == "2":
            p.sort_by_newest()
           
        elif choice == 'X':
            continue
        else:
            print("Masukkan input yang sesuai")

    elif pilihan == "3":
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

    elif pilihan == "5":
        os.system('cls')
        genre_lagu = input("Genre lagu yang ingin dicari: ")
        p.search_by_genre(genre_lagu)

    elif pilihan == "6":
        break

    else:
        print("Input yang anda masukkan tidak sesuai, silahkan coba lagi")
