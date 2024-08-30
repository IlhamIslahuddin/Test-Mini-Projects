def search_monster():
    searching_for = str(input("What is the name of the monster you are looking for? "))
    lower = searching_for.lower()
    file = open("monsters simple.txt", "r")
    lines = file.readlines()
    found = False
    for line in lines:
        split = line.split(",")
        if (split[0]).lower() == lower:
            print (line)
            found = True
            break
    if found == False:
        print (f"Couldnt find a monster named {searching_for}.")
    file.close()

if __name__ == "__main__":
    search_monster()
