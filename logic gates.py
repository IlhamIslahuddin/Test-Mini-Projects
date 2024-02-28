#AND gate

def ANDGATE():
  print ("this is an AND gate")
  Avalue = int(input("A: "))
  Bvalue = int(input("B: "))
  if Avalue != 1 and Avalue != 0 or Bvalue != 1 and Bvalue != 0:
    return "invalid input"
  elif Avalue == 1 and Bvalue == 1:
    return True
  else:
    return False
  
print (ANDGATE()) #print helps print the true or false value

#NOT gate
def NOTGATE():
  print ("\n") #create a space inbetween for formatting
  print ("this is an NOT gate")
  NOTvalue = int(input("Value: "))
  if NOTvalue != 1 and NOTvalue != 0:
    return "invalid input"
  elif ((NOTvalue) == 1):
    return False
  else:
    return True

print (NOTGATE())

#OR gate
def ORGATE():
  print ("\n")
  print ("this is an OR gate")
  ORAvalue = int(input("A: "))
  ORBvalue = int(input("B: "))
  if ORAvalue != 1 and ORAvalue != 0 or ORBvalue != 1 and ORBvalue != 0:
    return "invalid input"
  elif ((ORAvalue) == 1) or ((ORBvalue) == 1):
    return True
  else:
    return False


print (ORGATE())

#NAND gate

def NANDGATE():
  print ("\n")
  print ("this is an NAND gate")
  NANDAvalue = int(input("A: "))
  NANDBvalue = int(input("B: "))
  if NANDAvalue != 1 and NANDAvalue != 0 or NANDBvalue != 1 and NANDBvalue != 0:
    return "invalid input"
  elif ((NANDAvalue) == 1) and ((NANDBvalue) == 1):
    return False
  else:
    return True


print (NANDGATE())

#NOR gate
def NORGATE():
  print ("\n")
  print ("this is an NOR gate")
  NORAvalue = int(input("A: "))
  NORBvalue = int(input("B: "))
  if NORAvalue != 1 and NORAvalue != 0 or NORBvalue != 1 and NORBvalue != 0:
    return "invalid input"
  elif ((NORAvalue) == 1) or ((NORBvalue) == 1):
    return False
  else:
    return True

print (NORGATE())

def XORGATE():
  print ("\n")
  print ("this is an XOR gate")
  XORAvalue = int(input("A: "))
  XORBvalue = int(input("B: "))
  if XORAvalue != 1 and XORAvalue != 0 or XORBvalue != 1 and XORBvalue != 0:
    return "invalid input"
  elif ((XORAvalue) == 1) and ((XORBvalue) == 0) or ((XORAvalue) == 0) and ((XORBvalue) == 1):
    return True
  else:
    return False

print (XORGATE())
