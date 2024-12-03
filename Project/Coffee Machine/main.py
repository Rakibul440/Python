
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 126.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 210.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#ingredients
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
profit = 0

# resource report
def report(left_water,left_milk,left_coffee,total_profit):
    print(f'Water : {left_water}')
    print(f'Milk : {left_milk}')
    print(f'Coffee : {left_coffee}')
    print(f'Money : {total_profit}')

# report(water,milk,coffee)

# Select coffee
def coffee_type():
    types = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return types

# coffee = coffee_type()

# Machine
machine_on = True

while machine_on :
    # ask coffee type
    user_input = coffee_type()

    # machine information
    if user_input == 'off':
        break
    if user_input == 'report':
        report(water,milk,coffee,profit)

    # Check left ingredients
    elif user_input == 'espresso' or user_input == 'latte' or user_input ==  'cappuccino' :
        if MENU[user_input]['ingredients']['water'] > water :
            print('Sorry there is not enough water.')
        else:
            your_money = int(input('Please insert Money 💵 : ₹'))
            if MENU[user_input]['cost'] < your_money :

                # update ingredients
                water -= MENU[user_input]['ingredients']['water']
                if 'milk' in MENU[user_input]['ingredients'] :
                    milk -= MENU[user_input]['ingredients']['milk']
                coffee -= MENU[user_input]['ingredients']['coffee']
                profit += MENU[user_input]['cost']

                print(f'Here is your {user_input}☕.Enjoy!')
                print(f'Here is ₹{your_money - MENU[user_input]['cost']} in change.')
            else:
                print("Sorry that's not enough money. Money refunded.")








