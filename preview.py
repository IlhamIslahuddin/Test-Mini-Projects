def Preview(file_name,num_lines):
    opened = open(file_name,"r")
    for i in range (num_lines):
        line = str((opened.readlines(1)))
        cleaned = str(line[2:(len(line)-4)])
        print (cleaned)

if __name__ == "__main__":
    Preview("text.txt",5)
