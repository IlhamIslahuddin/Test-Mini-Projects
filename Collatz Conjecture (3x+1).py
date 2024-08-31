import time
##Note: Output may reach terminal max lines
def Collatz_Conjecture():
    print ("______________________________________________________________________________________________________________________________________________________")
    print ("Collatz Conjecture AKA 3x+1: Asks whether repeating two arithmetic operations will eventually transform every positive integer into the number 1.")
    print ("If the number, x, is odd: apply the operation 3x + 1.")
    print ("If the number, x, is even: apply the operation x / 2.")
    print ("______________________________________________________________________________________________________________________________________________________")
    time.sleep(2)
    operations = 0
    valid = False
    counter = 1
    while valid == False:
        try:
            num = int(input("!Input a positive integer: "))
            while num <= 0 or num % 1 != 0:
                print ("!Number inputted was not a positive integer.")
                num = int(input("!Input a positive integer: "))
            valid = True
        except:
            print ("!Number inputted was not a positive integer.")
    for i in range(9999999999999999999):
        if counter == 2:
            print (f"{num} / 2 =")
            num = num // 2
            print (f"[{num}]")
            operations += 1
            print ("~~1 has been reached twice, proving that a loop will continue and that the positive integer inputted has reached 1.~~")
            print (f"Reached 1 after {operations} operations")
            break
        elif num == 1:
            counter += 1
            print (f"3({num}) + 1 =")
            num = (num*3) + 1
            print (f"[{num}]")
            operations += 1
        if num % 2 == 0:
            print (f"{num} / 2 =")
            num = num // 2
            print (f"[{num}]")
            operations += 1
        elif num % 2 == 1:
            print (f"3({num}) + 1 =")
            num = (num*3) + 1
            print (f"[{num}]")
            operations += 1
        elif num == 1:
            counter += 1
            print (counter, "counter")
            print (f"3({num}) + 1 =")
            num = (num*3) + 1
            print (f"[{num}]")
            operations += 1

if __name__ == "__main__":
    Collatz_Conjecture()
