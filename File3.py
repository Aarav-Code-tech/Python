File=open("NE.txt","r")
a=0
Content=File.read()
split=Content.split("\n")
for i in split:
    if i :
        a+=1

print(a)