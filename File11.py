file=open("Aarav.txt","r")
file1=open("Aarav2.txt","r")
file2=open("NEfile.txt","w")

a=file.read()
b=file1.read()
c=a+"\n"+b
file2.write(c)
file.close()
file1.close()
file2.close()
file3=open("NEfile.txt","r")
print(file3.read())
file3.close()