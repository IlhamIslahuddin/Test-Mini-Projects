def insertion_sort(list):
    for i in range (1,len(list)):
        position = i
        buffer = 0
        current_value = list[position]
        while position>0 and list[position-1]>current_value:
            buffer = list[position-1]
            list[position-1] = current_value
            list[position] = buffer
            position -= 1
    return (list)
        

if __name__ == "__main__":
    array = [1,3,624,2,423,652,43,234567,2,44,1,65,65324,74,14,55653,334,454342,677654,65342,42,52,35,46345,25,6,435,1]
    ans = insertion_sort(array)
    print (ans)
