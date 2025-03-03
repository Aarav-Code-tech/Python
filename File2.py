Filer=open("NE.txt","w")
Filer.write("Non Existing.You are inside a non existing file illegally and are under arrest for um.... NOTHING")
Filer.close()

Filer=open("NE.txt","a")
Filer.write("\n Yes Uuhh.. Absolutely Nothing")
Filer.close()

Filer=open("NE.txt","r")
print(Filer.read())
Filer.close()