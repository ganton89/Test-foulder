with open("caperucita.txt", "r") as file:
    content = file.read().strip()
    lines = content.count() + 1
    print(lines)    

