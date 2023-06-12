class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} Kenyan Shillings. Current balance: {self.balance} Kenyan Shillings.")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance: {self.balance} Kenyan Shillings.")


def convert_currency(units, rate):
    converted_amount = units * rate
    return converted_amount


def main():
    account = BankAccount()
    units = float(input("Enter the number of units: "))
    currency = input("Enter the currency to exchange (USD, JPY, GBP, EUR): ")
    rate = 0

    if currency == "USD":
        rate = float(input("Enter the market exchange rate for USD to Kenyan Shillings: "))
    elif currency == "JPY":
        rate = float(input("Enter the market exchange rate for JPY to Kenyan Shillings: "))
    elif currency == "GBP":
        rate = float(input("Enter the market exchange rate for GBP to Kenyan Shillings: "))
    elif currency == "EUR":
        rate = float(input("Enter the market exchange rate for EUR to Kenyan Shillings: "))
    else:
        print("Invalid currency. Please enter USD, JPY, GBP, or EUR.")
        return

    converted_amount = convert_currency(units, rate)
    account.withdraw(converted_amount)

    while True:
        print("\nPlease choose an option:")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "2":
            account.check_balance()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")


if __name__ == '__main__':
    main()
