import random
import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'user_account', password = 'ch0psh0P!')

cursor = connection.cursor()

"""addData = ("INSERT INTO accounts (account_id, account_name, account_value, user_email) VALUES (FLOOR(RAND() * (1000 - 1 + 1)) + 1, 'account', 3668, 'john@gmail.com')")

cursor.execute(addData)

testQuery = ("SELECT * FROM accounts")

cursor.execute(testQuery)


###All of this comment is just me testing out MySQL and the functions surrounding it, very useful for me to test before really coding!###


for item in cursor:

    print(item)"""





#used as a placeholder for unused actions, no longer in use
def unfinished():
  print("Currently unfinished, this is a placeholder.")

#displays user's choices
def display_choices():
  print("1. Withdrawl or Deposit")
  print("2. View Existing Accounts")
  print("3. Create New Account")
  print("4. Help")
  print("5. Exit\n")

#will let you change the amount in an account, was very simple to do since I had just completed my create account function, so I just recycled the use of using a paramater as a second execute from the cursor.execute command.
def withdrawl_deposit():
  view_accounts()
  chosen_account_id = input("Please enter the ID of an account.")
  chosen_value = input("What value would you like to set your account to?")
  changeValue = ("update accounts set account_value=%s where account_id = %s")
  valueParam = (chosen_value,chosen_account_id)
  cursor.execute(changeValue,valueParam)


#will show you the accounts, very simple and just using the code provided from the canvas page.
def view_accounts():
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  testQuery = ("SELECT * FROM accounts")
  cursor.execute(testQuery)
  for item in cursor:
    print(item)
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#will let you create accounts. Took me A LOT of trial and error, but eventually I was able to figure out (with some help from stack overflow) that f strings would not help me in this situation and I should instead use placeholders in the mySQL language and then fill them in with a second command in python, filling up the table and pushing it onto the database! I had a ton of fun and I am beginning to love coding with MySQL and python.
def create_account():
  user_account_id = random.randint(1,1000)
  user_account_name = input("What would you like to name the account?")
  initial_account_value = input("What would you like the starting balance to be?")
  user_chosen_email = input("What email would you like to use for this account?")
  addData = ("INSERT INTO accounts (account_id, account_name, account_value, user_email) VALUES (%s, %s, %s, %s)")
  params = (user_account_id, user_account_name, initial_account_value, user_chosen_email)
  cursor.execute(addData,params)

  
  
  """addData = (f"INSERT INTO accounts (account_id, account_name, account_value, user_email) VALUES (FLOOR(RAND() * (1000 - 1 + 1)) + 1,{user_account_name} , {initial_account_value}, {user_chosen_email})")
  cursor.execute(addData)"""



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

#will display list of options. Very simple list that simply displays the options provided.
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

#the function that runs all of the programs. It uses a while loop to continue to show the user the menu in all of it's glory.
def chatbot():
  talking = True
  username = input("Name?")
  print(f"\nWelcome to the Bank of Pflugerville assistant! How can I help you today, {username}?\n")
  while talking == True:
    talking = list_of_options(talking)


chatbot()

connection.commit()

cursor.close()

connection.close()