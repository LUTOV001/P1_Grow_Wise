# import sys
# import questionary 
import fire
import time 

# Import other functions created in the different file.
# from fileio.csvUtils import *
from login.login_utils import *
from questionnaire.risk_score_questionnaire import *

# Initilizing function --- front door
def run():
    if opener() == True: # Account Registration and Login
        if risk_questions() == True:
            risk_mapping()
            ### this is place holder code for demo in presentation ###
            print('loading suggestions\n')
            time.sleep(1)
            print('.\n')
            time.sleep(1)
            print('.\n')
            time.sleep(1)
            print('.\n')
            time.sleep(1)
            print('.\n')
            time.sleep(1)
        
# First main funtion will run.
if __name__ == "__main__":
    fire.Fire(run) 