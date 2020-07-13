menu = ['Knacked', 'Pip Pip', 'Squidgy', 'Smashing']
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1

print(menu_prices)