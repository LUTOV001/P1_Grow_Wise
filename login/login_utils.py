import sys
import questionary 

from fileio.csvUtils import *

### NOTES AS OF 20230511 --- if login() is unsuccessful, it still progresses to the risk_score_questionnaire functions

#Check if the user is already registered or not
def validate_user_login_info(username,password):
    user_data=load_file()
    if username in user_data:
        if user_data[username]==password:
            return True
        return False
    return False


def login():
    username=input("Enter your user name:")
    password=input("Enter your Password:")
    if validate_user_login_info(username,password):
        print("login successful")
    else:
        print("login unsuccessful") 

#New User First Time Register\signup.
def register():
    new_user_name=(input("choose your user name:"))
    user_data=load_file()
    if new_user_name in user_data: # currently doesn't account for blank username
        print("This Username already exist")
        return
    new_user_password=(input("choose your Password:"))
    if new_user_password != '':
        append_csv(new_user_name,new_user_password)
    else:
        sys.exit('Password cannot be blank')

      
def opener():
    # will ask question about new user or existing user
    # if new user call register else call login 
    ## future changes will provide users with selectable options to reduce chance of error
    existing_user = input("Are you an existing user? Please enter Y/N\n") # throws error when lower case ;; fixed below
    existing_user = existing_user.upper() # corrects for case issues at input
    if existing_user == 'Y':
        login()
        return True
    elif existing_user =='N':
        register()
    else:
        sys.exit("Sorry, You have entered an incorrect input.")