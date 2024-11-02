'''
function
variable
constant
'''
def server():
    Number_of_Servers = 3
    Max_Accounts = 50

    
    Server1_Accounts = int(input("Give number of accounts for server 1: "))
    Server2_Accounts = int(input("Give number of accounts for server 2: "))

    
    if Server1_Accounts + Server2_Accounts > Max_Accounts:
        print("You have exceeded the maximum allowable accounts")
    elif Server1_Accounts + Server2_Accounts == Max_Accounts:
        print("There are no additional accounts allowed")
    else:
        remaining_accounts = Max_Accounts - (Server1_Accounts + Server2_Accounts)
        print(f'There are {remaining_accounts} accounts still available')
    return


if __name__ == "__main__":
    while True:
        print("1. Assign servers \n2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            server()
        elif choice == '2':
            exit()
        else:
            print("Invalid choice")
