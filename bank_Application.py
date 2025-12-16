
## Creating table 
#accounts_table = {account: password}
#users_table = {account:[amount, Name, email]}

accounts_table = {1234:456,
                  1235:457}

users_table = {1234:[1000, 'farooq', 'chfarooq2001@gmail.com'],
               1235:[500, 'surya', 'surya@gmail.com']}

# functions
# login function defination 
def login(username:int, password:int):
    # checking the account numer is exist in accounts table or not
    if username in accounts_table:
        # checking the password
        if password == accounts_table[username]:
            print("Login successfull")
            return True
        else:
            print("Check with credentials")
            return False
    else:
        print("User Not Found")
        return False


# withdraw function defination
def withdraw(account:int, withdraw_amount:int):
    # checking account in users table
    if account in users_table:
        amount = users_table[account][0]
        # checking amount is sufficient or not
        if amount >= withdraw_amount:
            users_table[account][0] -= withdraw_amount
            print(f"{withdraw_amount} withdraw successful and \
                  current balence is: {users_table[account][0]}")
        else:
            print("Insufficient amount in your account")
    else:
        print("User not found")

# deposite function defination
def deposite(account:int, deposite_amount:int):
    # checking account in users table
    if account in users_table:
         # validating amount 
        if deposite_amount > 0:
            users_table[account][0] += deposite_amount
            print(f"{deposite_amount} deposite successful and \
                  current balence is: {users_table[account][0]}")
        else:
            print("Check with your deposite amount")
    else:
        print("User not found")

# transfer function defination
def transer(sender:int,reciever:int, transfer_amount:int):
    # checking account in users table
    if sender in users_table:
        amount = users_table[sender][0]
        # reciever account is peresent in users table or not
        if reciever in users_table:
            # checking amount is sufficient or not
            if amount >= transfer_amount:
                users_table[sender][0] -= transfer_amount
                users_table[reciever][0] += transfer_amount
                print(f"{transfer_amount} Transfer successful and \
                    current balence is: {users_table[sender][0]}")
            else:
                print("Insufficient amount in your account")
        else:
            print("Reciever account not found")
    else:
        print("User not found")

# ministatement function defination
def ministatement(account:int):
    print("ministatement page development under proccessing")

# balence enquiry fuynction defination 
def balenceEnquiry(account:int):
    if account in users_table:
        print(f"Current balence is: {users_table[account][0]}")
    else:
        print("User not found")

# logout function defination
def logout():
    print("logout successfully")
    exit()





# main
if __name__ == "__main__":
    print("Welcome to the Codegnan Bank Application")
    username = int(input("Enter your account number:"))
    password = int(input("Enter your password:"))
    login_val = login(username = username, password = password)
    while login_val:
        operations = ("1. Withdraw \n",
                      "2. Deposite \n",
                      "3. Transfer \n",
                      "4. Mini Statement \n",
                      "5. Balance Enquiry \n",
                      "6. Logout \n"
                      )
        print(*operations)
        choice = int(input("Select you operation:"))
        if choice == 1:
            amount = int(input("Enter your withdraw amount:"))
            withdraw(account= username, withdraw_amount= amount)

        elif choice == 2:
            amount = int(input("your deposite amount:"))
            deposite(account= username, deposite_amount=amount)

        elif choice == 3:
            account = int(input("Enter reciever account anumber:"))
            amount = int(input("Enter your transfer amount:"))
            transer(sender=username, reciever=account, transfer_amount=amount)
        
        elif choice == 4:
            ministatement(account=username)
        
        elif choice == 5:
            balenceEnquiry(account=username)
        elif choice == 6:
            logout()
        else:
            print("select your operation in betwen 1 - 6")
