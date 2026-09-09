class insufficientBalance(Exception):
  pass

balance=5000


def depositBalance(amount):
    
    if (amount>0):
        balance =balance+amount
        print("Amount is deposited successfully")
        print("Updated balance is ",balance)
    else:
        print("Amount is not deposited successfully")


def withdrawBalance(amount):
    if(balance<amount):
        raise insufficientBalance("Balance is insufficient")
    else: 
        balance=balance-amount
        print("Amount is withdrawn successfully")
        print("Remaining balance is ",balance)


print("\t\tWelcome to ATM\t\t")
print("1. Deposit Balance")
print("2. Withdraw Balance")
case=int(input("Enter your case:"))

if case==1:
    try:
        print("\tAvailable balance is ",balance)
        amount=int(input("Enter amount to deposit:"))
        depositBalance(amount)
    except insufficientBalance as e:
        print(e)
elif case==2:
    try:
        print("\tAvailable balance is ",balance)
        amount=int(input("Enter amount to withdraw:"))
        withdrawBalance(amount)
    except insufficientBalance as e:
        print(e)
else:
    print("Invalid case")
