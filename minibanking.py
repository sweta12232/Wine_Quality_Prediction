import random
print("Mini Banking System")

total = 0

def userAccount(account_number, user_password):
    random_num = random.randint(1000000000, 9999999999)
    print(random_num)
    user_password = input("Enter the 4 digit password")
    
print("Enter your preferences ")
user_choice = input("Enter d to deposit, w to withdraw: ").lower()
def depositAmount( amount):
    if amount < 0:
        print("Invalid Input")
    if user_choice == "d":
        amount = int(input("Enter the amount you want to deposit:"))
    return total + amount
    print(f"Your total amount is {total}")
        
def withdrawAmount( withdraw, total):
    if user_choice == "w":
      withdraw =  int(input("Enter the amount you want to withdraw"))
      if withdraw > total:
          print("You have insufficent balance")
    elif withdraw < total:
        print(f"Nrs {withdraw} is reduced from your account")
        total = total - withdraw
        print(f"The total amount is {total}")
        
        
userAccount(123, 1234)
total = depositAmount(0)
withdrawAmount(0,total)
          
          
    