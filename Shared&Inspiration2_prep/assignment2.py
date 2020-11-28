import datetime

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


def deposit(amount: int, account):
    account['Balance'] += amount
    payer = input("Paid by: ")
    date = input("Date of this payment: ")

    new_deposit = {"Amount": amount, "Date": date, "Payer": payer, "Transaction": 'deposit'}
    account['History'].append(new_deposit)


def withdraw(amount: int, account):

    if account['Balance'] >= amount:
        account['Balance'] -= amount

        date = input("Date of this payment?: ")
        new_withdraw = {"Amount": amount, "Date": date, "Transaction": 'withdraw'}
        account['History'].append(new_withdraw)
    else:
        print("Not enough fund")


def print_balance(account):
    print(f"{account['Type']} account balance: {account['Balance']}")


def print_history(account):
    for record in account["History"]:
        print(record)

    print(f"\nThe total balance of {account['Type']} is {account['Balance']}")


def search_by_period(period, account):
    new_list = []
    date_today = datetime.datetime.now()
    for record in account['History']:
        year = int(record['Date'][0:4])
        month = int(record['Date'][5:7])
        day = int(record['Date'][8:10])
        date = datetime.datetime(year, month, day)

        if (date_today-date).days <= period:
            new_list.append(record)

    print("--Search result--")
    for record in new_list:
        print(record)


def search_by_date(start_date, end_date, account):
    new_list = []
    for record in account['History']:
        year = int(record['Date'][0:4])
        month = int(record['Date'][5:7])
        day = int(record['Date'][8:10])
        date = datetime.datetime(year, month, day)
        start = datetime.datetime(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]))
        end = datetime.datetime(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]))
        if start <= date <= end:
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

    # checking = {"Balance": 0, "History": [], "Type": "CHECKING"}
    # saving = {"Balance": 0, "History": [], "Type": "SAVING"}

    selected_account = checking
    populate_samples(checking, saving)
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
                    search_by_period(0, selected_account)
                elif option_2 == 2:
                    search_by_period(7, selected_account)
                elif option_2 == 3:
                    search_by_period(30, selected_account)
                elif option_2 == 4:
                    search_date_start = input('start date?')
                    search_date_end = input('end date?')
                    search_by_date(search_date_start, search_date_end, selected_account)

    print("Program ends")
