import os
file = open("NEfile.txt","x")

if os.path.exists("nef.txt"):
    os.remove("nef.txt")
    print("File Removed")
    