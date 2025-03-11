class library:
    def __init__(self,books,name):
        self.books=books
        self.name=name
        self.dict = {}

    def display(self):
        print("Welcome to the",self.name)
        print("The books available are:\n")
        for i in self.books:
            print(i)

    def lendbook(self,bookname,username):
        if bookname in self.dict:
            print("Want the book? Then keep wanting someone took it wayyy before you.")
        elif bookname not in self.books:
            print("We don't have that book.Ha Ha HA no book for you")
        
        else:
            self.dict[bookname]=username
            print("Fine you can have this book. But...\n if there is a single scratch on it.\n")
            print("I will launch 200 TNTs on you")
            self.books.remove(bookname)
    def Add(self,bookname):
        self.books.append(bookname)
        print("You have your book. Now get OUT")
obj = library(["Harry Potter","Percy Jackson","Heroes of Olympus"],"Library of DEATH")
a= input("Now umm Enter your name  ")
while True:
    print("Welcome to the Library of DEATH","Press 1 for display 2 for adding books and 3 for lending books")
    b = int(input("1,2 or 3 Fast"))

    if b not in [1,2,3]:
        print("ENTER A VALID OPTION OR ELSE...")
        continue
    elif b==1:
        obj.display()
    elif b ==2:
        c = input("Which book do you want?")
        obj.Add(c)
    elif b==3:
        d = input("Which book do you want?")
        obj.lendbook(d,a)
