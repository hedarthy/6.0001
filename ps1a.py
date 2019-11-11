#part 1a

#ask user for salary, percent of salary saved, and total cost of home
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#data from problem
portion_down_payment = 0.25
cost_downpayment = total_cost * portion_down_payment
r = 0.04
monthly_salary = annual_salary / 12
monthly_return = r / 12
monthly_deposits = portion_saved * monthly_return
current_savings = 0.0

months = 0

while current_savings < cost_downpayment:
    months += 1 #count the months
    
    #multiply savings by rate of return
    current_savings *= 1 + monthly_return
    current_savings += monthly_deposits

print("Months: ", months)