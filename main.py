import random

#empty list used to story user created accounts
accounts = []

#used as a placeholder ofr unused actions, no longer in use
def unfinished():
  print("Currently unfinished, this is a placeholder.")

#displays user's choices
def display_choices():
  print("1. Withdrawl or Deposit")
  print("2. View Existing Accounts")
  print("3. Create New Account")
  print("4. Help")
  print("5. Exit\n")

#will ask user their username
def ask_username():
  username = input("Enter your username or email: ")
  return username

#will ask user their password
def ask_password():
  password = input("Enter your password: ")
  return password

#custom age return
def age_finder():
  number_is_correct = True
  while number_is_correct is True:
    try:
      age = int(input("What is your age? "))
      if age in range(1, 29):
        print("New to this world!")
      elif age in range(30, 59):
        print("Same age as my younger brother!")
      elif age in range(60, 79):
        print("I wish I was that young!")
      elif age >= 80:
        print("You probably know more than me!")
      else:
        print("Invalid age")
      number_is_correct = False
      return age
    except ValueError:
      print("Invalid input. Please enter a valid age.")

#will let you change the amount in an account
def withdrawl_deposit():
  which_account = 0
  try:
    which_account = int(input("Please enter the account number you wish to make changes to."))
  except ValueError:
    print("That value does not work.")
    withdrawl_deposit()
  for i, account in enumerate(accounts):
    if accounts[i]["account_num"] == which_account:
      amount = input("What would you like to set the balance to?")
      accounts[i]["amount"] = amount
      
#will show you the accounts
def view_accounts():
  for account in accounts:
    print("~~~~~~~~~~~~~~")
    for key, value in account.items():
      print(f"{key}: {value}")
    print("~~~~~~~~~~~~~~")

#will let you create accounts
def create_account():
  type = input("Checking or savings?\n")
  amount = 0
  name = input("What would you like to name the account?\n")
  new_account = Account(type,amount,name)
  accounts.append(new_account.features())
  
  

def help():
  helping = True
  while helping == True:
    help_menu = input("What do you need help with?\n1. Withdrawl\n2. Deposit\n3. View Accounts\n4. Create Account\n5. Checking Account\n6. Savings Account\n7. Exit\n\n" )
    if help_menu == "1":
      print("To withdrawl, you must first have a bank account. You can create one by typing 'create account'. Then, you can access the account to withdrawl by typing '1' into the main menu.\n")
    elif help_menu == "2":
      print("To deposit, you must first have a bank account. You can create one by typing 'create account'. Then, you can access the account to deposit by typing '1' into the main menu.\n")
    elif help_menu == "3":
      print("To view your accounts, you must first have a bank account. You can create one by typing 'create account'. Then, you can access the account to view your accounts by typing '3' into the main menu.\n")
    elif help_menu == "4":
      print("To create an account, you must type '4' into the main menu, then you may create an account.\n")
    elif help_menu == "5":
      print("A checking account is an account where you may remove funds easily. Used for groceries and impulse buys.\n")
    elif help_menu == "6":
      print("A savings account is an account where you may store funds for a long time while accruing interest. This is used for money you wish to divert to retirement or other long term goals.\n")
    elif help_menu == "7":
      print("Exiting...\n")
      helping = False
    

def exit(talking):
  print("Goodbye, see you soon!")
  talking = False
  return talking

#will display list of options
def list_of_options(talking):
  while talking is True:
    display_choices()
    try:
      selection = int(input("Please select an option: "))
      if selection == 5:
        talking = exit(talking)
      elif selection == 1:
        withdrawl_deposit()
      elif selection == 2:
        view_accounts()
      elif selection == 3:
        create_account()
      elif selection == 4:
        help()
      else:
        print("\nI didn't understand that. Please try again.\n")
    except ValueError:
      print("\nI didn't understand that. Please try again.\n")

#the function that runs all of the programs
def chatbot():
  talking = True
  username = ask_username()
  password = ask_password()
  print(f"Hey there, {username}!")
  age = age_finder()
  print(f"\nWelcome to the Bank of Pflugerville assistant! How can I help you today, {username}?\n")
  while talking == True:
    talking = list_of_options(talking)

#the class used to make accounts
class Account:
  def __init__(self, type, amount, name):
    self.account_num = random.randint(1000,5000)
    self.type = type
    self.amount = amount
    self.name = name

  def features(self):
    return {"account_num":self.account_num, 
            "name":self.name,
            "amount":self.amount, 
            "type":self.type,
           }


chatbot()