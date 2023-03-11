def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance
        #print("The balance is", current_balance)

balance = withdraw_money(200, 80)

if (balance <=50):
    print("We need to make a deposit")
else:
    print("Your balance is good to go!")