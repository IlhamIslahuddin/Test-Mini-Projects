##creates a dictionary from a text file
def create_dicitonary(file):
    dict = {}
    f = open(file,"r")
    lines = f.readlines()
    for line in lines:
        split = line.split(",")
        ## delimiter depends on how items are seperated
        dict[split[0]] = (split[1::])
    item = (dict.get("key", "default"))
    print (item)
    return dict
        
if __name__ == "__main__":
    create_dicitonary("file name") 
