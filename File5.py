File=open("Aarav1.txt","a")
File.write("Operations on file handling")
File.write("\nAarav1.txt in append mode")
File.write("\nCricket")
File.close()
File=open("Aarav1.txt","r")
print(File.read(8))
