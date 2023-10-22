'''Implement a class called BankAccount that represents a bank account.The class should have private
attributes for account number,account holder name,and account balance.Include method to
deposit money, withdrawl money,and display the account balance.Ensure that the account balance
cannot be accessed directly from outside the classes.write a program to creat an instance of the
BankAccount class and test the deposit and withdrawl functionality '''


class BankAccount:

  def __init__(self, account_number,account_holder_name,initial_balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
    
    
    print ("Deposited {}. New balance: {}". format (amount,self__account_balance))
    
    else:
      print ("Invalid deposit amount.please deposit a positive anount.")

  def withdrawl(self, amount):
    if amount > 0 and amount<= self.__account_balance:
      self.__account_balance -= amount

      print ("Withdrawl {}.New balance: {}". format (amount_account_balance))
      
      
      else:
        print ("Invalid withdrawl amount or insufficient balance.")

 def display_balance(self):
   print ("Account balance for {} (Account #{}).{}".format(self_account_holder_name,s3lf.__account_nunber,self.__account_balance))




account=BankAccount(account_number="123456789",
account_holder_name="Monika",
initial_balance = 5000.0)


account.display_balance()
account.deposit(500.0)
account.withdrawl(200.0)
account.display_balance()

