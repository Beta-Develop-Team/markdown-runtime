import os
print("Please save your files in the code/ directory")
name = input("Enter the file name: ")
os.chdir("..")
os.chdir("code")
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
with open(name, "r") as f:
    line = f.readline()
    if line.startswith("#"):
        print(line.lstrip("#"))