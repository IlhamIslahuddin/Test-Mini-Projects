def DPuniquePaths(m: int, n: int) -> int:
    # Create a 2D array initialized to 1
    array = []
    for i in range(n):
        array.append(1)
    add = [array]
    array = add
    for i in range(m):
        array = array + add
    
    # Start filling the array (each point is the sum of the points directly to its left and above)
    for i in range(1, m):
        for j in range(1, n):
            array[i][j] = array[i-1][j] + array[i][j-1]
    
    return array[m-1][n-1]

if __name__ == "__main__":
    print(DPuniquePaths(23,12))
