#part 1a

#ask user for salary, percent of salary saved, and total cost of home
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#data from problem
portion_down_payment = 0.25
annual_r = 0.04
monthly_r = annual_r / 12.0

#how much to add monthly
monthly_salary = annual_salary / 12.0
monthly_deposit = monthly_salary * portion_saved

#cost of home
cost_downpayment = portion_down_payment * total_cost

#counter and savings
months = 0
current_savings = 0.0

while current_savings < cost_downpayment:
    months += 1

    returnOnInvestment = (monthly_r)*current_savings
    current_savings += returnOnInvestment
    current_savings += monthly_deposit

print("Number of months:", months)