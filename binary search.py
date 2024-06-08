def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1
    # If the element is not present in the array
    return -1

if __name__ == "__main__":
    array = [2, 3, 4, 6,7,9, 10, 40,55,60,901,1009]
    target = 901
    result = binary_search(array, target)
    if result != -1:
     print("Target is at index", result)
    else:
       print("Target is not in array")
