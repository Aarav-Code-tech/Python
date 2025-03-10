file=open("UFO.txt","w")
file1=open("Aarav2.txt","r")
a=set()
for i in file1:
    if i not in a:
        a.add(i)
        file.write(i)

print(a)
file.close()
file1.close()