import datetime

"""
Assignment scope:
1. Define functions and variables
2. Add data to list and dictionary
3. Print each element in dictionary and list through for loop
4. Slice string to get specific character 
5. Use datetime package to compare two different dates

Assumption and condition for this assignment:
1. The form of date should be yyyy-mm-dd. 
2. It is assumed that data is entered in order of date.
3. Any exception will be caught after session3. 
"""

checking = {"Balance": 0, "History": [], "Type": "CHECKING"}
saving = {"Balance": 0, "History": [], "Type": "SAVING"}


def select_menu() -> int:
    is_valid_input = False

    while not is_valid_input:
        selected = input("""
        1. Deposit
        2. Withdrawal
        3. Balance check
        4. Select account
        5. View History
        6. Search records by date
        7. Exit
        """)

        try:
            selected_int = int(selected)
            if selected_int in range(1, 8):
                is_valid_input = True
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")

    return selected_int


def date_search_menu() -> int:
    """
    This is a second menu when user input "6. Search records by date" on main Menu
    :return: selected_input (int)
    """
    is_valid_input = False

    while not is_valid_input:
        selected = input("""
        1. Today
        2. Last 7 days
        3. Last 1 month
        4. search by date
        5. Go back to Main Menu
        """)

        try:
            selected_int = int(selected)
            if selected_int in range(1, 6):
                is_valid_input = True
            else:
                print("Wrong input")
        except ValueError:
            print("Wrong input")

    return selected_int


def select_account():
    selected = input("""
    1. checking account
    2. Saving account
    """)

    if selected == '1':
        return checking
    elif selected == '2':
        return saving
    else:
        # Use Checking as a default in this scenario
        return checking


def get_amount():
    while True:
        amount = input("Enter amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Invalid amount")


def deposit(amount: int, acc):
    """
    TODO:
    Access checking & saving account through parameter.
    Each deposit records should be added on 'history' of the account and add the amount to the balance of account.
    records should be the form of dictionary and these are elements:
        "Date" : input by user, the form of "yyyy-mm-dd" ex) 2020-03-05, 2020-09-05
        "Amount": input by user through parameter.
        "Payer" : input by user   ex) SAP, Microsoft, Samsung
        "sort" : It is default to "deposit"
    """
    acc['Balance']+=amount
    payer =input("Paid by? ")
    date = input("Date of this payment ? format(YYYY-MM-DD ")

    new_record = {"Amount": amount, "Date": date, "Payer": payer, "Transaction": 'deposit'}
    acc['History'].append(new_record)


def withdraw(amount: int, acc):
    """
    TODO:
    Access checking & saving account through parameter.
    Each withdraw records should be added on 'history' of the account and deduct the amount to the balance of account.
    Do not add if balance is not enough.
    
    records should be the form of dictionary and these are elements:
        "Date" : input by user, the form of "yyyy-mm-dd" ex) 2020-03-05, 2020-09-05
        "Amount": input by user through parameter.
        "sort" : It is default to "withdraw"
    """
    if acc['Balance']>=amount:
        acc['Balance']-=amount
        date = input("Date of this payment ? format(YYYY-MM-DD ")
        new_record = {"Amount": amount, "Date": date, "Transaction": 'withdraw'}
        acc['History'].append(new_record)
    else:
        print("Not enough fund!")

def print_balance(account):
    print(f"{account['Type']} account balance: {account['Balance']}")


def print_history(acc):
    """
    TODO:
    Access checking & saving account through parameter.
    Print history of the total records on the account.
    """
    for record in acc['History']:
        print(record)

    print(f"Total balance : {acc['Balance']}")



# checking = {"Balance": 0, "History": [], "Type": "CHECKING"}
# saving = {"Balance": 0, "History": [], "Type": "SAVING"}

def search_by_period(period, account): # 0, 7, 30
    """
    TODO:
    Access checking & saving account through parameter.
    Compare date of each records on the account with the specific period and print the records if they meet condition.

    hint)
    1. Use datetime package to compare two different dates.
    2. String slicing may be needed.
    """
    new_list = []
    date_today = datetime.datetime.now()
    for record in account['History']: # 2020-09-30
        year = int(record['Date'][0:4]) #2020
        month = int(record['Date'][5:7])  # 09
        day = int(record['Date'][8:10]) # 30
        new_date = datetime.datetime(year, month, day)

        if(date_today- new_date).days <=period:
            new_list.append(record)

    for record in new_list:
        print(record)

def search_by_date(start_date: str, end_date: str, account):
    """
    TODO:
    Access checking & saving account through parameter.
    Compare date of each records on the account with start and end date and print the records if they meet conditions.

    hint)
    1. Use datetime package to compare two different dates.
    2. String slicing may be needed.
    """
    new_list =[]
    for record in account['History']:
        year = int(record['Date'][0:4])  # 2020
        month = int(record['Date'][5:7])  # 09
        day = int(record['Date'][8:10])  # 30
        new_date = datetime.datetime(year, month, day)
        #2020-09-01 2020-09-15
        start = datetime.datetime(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
        end = datetime.datetime(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))

        if start <=new_date <=end:
            new_list.append(record)

    print("--Search result--")
    for record in new_list:
        print(record)





def populate_samples(account_1, account_2):
    """
    This is sample records for the purpose of test
    """
    test_acc1_ex = [{"Amount": 500, "Date": '2020-09-01', "Payer": 'SAP', "Transaction": 'deposit'},
                        {"Amount": 20, "Date": '2020-09-01', "Transaction": 'withdraw'},
                        {"Amount": 15, "Date": '2020-09-02', "Transaction": 'withdraw'},
                        {"Amount": 70, "Date": '2020-09-03', "Transaction": 'withdraw'},
                        {"Amount": 65, "Date": '2020-09-03', "Transaction": 'withdraw'},
                        {"Amount": 3, "Date": '2020-09-04', "Transaction": 'withdraw'},
                        {"Amount": 5, "Date": '2020-09-05', "Transaction": 'withdraw'},
                        {"Amount": 7, "Date": '2020-09-06', "Transaction": 'withdraw'},
                        {"Amount": 9, "Date": '2020-09-07', "Transaction": 'withdraw'},
                        {"Amount": 10, "Date": '2020-09-08', "Transaction": 'withdraw'}]

    test_acc2_ex = [{"Amount": 300, "Date": '2020-09-01', "Payer": 'Microsoft', "Transaction": 'deposit'},
                      {"Amount": 10, "Date": '2020-09-01', "Transaction": 'withdraw'},
                      {"Amount": 7, "Date": '2020-09-02', "Transaction": 'withdraw'},
                      {"Amount": 30, "Date": '2020-09-03', "Transaction": 'withdraw'},
                      {"Amount": 4, "Date": '2020-09-03', "Transaction": 'withdraw'},
                      {"Amount": 10, "Date": '2020-09-01', "Payer": 'TDBank', "Transaction": 'deposit'},
                      {"Amount": 10, "Date": '2020-09-04', "Transaction": 'withdraw'},
                      {"Amount": 20, "Date": '2020-09-05', "Transaction": 'withdraw'},
                      {"Amount": 38, "Date": '2020-09-06', "Transaction": 'withdraw'},
                      {"Amount": 10, "Date": '2020-09-01', "Payer": 'John Doe', "Transaction": 'deposit'},
                      {"Amount": 9, "Date": '2020-09-07', "Transaction": 'withdraw'},
                      {"Amount": 10, "Date": '2020-09-08', "Transaction": 'withdraw'}]

    for record in test_acc1_ex:
        account_1['History'].append(record)
        if record['Transaction'] == 'deposit':
            account_1['Balance'] += record['Amount']
        else:
            account_1['Balance'] -= record['Amount']

    for record in test_acc2_ex:
        account_2['History'].append(record)
        if record['Transaction'] == 'deposit':
            account_2['Balance'] += record['Amount']
        else:
            account_2['Balance'] -= record['Amount']


if __name__ == "__main__":

    selected_account = checking #default
    populate_samples(checking, saving) # this is for populating sample records
    is_running = True

    while is_running:
        print(f"Selected account: {selected_account['Type']}")
        option = select_menu()

        if option not in range(1, 8):
            print("Invalid input")
            continue
        elif option == 7:
            is_running = False

        if option == 1:
            input_amount = get_amount()
            deposit(input_amount, selected_account)
        elif option == 2:
            input_amount = get_amount()
            withdraw(input_amount, selected_account)
        elif option == 3:
            print_balance(selected_account)
        elif option == 4:
            selected_account = select_account()
        elif option == 5:
            print_history(selected_account)
        elif option == 6:

            is_running_2 = True

            while is_running_2:
                option_2 = date_search_menu()

                if option_2 not in range(1, 6):
                    print("Invalid input")
                    continue
                elif option_2 == 5:
                    is_running_2 = False

                if option_2 == 1:
                    search_by_period(0, selected_account)  # today
                elif option_2 == 2:
                    search_by_period(7, selected_account)  # last 7 days
                elif option_2 == 3:
                    search_by_period(30, selected_account) # last 30 days
                elif option_2 == 4:
                    search_date_start = input('start date?') #2020-09-30 string
                    search_date_end = input('end date?')
                    search_by_date(search_date_start, search_date_end, selected_account)

    print("Program ends")
