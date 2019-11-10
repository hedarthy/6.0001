#part 1a

#take the inputs
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
counter = 0

#calculate how much you need to save
cost_downpayment = total_cost * portion_down_payment

#calculate how much you save on a monthly basis
monthly_earnings = current_savings * r/12

while current_savings < cost_downpayment:
    monthly_savings = (annual_salary / 12) * portion_saved
    current_savings = (current_savings*r/12) + monthly_savings
    counter += 1

print("Number of months: ", counter)