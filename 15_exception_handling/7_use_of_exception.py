# use of exception handling -

# example -
# requirement - 1. balance in bank should not be less than 1000
# 2. user account will be blocked for an hour if user put 3 times wrong pin


import time

class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempts = 1

def withdraw():
    global attempts  # we can update the global variable 
    saved_pin = 1234   # hard-coded
    balance = 10000   # hard-coded

    pin = int(input("Enter the PIN : "))
    if pin == saved_pin:
        try :
            amount = int(input("Enter amount to withdraw : "))
            temp_amount = balance - amount 
            if temp_amount < 1000:
                raise BalanceExceptionError("Incificient balance")
        
            balance = temp_amount
            print("Amount is deducted from your account")
            print("Your current balance is : ", balance)

        except Exception as var:
            print(var)


    else :
        print("wrong pin")
        ans = input("Do you want to continue again (y/n) : ")
        if ans.lower() == 'y':
            attempts+=1
            try :
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts, your account is blocked for an hour")
            except Exception as var:
                print(var)
                time.sleep(3600)  # time in second
            else :
                withdraw()

withdraw()
        
















