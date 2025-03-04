File1=open("Aarav1.txt","r")
File2=open("Aarav2.txt","w")

for i in File1:
    if not(i.startswith("Aarav1")):
        File2.write(i)


File1.close()
File2.close()
File2=open("Aarav2.txt","r")
print(File2.read())

