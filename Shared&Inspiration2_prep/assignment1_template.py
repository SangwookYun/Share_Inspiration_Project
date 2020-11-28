"""
Assignment scope:
1. Define functions
2. Define variables
3. Use only limited global variables
4. Try different ways of calling arguments
5. Use 'while, if-elif-else, nested if-else
"""


CHECKING = 'checking' # In this assignment, checking account is used as a default account
SAVING = 'saving'


def select_menu() -> int:
    is_valid_input = False

    while not is_valid_input:
        selected = input("""
        1. Deposit
        2. Withdrawal
        3. Balance check
        4. Select account
        5. Exit
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


def select_account() -> str:
    """
    TODO:
    Get a user input; '1' as 'checking account' and '2' as 'saving account'.
    If user selects checking account, return CHECKING.
    If user selects saving account, return SAVING.
    Otherwise, return CHECKING as a default.
    """


def get_amount() -> int:
    while True:
        amount = input("Enter amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
        print("Invalid amount")


def deposit(amount: int, account: str = CHECKING):
    """
    TODO:
    Add a proper argument.
    Access checking_bal & saving_bal as global variable.
    Depending on arguments, deposit & change the balance of 'checking' or 'saving'
    """


def withdraw(amount: int, account: str = CHECKING):
    """
    TODO:
    Add a proper argument.
    Access checking_bal & saving_bal as global variable.
    Depending on arguments, withdraw & change the balance of 'checking' or 'saving'
    """


def print_balance():
    """
    TODO:
    Add a proper argument.
    Access checking_bal & saving_bal as global variable.
    Depending on the argument, print the balance of 'checking' or 'saving'
    """


if __name__ == "__main__":
    """ 
    REQ: Only access checking_bal & saving_bal from other functions as global variables
    """
    checking_bal = 0
    saving_bal = 0

    selected_account = CHECKING
    is_running = True

    while is_running:
        print(f"Selected account: {selected_account}")
        option = select_menu()

        if option not in range(1, 6):
            print("Invalid input")
            continue
        elif option == 5:
            is_running = False

        """
        REQ: Try Case 1 ~ 3 and compare behaviors and results. 
        Other cases should be commented out when one case is tested.
        """

        """ Case 1"""
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

        """ Case 2"""
        # if option == 1:
        #     input_amount = get_amount()
        #     deposit(account=selected_account, amount=input_amount)
        # elif option == 2:
        #     input_amount = get_amount()
        #     withdraw(account=selected_account, amount=input_amount)
        # elif option == 3:
        #     print_balance(selected_account)
        # elif option == 4:
        #     selected_account = select_account()

        """ Case 3"""
        # if option == 1:
        #     input_amount = get_amount()
        #     deposit(amount=input_amount)
        # elif option == 2:
        #     input_amount = get_amount()
        #     withdraw(amount=input_amount)
        # elif option == 3:
        #     print_balance(selected_account)
        # elif option == 4:
        #     selected_account = select_account()

    print("Program ends")
