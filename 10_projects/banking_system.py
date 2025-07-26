# Banking System with Account Management

# Features:
# 1. Multiple Account Types (Savings, Current)
# 2. Transaction History
# 3. Interest Calculation
# 4. Account Statement Generation
# 5. Money Transfer between Accounts

import json
from datetime import datetime
import random
import string

class BankAccount:
    """Base class for bank accounts"""
    def __init__(self, account_holder, initial_balance=0):
        self.account_number = self._generate_account_number()
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def _generate_account_number(self):
        """Generate a random 10-digit account number"""
        return ''.join(random.choices(string.digits, k=10))
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            return {"status": "error", "message": "Invalid deposit amount"}
        
        self.balance += amount
        self._add_transaction("Credit", amount)
        return {"status": "success", "message": f"Deposited ${amount:.2f}"}
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            return {"status": "error", "message": "Invalid withdrawal amount"}
        if amount > self.balance:
            return {"status": "error", "message": "Insufficient funds"}
        
        self.balance -= amount
        self._add_transaction("Debit", amount)
        return {"status": "success", "message": f"Withdrawn ${amount:.2f}"}
    
    def _add_transaction(self, type_, amount):
        """Record a transaction"""
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": type_,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(transaction)
    
    def get_statement(self):
        """Generate account statement"""
        statement = f"\nAccount Statement for {self.account_number}"
        statement += f"\nAccount Holder: {self.account_holder}"
        statement += f"\nAccount Type: {self.__class__.__name__}"
        statement += f"\nCreated Date: {self.created_date}"
        statement += f"\nCurrent Balance: ${self.balance:.2f}"
        statement += "\n\nTransaction History:"
        statement += "\nDate                 Type      Amount     Balance"
        statement += "\n" + "-"*50
        
        for t in self.transactions:
            statement += f"\n{t['date']}  {t['type']:<8}  ${t['amount']:<8.2f}  ${t['balance']:.2f}"
        
        return statement

class SavingsAccount(BankAccount):
    """Savings account with interest calculation"""
    def __init__(self, account_holder, initial_balance=0, interest_rate=2.5):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        """Calculate monthly interest"""
        interest = self.balance * (self.interest_rate / 100 / 12)
        self.deposit(interest)
        return {"status": "success", "message": f"Interest credited: ${interest:.2f}"}

class CurrentAccount(BankAccount):
    """Current account with overdraft facility"""
    def __init__(self, account_holder, initial_balance=0, overdraft_limit=1000):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Withdraw with overdraft facility"""
        if amount <= 0:
            return {"status": "error", "message": "Invalid withdrawal amount"}
        if amount > (self.balance + self.overdraft_limit):
            return {"status": "error", "message": "Amount exceeds overdraft limit"}
        
        self.balance -= amount
        self._add_transaction("Debit", amount)
        return {"status": "success", "message": f"Withdrawn ${amount:.2f}"}

class Bank:
    """Bank management system"""
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_type, holder_name, initial_balance):
        """Create a new bank account"""
        if account_type.lower() == "savings":
            account = SavingsAccount(holder_name, initial_balance)
        elif account_type.lower() == "current":
            account = CurrentAccount(holder_name, initial_balance)
        else:
            return {"status": "error", "message": "Invalid account type"}
        
        self.accounts[account.account_number] = account
        return {"status": "success", "message": f"Account created successfully!", "account_number": account.account_number}
    
    def transfer_money(self, from_acc_num, to_acc_num, amount):
        """Transfer money between accounts"""
        if from_acc_num not in self.accounts or to_acc_num not in self.accounts:
            return {"status": "error", "message": "Invalid account number(s)"}
        
        from_account = self.accounts[from_acc_num]
        to_account = self.accounts[to_acc_num]
        
        # Try withdrawal first
        withdrawal = from_account.withdraw(amount)
        if withdrawal["status"] == "error":
            return withdrawal
        
        # If withdrawal successful, deposit to recipient
        deposit = to_account.deposit(amount)
        return {"status": "success", "message": f"Transferred ${amount:.2f} successfully"}

def main():
    bank = Bank()
    
    while True:
        print("\n=== Banking System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Check Balance")
        print("6. Account Statement")
        print("7. Calculate Interest (Savings)")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            name = input("Enter account holder name: ")
            acc_type = input("Enter account type (savings/current): ")
            try:
                initial = float(input("Enter initial deposit amount: "))
                result = bank.create_account(acc_type, name, initial)
                print(f"\n{result['message']}")
                if result['status'] == 'success':
                    print(f"Account Number: {result['account_number']}")
            except ValueError:
                print("Please enter a valid amount!")
        
        elif choice in ["2", "3", "4", "5", "6", "7"]:
            acc_num = input("Enter account number: ")
            if acc_num not in bank.accounts:
                print("Invalid account number!")
                continue
            
            account = bank.accounts[acc_num]
            
            if choice == "2":
                try:
                    amount = float(input("Enter deposit amount: "))
                    result = account.deposit(amount)
                    print(f"\n{result['message']}")
                except ValueError:
                    print("Please enter a valid amount!")
            
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    result = account.withdraw(amount)
                    print(f"\n{result['message']}")
                except ValueError:
                    print("Please enter a valid amount!")
            
            elif choice == "4":
                to_acc = input("Enter recipient's account number: ")
                try:
                    amount = float(input("Enter transfer amount: "))
                    result = bank.transfer_money(acc_num, to_acc, amount)
                    print(f"\n{result['message']}")
                except ValueError:
                    print("Please enter a valid amount!")
            
            elif choice == "5":
                print(f"\nCurrent Balance: ${account.balance:.2f}")
            
            elif choice == "6":
                print(account.get_statement())
            
            elif choice == "7":
                if isinstance(account, SavingsAccount):
                    result = account.calculate_interest()
                    print(f"\n{result['message']}")
                else:
                    print("Interest calculation is only available for savings accounts!")
        
        elif choice == "8":
            print("Thank you for using our Banking System!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
