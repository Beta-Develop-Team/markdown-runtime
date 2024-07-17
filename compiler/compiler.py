import os


print("Please save your files in the code/ directory")

# Going with your method of asking for the name.
# Another and better method would to use arguments
# when running. For example: 'python3 compiler.py hello.markdownruntime'.
while True:
    name = input("Enter the file name: ")
    if name.endswith(".markdownruntime"):
        break

# Save a few keystrokes by combining
os.chdir("../code")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


with open(name, "r") as f:
    line = f.readline()
    if line.startswith("#"):
        print(line.lstrip("#"))
