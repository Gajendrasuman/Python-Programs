import pickle
import os
import random as r
class bank(object):
    def __int__(b):
        b.ac=0
        b.name=""
        b.bal=0
        b.contact=0
        b.email=""
        b.pin=0

    def add_bnk(b):
        b.ac=int(input("Type User Account No. : "))
        b.name=input("Type User Name : ")
        b.bal=int(input("Type User Balance : "))
        b.contact=int(input("Type User Contact No. : "))
        b.email=input("Type User Email Account : ")
        b.pin=r.randint(1000,9999)
        print("Your Pin No. Is : ",b.pin)
    def disp_bnk(b):
        print("Account No. ",b.ac)
        print("Pin No. ",b.pin)
        print("User Name ",b.name)
        print("Balance ",b.bal)
        print("Contact No. ",b.contact)
        print("Email ID ",b.email)
        
              
    def display_bnk(b):
        print("%-6s"%b.ac,"%-10s"%b.name,"%-7s"%b.bal,"%-10s"%b.contact,"%-20s"%b.email,"%-4s"%b.pin)
    def modify_bnk(b):
        b.ac=int(input("Type User Account No. : "))
        
        b.name=input("Type New User Name : ")
        b.bal=int(input("Type Amout : "))
        b.contact=int(input("Type New Contact No. : "))
        b.email=input("Type New Email Account : ")
    def withdraw_bnk():
        b.pin=int(input("Type Pin No. : "))
        bal=int(input("Type Amount To Withdraw : "))
        if (b.bal==0):
            print("Amount Not Available")
        elif(bal<=b.bal):
            b.bal-=bal
            print("Amount Withdraw Successfull")
        else:
            print("Amount Not Available")
    def debit_bnk():
        
        bal=int(input("Type Amount To Deposit : "))
        b.bal+=bal
        print("Amount Deposited Successfuly")
    def bal_bnk():
        print("Balance Available : ","%-7s"%b.bal)        

   
#ADD

def new_bnk():
    try:
        bnk=bank()
        file=open("bank.dat","ab")
        bnk.add_bnk()
        pickle.dump(bnk,file)
        file.close
        print("Bank Account Created Successfuly")
        input("Press Enter To Continue...")
    except:
        pass




#display
def display_ac():
    os.system("cls")
    print(40*"~~~~","\n\n")
    print("                               All Bank Accounts \n\n")
    print(40*"~~~~","\n\n")
    try:
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            bnk.display_bnk()
    except EOFError:
        file.close()
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

# searching Account


def search_ac():
    os.system("cls")
    try:
        z=0
        print(40*"~~~~","\n\n")
        print(2*"~\n")
        print("~                      Search By Account No.                           ~")
        print(2*"~\n")
        print(40*"~~~~","\n\n")
        n=int(input("Type User Account No. : "))
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            if(bnk.ac==n):
                z=1
                print("Account Found")
                bnk.disp_bnk()
    except EOFError:
        file.close()
        if(z==0):
            print("Account Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

#searching Name

def search_name():
    os.system("cls")
    try:
        z=0
        print(40*"~~~~","\n\n")
        print(2*"~\n")
        print("~                      Search By Name                           ~")
        print(2*"~\n")
        print(40*"~~~~","\n\n")
        n=input("Type User Name : ")
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            if(bnk.name.lower()==n.lower()):
                z=1
                print("Account Found")
                bnk.disp_bnk()
    except EOFError:
        file.close()
        if(z==0):
            print("Account Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")



#searching Contact

def search_contact():
    os.system("cls")
    try:
        z=0
        print(40*"~~~~","\n\n")
        print(2*"~\n")
        print("~                      Search By Contact No.                           ~")
        print(2*"~\n")
        print(40*"~~~~","\n\n")
        n=int(input("Type Registered Contact No. : "))
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            if(bnk.contact==n):
                z=1
                print("Account Found")
                bnk.disp_bnk()
    except EOFError:
        file.close()
        if(z==0):
            print("Account Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

#searching Email

def search_email():
    os.system("cls")
    try:
        z=0
        print(40*"~~~~","\n\n")
        print(2*"~\n")
        print("~                      Search By Email ID                           ~")
        print(2*"~\n")
        print(40*"~~~~","\n\n")
        n=input("Type User Email ID : ")
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            if(bnk.email.lower()==n.lower()):
                z=1
                print("Account Found")
                bnk.disp_bnk()
    except EOFError:
        file.close()
        if(z==0):
            print("Account Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")

#search pin

def search_pin():
    os.system("cls")
    try:
        z=0
        print(40*"~~~~","\n\n")
        print(2*"~\n")
        print("~                      Search By Pin No.                           ~")
        print(2*"~\n")
        print(40*"~~~~","\n\n")
        n=int(input("Type User Pin No. : "))
        file=open("bank.dat","rb")
        while True:
            bnk=pickle.load(file)
            if(bnk.pin==n):
                z=1
                print("Account Found")
                bnk.disp_bnk()
    except EOFError:
        file.close()
        if(z==0):
            print("Account Not Available")
        print(40*"~~~~")
        input("Press Enter To Continue...")
    except IOError:
        print("File Not Found")
def modify_ac():
    os.system("cls")
    z=0
    try:
        n=int(input("Type Pin No. : "))
        file=open("bank.dat","rb")
        temp=open("temp.dat","wb")
        while True:
            bnk=pickle.load(file)
            if(bnk.pin==n):
                z=1
                print("Account Found")
                bnk.disp_bnk()
                print("Enter New Data")
                bnk.modify_bnk()
                pickle.dump(bnk,temp)
                print("Account Updated Successfuly")
            else:
                pickle.dump(bnk,temp)
    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Account Not Available")
    except IOError:
        print("File Not Found")
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")

    input("Press Enter To Continue...")

#Delete
        
def del_bnk():
    z=0
    try:
        n=int(input("Type Pin No. : "))
        file=open("bank.dat","rb")
        temp=open("temp.dat","wb")
        while True:
            bnk=pickle.load(file)
            if(bnk.pin==n):
                z=1
                print("Account Found ")
                bnk.disp_bnk()
            else:
                pickle.dump(bnk,temp)
    except EOFError:
        file.close()
        temp.close()
        if(z==0):
            print("Account Not Found")
    except IOError:
        print("File Not Found")
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    input("Press Enter To Continue...")
while True:
    os.system("cls")
    print(40*"~~~~","\n\n")
    print(2*"~\n")
    print("~             Welcome To Bank Of Gajendra                          ~")
    print(2*"~\n")
    print(40*"~~~~","\n\n")
    print("""
1. Add Account
2. Display All Accounts
3. Search By Account No.
4. Search By Pin No.
5. Search By Name
6. Search By Contact No.
7. Search By Email Address
8. Remove Account
9. Exit
""")
    ch=int(input("Type Your Choice : "))
    if(ch==1):
        new_bnk()
    elif(ch==2):
        display_ac()
    elif(ch==3):
        search_ac()
    elif(ch==4):
        search_pin()
    elif(ch==6):
        search_contact()
    elif(ch==7):
        search_email()
    elif(ch==5):
        search_name()
    elif(ch==8):
        del_bnk()
    elif(ch==9):
        
        print(40*"~~~~")
        print("            Thank You For Using My Program         ")
        print(40*"~~~~")
        break
    else:
        print("INVALID CHOICE")
