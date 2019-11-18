#ps1c
#modified code from @tuthang102

#user input
annual_salary = float(input("Enter the starting salary: "))
placeholder = annual_salary

#problem data
total_cost = 1000000
semi_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 36

#acceptable range and bisection search
epsilon = 100
low = 0
high = 10000
counter = 0

while True:
    #reset
    portion_saved = (low + high) / 2
    annual_salary = placeholder
    current_savings = 0
    monthly_salary = annual_salary / 12.0

    for i in range(1, months + 1):
        returnOnInvestment = (current_savings * 0.04) / 12
        monthlyDeposit = float(monthly_salary * portion_saved) / 10000
        current_savings = current_savings + monthlyDeposit + returnOnInvestment

        if i % 6 == 0:
            annual_salary = annual_salary + (annual_salary + semi_raise)
    
    if abs(current_savings - portion_down_payment) <= epsilon:
        print("Best savings rate: ", round(portion_saved / 100, 2), "%")
        print("Steps in binary search", counter)
        break

    #if guess was too high
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings > portion_down_payment:
        high = portion_saved

    #if guess was too low
    elif abs(current_savings - portion_down_payment) > epsilon and current_savings < portion_down_payment:
        low = portion_saved
    
    if low == high:
        print("It is not possible to pay the downpayment in three years.")
        break
    
    counter += 1