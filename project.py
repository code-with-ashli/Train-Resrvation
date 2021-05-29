#Train Ticket Reservation Ssytem Brought To You By: CODE WITH ASHLI
#Working on Basic Structure
#Use this credentials for login
#username: admin
#password: ashli

import os 
import random

def main():                                                            #Main page
    os.system('cls')
    print("\t\t ================================================")
    print("\t\t||                                              ||")
    print("\t\t||                                              ||")
    print("\t\t||      ----------TRAIN TICKET--------------    ||")
    print("\t\t||      --------RESERVATION SYSTEM----------    ||")
    print("\t\t||                                              ||")
    print("\t\t||                                              ||")
    print("\t\t||              BROUGHT TO YOU BY               ||")
    print("\t\t||          |   CODE WITH ASHLI   |           ||")
    print("\t\t ================================================")

    print("\n                             Press Enter To Continue ")
    cls = input('')
    os.system('cls')
    login()
    home()
    
    
    # def info():
    # Name=str(input("Name: "))
    # Train_num=int(input("Train Number: "))
    # Number_of_seats=int(input("Number of Seats: "))
    # def switch_demo(menu_choice):
    #     switcher = {
    #         1:Reservation(),
    #         2:View_details(),
    #         3:Cancle(),
    #         4:End(0)
    #     }
    #info()
    #os.system('cls')
def login():                                                                      #To login into program
    a=0
    while True:
        os.system('cls')
        print("\n=========================LOGIN FORM============================")
        username=str(input("\n                     ENTER USERNAME:-"))
        password=str(input("\n                     ENTER PASSWORD:-"))
        print("\n===============================================================")
        if ((username=="admin") and (password=="ashli")):
            print("\n\n\tWELCOME TO OUR SYSTEM!! YOUR LOGIN IS SUCCESSFUL")
            print("\n                     Press Enter To Continue  ")
            cls = input('')
            os.system('cls')
            break
        else:
            print("\n\tYOU HAVE ENTERED WRONG CREDENTIALS")
            print("\n\t Press Enter To Continue ")
            cls = input('')
            a+=1
        if a==4:
            print("\tYou've enetered wrong password 4 times! Session Over!!")
            print("\n \t Press Enter To Continue ")
            cls = input('')
            os.system('cls')

def home():                                                        #Homepage of the profram
    os.system('cls')
    print("  ===========================================")
    print("||                                            ||")
    print("||            TRAIN RESERVATION SYSTEM        ||")
    print("||                                            ||")
    print("  ===========================================")
    print("\n 1>>  Reserve A TICKET")
    print("\n-----------------------")
    print("\n 2>>  Views All Available Trains ")
    print("\n----------------------------------")    
    print("\n 3>>  Cancle Reservation")
    print("\n-------------------------")    
    print("\n 4>>  Exit")
    print("\n-----------")
    menu_choice=int(input("-->"))
    if menu_choice==1:
        Reservation()
    elif menu_choice==2:
        View_details()
        print("\n Press Enter to Return To Main Menu ")
        cls = input('')
        home()
    elif menu_choice==3:
        Cancel()
    elif menu_choice==4:
        exit()
    else:
        print("Invalid Responce")

def Reservation():                                   #Do your reservation
    os.system('cls')
    print("******************************")
    name=str(input("\nENTER YOUR NAME: "))
    print("\n******************************")
    seats=int(input("\nENTER Number of Seats: "))
    if seats==1:
        print("")
    elif seats==2:
        print("\n******************************")
        name1=str(input("\nEnter Name of copassenger:"))
    elif seats==3:
        print("\n******************************")
        name1=str(input("\nEnter Name of Copassenger 1:"))
        name2=str(input("\nEnter Name of Copassenger 2:"))
    elif seats==4:
        print("\n******************************")
        name1=str(input("\nEnter Name of Copassenger 1:"))
        name2=str(input("\nEnter Name of Copassenger 2:"))
        name3=str(input("\nEnter Name of Copassenger 3:"))
    else:
        print("You can reserve only 3 Copassenger")
    print("\n<<  Press Enter To Check Available Trains  >>")
    cls=input('')
    os.system('cls')
    View_details()
    b=1
    while True:
        train_number=int(input("\n>>>>>  Enter Train Number: "))
        if ((train_number>=1001) and (train_number<=1008)):
            charges=charge(train_number,seats)
            printticket(name,seats,train_number,charges)
        else:
            print("Please Enter Train No. From Available List")
            b+=1
            print("\nPrss Enter To Try Again")
            cls = input('')
            os.system('cls')
            View_details()
        if b==3:
            print("You cross the attempt limit")
            print("\nPress Enter To Return To Main Menu")
            cls = input('')
            home()



    #  def co_passenger_name(seats):
    #      if seats==2:
    #          print("Name Copassenger 1:",str(name1))
    #      elif seats==3:
    #          print("Name Copassenger 1:",str(name1))
    #          print("Name Copassenger 2:",str(name2))
    #      elif seats==4:
    #          print("Name Copassenger 1:",str(name1))
    #          print("Name Copassenger 2:",str(name2))
    #          print("Name Copassenger 3:",str(name3))

def charge(train_number,seats):                   #Calculate Your charges
    if train_number==1001:
        return 300*seats
    if train_number==1002:
        return 300*seats
    if train_number==1003:
        return 700*seats
    if train_number==1004:
        return 700*seats
    if train_number==1005:
        return 1500*seats
    if train_number==1006:
        return 1500*seats
    if train_number==1007:
        return 7000*seats
    if train_number==1008:
        return 7000*seats

def printticket(name,seats,train_number,charges):     #Print Ticket
    os.system('cls')
    print("=======================================")
    print("-----------------TICKET----------------")
    print("---------------------------------------")
    print("Name                ",str(name))
    # co_passenger_name()
    print("Seats:              ",int(seats))
    pnr=random.randint(8000000001,8999999999)
    print("PNR:                ",int(pnr))
    print("Train Number:       ",int(train_number))
    specific_train(train_number)
    print("Total Fair:         ",float(charges))
    print("=======================================")
    confirm=str(input("\nPlease Confirm Your Reservation[y/n]: "))
    print("\n=======================================")
    if confirm=='y':
        print("\nCongratulation!!! Reservation Done")
        print("=======================================")
    else:
        print("\nReservation cancelled")
        print("=======================================")
    print("\nPress Enter To Return To Main Menu")
    cls = input('')
    home()


def specific_train(train_number):                #Print Ticket Subfunction
    if train_number==1001:
        print("Train Name:          Red Line Express")
        print("From:                Stanford")
        print("To:                  Fremont")
        print("Distance(Miles):     13")
        print("Departure:           7.00")
    elif train_number==1002:
        print("Train Name:          Red Line Express")
        print("From:                Fremont")
        print("To:                  Stanford")
        print("Distance(Miles):     13")
        print("Departure:           10.00")
    elif train_number==1003:
        print("Train Name:          Oakland Express")
        print("From:                Stanford")
        print("To:                  Fremont")
        print("Distance(Miles):     13")
        print("Departure:           8.00")
    elif train_number==1004:
        print("Train Name:          Oakland Express")
        print("From:                Stanford")
        print("To:                  Fremont")
        print("Distance(Miles):     13")
        print("Departure:           12.00")
    elif train_number==1005:
        print("Train Name:          Golden Gate Express")
        print("From:                Stanford")
        print("To:                  Fremont")
        print("Distance(Miles):     3")
        print("Departure:           10.00")
    elif train_number==1006:
        print("Train Name:          Golden Gate Express")
        print("From:                Stanford")
        print("To:                  Fremont")
        print("Distance(Miles):     13")
        print("Departure:           16.00")
    elif train_number==1007:
        print("Train Name:          White Sand Express")
        print("From:                San Francisco")
        print("To:                  San Diego")
        print("Distance(Miles):     500")
        print("Departure:           09.00")
    elif train_number==1008:
        print("Train Name:          White Sand Express")
        print("From:                San Diego")
        print("To:                  San Francisco")
        print("Distance(Miles):     500")
        print("Departure:           18.00")



def View_details():             #See train Timetable
    os.system('cls')
    print("\n-----------------------------------------------------------------------------------------------------------------------------------")
    print("\nTr.no.\tName\t\t\tFrom\t\t  To\t\tDistance(Miles)\t\tDepature\t\tCharges")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------")
    print("\n1001 \tRed Line Express\tStanford\t  Fremont\t\t13\t\t07.00\t\t\tRs. 300")
    print("\n1002 \tRed Line Express\tFremont\t\t  Stanford\t\t13\t\t10.00\t\t\tRs. 300")
    print("\n1003 \tOakland Express\t\tStanford\t  Oakland\t\t27\t\t08.00\t\t\tRs. 700")
    print("\n1004 \tOakland Express\t\tOakland\t\t  Stanford\t\t27\t\t12.00\t\t\tRs. 700")
    print("\n1005 \tGolden Gate Express\tStockton\t  San Francisco\t\t84\t\t10.00\t\t\tRs. 1500")
    print("\n1006 \tGolden Gate Express\tSan Francisco\t  Stockton\t\t84\t\t16.00\t\t\tRs. 1500")
    print("\n1007 \tWhite Sand Express\tSan Francisco\t  San Diego\t\t500\t\t09.00\t\t\tRs. 7000")
    print("\n1008 \tWhite Sand Express\tSan Francisco\t  San Diego\t\t500\t\t18.00\t\t\tRs. 7000")
    print("\n-----------------------------------------------------------------------------------------------------------------------------------")

def Cancel():                     #Cancel your reservation
    os.system('cls')
    train_no=int(input("Enter Train No:"))
    pnr=int(input("\nEnter PNR No:"))
    print("------------------------------")
    print("Ticket Cancelled Successfully")
    print("-----------------------------")
    print("\n\t Press Enter To Return To Main Menu")
    cls = input('')
    home()

#I am planned to add options to check seat details and check reservation status but failed to do



if __name__ == '__main__':
    main()