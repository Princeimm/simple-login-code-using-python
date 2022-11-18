import time 
def login():
    username  = "user" #add your choice username 
    password  = "123"  #add your choice password
    username  =input(">>>>>>> Username :")
    pass_word =input(">>>>>>> Password :")
    if (pass_word == password):
        print(">>>>>>>Verifying.....")
        time.sleep(3.0)
        print(">>>>>>> login successful ")
    else:
        print(">>>>>>> verifying.....")
        time.sleep(3.0)
        print(">>>>>>> Invalid username or data !!")
login()