File=open("Aarav1.txt","r")
File2=open("nef.txt","w")
for i in range(1,len(File.readlines())+1):
    if i%2==0:
        File2.write(str(i))
File.close()
File2.close()
File2=open("nef.txt","r")
print(File2.read())
File2.close()

