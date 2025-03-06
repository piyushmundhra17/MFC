class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book_id, title, author):
        self.books.append({'id': book_id, 'title': title, 'author': author})
        print("Book added successfully!")
    
    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    
    def update_book(self, book_id, title, author):
        for book in self.books:
            if book['id'] == book_id:
                book['title'] = title
                book['author'] = author
                print("Book updated successfully!")
                return
        print("Book not found!")
    
    def delete_book(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                print("Book deleted successfully!")
                return
        print("Book not found!")
    
    def add_member(self, member_id, name):
        self.members.append({'id': member_id, 'name': name})
        print("Member added successfully!")
    
    def view_members(self):
        if not self.members:
            print("No members available.")
        else:
            for member in self.members:
                print(f"ID: {member['id']}, Name: {member['name']}")
    
    def update_member(self, member_id, name):
        for member in self.members:
            if member['id'] == member_id:
                member['name'] = name
                print("Member updated successfully!")
                return
        print("Member not found!")
    
    def delete_member(self, member_id):
        for member in self.members:
            if member['id'] == member_id:
                self.members.remove(member)
                print("Member deleted successfully!")
                return
        print("Member not found!")

# Example usage
library = Library()
library.add_book(1, "1984", "George Orwell")
library.view_books()
library.update_book(1, "Animal Farm", "George Orwell")
library.delete_book(1)
library.add_member(101, "Alice")
library.view_members()
