# Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage
# over given Nth terms at a given interest rate. Also figure out how long it
# will take the user to pay back the loan. For added complexity, add an option
# for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

def mortgage_calculator():
    annual_int_rate = 0
    annual_int_rate = float(annual_int_rate)
    mortgage_life = 0
    mortgage_life = float(mortgage_life)
    mortgage_amount = float(raw_input("Enter the amount would you like to borrow: "))

    salary = float(raw_input("Enter your salary per annum: "))

    if salary > 15000 and salary <= 24999 and mortgage_amount > 50000:
        annual_int_rate += 0.15
        mortgage_life += 30
    elif salary > 24999 and salary <= 44999 and mortgage_amount > 50000:
        annual_int_rate += 0.125
        mortgage_life += 25
    elif salary > 45000 and salary <= 64999 and mortgage_amount > 50000:
        annual_int_rate += 0.10
        mortgage_life += 20
    else:
        annual_int_rate += 0.06
        mortgage_life += 15

    r = float(annual_int_rate/12)
    n = mortgage_life * 12
    mnth_paym = mortgage_amount * (r(1 + r)**n/(1 + r)**n - 1)
    print("Monthly payments for the next {} months will be {}".format(n, mnth_paym))



def run():
    employment_check = raw_input("Are you employed [y/n]: ").upper()
    if employment_check == "Y":
        mortgage_calculator()
    else:
        print("You don't qualify for a mortgage")

run()



