#fizzbuzz interview question
#numbers 1 to 100
#if the number is a multiple of 5 print fizz
#if the number is a multiple of 7 print buzz
#if the number is a multiple of 5 and 7 print fizzbuzz

for i in range (1,100):
    if i % 5 == 0 and i % 7 == 0:
        print (i,"fizzbuzz")
    elif i % 5 == 0:
        print (i,"fizz")
    elif i % 7 == 0:
        print (i,"buzz")
    else:
        print (i)
