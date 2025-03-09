def recursive_sum(n):
   if n == 0:
       return n
   else:
       return n + recursive_sum(n-1)

if __name__ == "__main__":
    try:
        num = int(input("Input num: "))
        if num < 0:
            print("Please enter a positive number.")
        else:
            print("The sum of all numbers up to (inclusive) this number is",recursive_sum(num))
    except:
        print ("Error: Non-integer input")
