#this code assumes the check digit is at the end
num = int(input("Enter the number to check: "))
multiplied = []
string = str(num)
orig_num_digits = len(string) - 1
check_digit = string[orig_num_digits]
new_string = string[0:orig_num_digits]
for i in range(len(new_string)):
    x = int(string[i])*(len(string)-i)
    multiplied.append(x)
    print (multiplied)

total = 0
for i in range(len(multiplied)):
    total += multiplied[i]
print (total)
mod_11 = total%11
if (11-mod_11) == int(check_digit):
    print ("checksum is valid")
else:
    print ("checksum is invalid, check digit does not match")
