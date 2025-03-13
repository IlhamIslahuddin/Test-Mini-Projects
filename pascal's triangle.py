def pascals(n):
    arr = []
    for i in range(1,n+1):
        array = [1 for _ in range(i)]
        if i > 2:
            x = 1
            while x < i-1:
                array[x] = arr[i-2][x] + arr[i-2][x-1]
                x += 1
        arr.append(array)
    print(arr)

if __name__ == "__main__":
    pascals(6)
