def isnumprime():
  prime = True
  num = int(input("Enter the number: "))
  if num <= 1:
    prime = False
    print ("number is not prime as it is 1 or negative")
  else:
    for i in range (2,num-1):
      if num%i == 0:
        print("number is not prime, divisble by ", i,",", i, "X", int(num/i))
        prime = False
        break
  if prime == True:
    print ("number is prime")

isnumprime()
    
