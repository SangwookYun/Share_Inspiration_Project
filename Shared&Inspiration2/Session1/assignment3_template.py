from datetime import date
import datetime
"""
Assignment scope:
1. Define functions
2. Study Generator, Comprehension, and exception.
3. Review datetime and date module and its differences. 
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
        6. Search records by date/amount
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
        5. search by amount
        6. Go back to Main Menu
        """)

        try:
            selected_int = int(selected)
            if selected_int in range(1, 7):
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


def get_date():
    """
    TODO:
    Check when this function is called.
    You should complete this function with exception.
    If user enter the wrong format (not YYYY-MM-DD), call exception.
    If user enter the right format of date, return date. (not datetime, it should be date!)
    """
    while True:
        try:
            date_input =input("Date of this payment : ")
            date = datetime.strptime(date_input, '%Y-%m-%d')
            return date
        except:
            print("Please enter the date with yyyy-mm-dd")


def deposit(amount: int, account):
    account['Balance'] += amount
    payer = input("Paid by: ")
    date = get_date()
    new_deposit = {"Amount": amount, "Date": date, "Payer": payer, "Transaction": 'deposit'}
    account['History'].append(new_deposit)


def withdraw(amount: int, account):
    """
    TODO:
    Access checking & saving account through parameter.
    Each withdraw records should be added on 'history' of the account and deduct the amount to the balance of account.
    Do not add if balance is not enough.

    Use get_date() function !!!

    records should be the form of dictionary and these are elements:
        "Date" : input by user, the form of "yyyy-mm-dd" ex) 2020-03-05, 2020-09-05
        "Amount": input by user through parameter.
        "Transaction" : It is default to "withdraw"
    """


def print_balance(account):
    print(f"{account['Type']} account balance: {account['Balance']}")


def print_history(account):
    for record in account["History"]:
        print(record)

    print(f"\nThe total balance of {account['Type']} is {account['Balance']}")


def search_by_period(period, account):
    """
     TODO:
     Check the parts of this function which can be replaced by list comprehension, and use list comprehension
     to generate 'new_list'.
     """
    date_today = date.today()

    new_list = []
    for record in account['History']:
        if 0 <= (date_today - record['Date']).days <= period:
            new_list.append(record)

    new_list =[record for record in account['History'] if 0 <= (date_today - record['Date']).days <= period]


    print("--Search result--")
    for record in new_list:
        print(record)


def search_by_date(account):
    """
     TODO:
     Check when this function is called.
     You should complete this function with exception.
     Start date and End date will be entered by user. Store it to type of date (not datetime)!!!

     If user enter the wrong format (not YYYY-MM-DD), call exception.
     If user enter the right format of date, add it to new list and print the results.
     Use list comprehension to generate new list.

     hint
     On the account['History'], each date is stored on the type of date. You should change the type of "date" to
     "datetime". If you change it to datetime, then it is easy to compare between two different dates.
     To change it, you can use "combine" method.

     This is an example. =>  datetime.combine(record['Date'], datetime.min.time())
     """
    try:

        start_date_input = input("start date")
        end_date_input = input("end date")
        start_date = datetime.strptime(start_date_input, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_input, '%Y-%m-%d')

        new_list = [record for record in account['History'] if
                    start_date <= datetime.combine(record['Date'], datetime.min.time()) <= end_date]

        print("--Search result--")
        for record in new_list:
            print(record)



    except:
        print("Please ... yyyy-mm-dd")


def get_records_by_amount(amount, account):
    """
     TODO:
     Check when this function is called.
     Return transaction records which amount('Amount' in 'History')  >= amount(function argument)
     You should use GENERATOR.
    """
    for record in account['History']:
        if record['Amount']>=amount:
            yield record


def populate_samples(account_1, account_2):
    """
    This is sample records for the purpose of test
    """
    test_acc1_ex = [{"Amount": 500, "Date": date(year=2020, month=9, day=22), "Payer": 'SAP', "Transaction": 'deposit'},
                    {"Amount": 20, "Date": date(year=2020, month=9, day=23), "Transaction": 'withdraw'},
                    {"Amount": 15, "Date": date(year=2020, month=9, day=23), "Transaction": 'withdraw'},
                    {"Amount": 70, "Date": date(year=2020, month=9, day=24), "Transaction": 'withdraw'},
                    {"Amount": 65, "Date": date(year=2020, month=9, day=24), "Transaction": 'withdraw'},
                    {"Amount": 3, "Date": date(year=2020, month=9, day=25), "Transaction": 'withdraw'},
                    {"Amount": 5, "Date": date(year=2020, month=9, day=25), "Transaction": 'withdraw'},
                    {"Amount": 7, "Date": date(year=2020, month=9, day=26), "Transaction": 'withdraw'},
                    {"Amount": 9, "Date": date(year=2020, month=9, day=26), "Transaction": 'withdraw'},
                    {"Amount": 10, "Date": date(year=2020, month=9, day=26), "Transaction": 'withdraw'}]

    test_acc2_ex = [
        {"Amount": 300, "Date": date(year=2020, month=9, day=5), "Payer": 'Microsoft', "Transaction": 'deposit'},
        {"Amount": 10, "Date": date(year=2020, month=9, day=14), "Transaction": 'withdraw'},
        {"Amount": 7, "Date": date(year=2020, month=9, day=14), "Transaction": 'withdraw'},
        {"Amount": 30, "Date": date(year=2020, month=9, day=15), "Transaction": 'withdraw'},
        {"Amount": 4, "Date": date(year=2020, month=9, day=20), "Transaction": 'withdraw'},
        {"Amount": 50, "Date": date(year=2020, month=9, day=21), "Payer": 'TDBank', "Transaction": 'deposit'},
        {"Amount": 10, "Date": date(year=2020, month=9, day=21), "Transaction": 'withdraw'},
        {"Amount": 60, "Date": date(year=2020, month=9, day=22), "Transaction": 'withdraw'},
        {"Amount": 38, "Date": date(year=2020, month=9, day=22), "Transaction": 'withdraw'},
        {"Amount": 10, "Date": date(year=2020, month=9, day=24), "Payer": 'John Doe', "Transaction": 'deposit'}]

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

                if option_2 not in range(1, 7):
                    print("Invalid input")
                    continue
                elif option_2 == 6:
                    is_running_2 = False

                if option_2 == 1:
                    search_by_period(0, selected_account)
                elif option_2 == 2:
                    search_by_period(7, selected_account)
                elif option_2 == 3:
                    search_by_period(30, selected_account)
                elif option_2 == 4:

                    search_by_date(selected_account)

                elif option_2 == 5:
                    amount = int(input("Please enter the amount \n"))
                    records = get_records_by_amount(amount, selected_account)
                    count = 0
                    while True:
                        try:
                            print(next(records))
                            count += 1
                        except (StopIteration, IndexError, ValueError):
                            break
                    print(f"{count} records found")

    print("Program ends")
