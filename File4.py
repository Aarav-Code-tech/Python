file1=open("NE.txt","r")
file2=open("Empty.txt","w")

a=file1.read()
file2.write(a)

file1.close()
file2.close()
Empty=open("Empty.txt","r")
print(Empty.read())