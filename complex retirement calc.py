# calculate retirement savings
#  start_age is the age (in months) when we start the calculation
#  initial is the initially saved balance at the start
#  working is a three tuple (months, contribution, rate of return)
#  retired is a three tuple (months, contribution, rate of return)
def calculate(start_age, initial, months, contribution, ror):
    global balance
    balance = initial
    global age_year
    age_year = start_age/12
    global age_month
    age_month = start_age % 12
    for i in range (months):
        print (f'Age  {int(age_year)} month {(int(age_month))} you have ${(balance):.2f}')
        balance += balance*ror
        balance += contribution
        if age_month < 11:
            age_month += 1
        elif age_month >= 11:
            age_year += 1
            age_month = 0
    return balance
    return age_year
    return age_month


def calculateRetirement(start_age, initial, working, retired):
    work_calc = calculate(start_age, initial, *working)
    new_age = (int(age_year)*12) + age_month
    retired_calc = calculate(new_age, balance,*retired)
    pass

def main():
    working=(234, 1234.00, 0.0039062)
    retired=(105, -3567.00, 0.0097656)
    calculateRetirement(240, 0.00, working, retired)
    pass

if __name__=="__main__":
    main()
    pass
