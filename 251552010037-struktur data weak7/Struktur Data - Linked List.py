class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
a.next = b
b.next = c

current = a
while current:
    print(current.data)
current = current.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node("A")
b = Node("B")
c = Node("C")
a.next = b
b.next = c
current = a
while current:
    print(f"Node @ {id(current)} | Data: {current.data} | Next: {id(current.next) if current.next else None}")
current = current.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(node):
    while node:
        next_id = id(node.next) if node.next else None
        print(f"[{node.data} | {next_id}] --> ", end="")
        node = node.next
    print("NULL")

a = Node("A")
b = Node("B")
c = Node("C")
a.next = b
b.next = c
print_linked_list(a)

#Insertion di Awal (Beginning)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        def insert_at_beginning(head, data):
            new_node = Node(data)
            new_node.next = head
            return new_node

head = Node("B")
head =  insert_at_beginning (head, "A") # type: ignore
def print_linked_list(head):
    while head:
        print(f"[{head.data}] → ", end="")
        head = head.next
    print("NULL")
print_linked_list(head)

#Insertion di Akhir (End)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
head = None
head = insert_at_end(head, "A")
head = insert_at_end(head, "B")
def print_linked_list(head):
    while head:
        print(f"[{head.data}] → ", end="")
        head = head.next
    print("NULL")
print_linked_list(head)

#part 1:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node
head = Node("B")
head = insert_at_beginning(head, "A")
def print_linked_list(head):
    while head:
        print(f"[{head.data}] → ", end="")
head = head.next
print("NULL")
print_linked_list(head)

#part 2 :
def insert_after_node(prev_node, data):
    if not prev_node:
        print("Node sebelumnya tidak boleh None")
        return
    new_node = Node(data) # type: ignore
    new_node.next = prev_node.next # pyright: ignore[reportUndefinedVariable]
    prev_node.next = new_node # type: ignore
head = Node("B")
head = insert_at_beginning(head, "A")
head = insert_at_end(head, "C")
def print_linked_list(head):
    while head:
        print(f"[{head.data}] → ", end="")
        head = head.next
    print("NULL")
#part 3 :

current = head
while current and current.data != "B":
    current = current.next
insert_after_node(current, "X")

print_linked_list(head)

#Contoh Linked List 
# part 1 :
class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song # type: ignore
        print(f"Lagu '{title}' ditambahkan ke playlist.") # type: ignore
#part 2 :
def show_playlist(self):
    current = self.head
    if not current:
        print("Playlist kosong.")
        return
    print(" Playlist:")
    while current:
        print(f"- {current.title}")
        current = current.next
def play_all(self):
    current = self.head
    if not current:
        print("Tidak ada lagu untuk diputar.")
        return
    print("Memutar semua lagu:")
    while current:
        print(f" Memutar: {current.title}")
        current = current.next
#part 3 :
playlist = Playlist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")
print("\nMenampilkan playlist:")
playlist.show_playlist()
print("\nMemutar semua lagu:")
playlist.play_all()