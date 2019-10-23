lines = open("README.md", "r").readlines()

[print(line, end="") for line in lines]

print("\nEverything is OK")
