#part 1c

#ask user for salary, and fill in the blanks
annual_salary = float(input("Enter the starting salary: "))
#portion_saved is variable you are looking for
total_cost = 1000000
semi_annual_raise = 0.07

#data from problem
annual_r = 0.04
monthly_r = annual_r / 12.0

#how much to add monthly
monthly_salary = annual_salary / 12.0
#monthly_deposit = monthly_salary #* portion_saved guess

#cost of home
cost_downpayment = 0.25 * total_cost

#counter and savings
months = 36
current_savings = 0.0

#bisection sort 
epsilon = 100
num_guesses = 0
low = 0
high = 10000
guess = ((low + high) / 2.0)

while abs(current_savings - cost_downpayment) >= epsilon:

    #reset
    current_savings = 0

    for i in range(0, months):
        monthly_deposit = monthly_salary * (guess / 10000)

        if i % 6 == 5:
            annual_salary = annual_salary * (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12.0
            monthly_deposit = monthly_salary * (guess / 10000)

        returnOnInvestment = monthly_r * current_savings
        current_savings += returnOnInvestment
        current_savings += monthly_deposit

    if current_savings > cost_downpayment:
        #look in upper half
        low = guess
    else:
        #look in lower half
        high = guess
    guess = (low + high)/2.0
    num_guesses += 1 #counts guesses

print("best savings rate:", guess)
print("Stepts in bisection search: ", num_guesses)