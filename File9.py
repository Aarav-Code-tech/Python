with open("Aarav1.txt","r") as file:
    a = file.readlines()
    for i in a:
        word=i.split()
        print(word)
file.close()



