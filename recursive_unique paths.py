def recursive_unique_paths(m,n):
    if m == 1 or n == 1:
        return 1
    
    return recursive_unique_paths(m-1,n) + recursive_unique_paths(m,n-1)

if __name__ == "__main__":
    print (recursive_unique_paths(7,3))
