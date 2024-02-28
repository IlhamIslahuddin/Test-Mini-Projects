#this is a simple retirement bank calculator based on an example used in an online course about python i did on coursera
working_duration = 3
working_contribution = 1000
working_ROR = 1.01
retired_duration = 2
retired_contribution = -2000
retired_ROR = 1.001

def retirement_calculator(bank):
      for i in range (working_duration):
            bank = (bank*working_ROR) + working_contribution
      for j in range (retired_duration):
            bank = (bank*retired_ROR) + retired_contribution
      bank = round(bank,2)
      print ("$",bank)
            
retirement_calculator(10000)
