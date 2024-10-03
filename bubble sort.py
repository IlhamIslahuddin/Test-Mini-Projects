array = [6,26,4,43,2,22,2,34,4,5,2,33,5,7,6,5,4567]

def sort(array_to_sort):
    noSwaps = False
    for i in range(len(array_to_sort)):
        noSwaps = True
        for j in range(len(array_to_sort)-1):
            if array_to_sort[j] > array_to_sort[j+1]:
                noSwaps = False
                temp = array_to_sort[j]
                array_to_sort[j] = array_to_sort[j+1]
                array_to_sort[j+1] = temp
        if noSwaps == True:
            return array_to_sort
            

if __name__ == "__main__":
    print (sort(array))
