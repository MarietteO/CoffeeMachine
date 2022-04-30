MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = 0

machine_on = True

def resources_sufficient(drink):
    """Check if there are enough resources to make the drink"""
    for resource in resources:
        if resources[resource] < MENU[drink]["ingredients"][resource]:
            print(f"Sorry, there is not enough {resource}.")
            return False
        else:
            return True

def process_coins():
    """Prompt for coins and calculate value of coins"""
    print("Please insert coins.")
    amount_of_quarters = int(input("How many quarters? "))
    amount_of_dimes = int(input("How many dimes? "))
    amount_of_nickles = int(input("How many nickles? "))
    amount_of_pennies = int(input("How many pennies?"))
    total_amount = ((amount_of_quarters*25)+(amount_of_dimes*10)+(amount_of_nickles*5)+(amount_of_pennies*1))/100
    return total_amount

def transaction_successful(drink, money_paid):
    """Check if user has inserted enough money"""
    if MENU[drink]["cost"] > money_paid:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif MENU[drink]["cost"] < money_paid:
        change = money_paid - MENU[drink]["cost"]
        print(f"Your change is ${change:.2f}.")
        return True
    else:
        return True


while machine_on:
    choice = input("What would you like? espresso/latte/cappuccino: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        for resource in resources:
            print(f"{resource}: {resources[resource]}ml")
        print(f"Money: ${Money:.2f}")
    else:
        if resources_sufficient(choice) == True:
            amount = process_coins()
            for resource in resources:
                resources[resource] -= MENU[choice]["ingredients"][resource]
                if resources[resource] < 0:
                    resources[resource] = 0
            if transaction_successful(choice, amount) == True:
                Money += MENU[choice]["cost"]
                print(f"Here is your {choice}. ☕ Enjoy!")



