
#def book_ticket(movie, showtime, num_tickets, customer_name, available_seats):
"""Books movie tickets and returns a booking confirmation."""
print("Welcome to 24/7 Entertainment Theatre ")
def Action_Movie ():
    seat=input("enter the seat type to enjoy the movie[balcony,reserved class]:")
    avl_language="telugu","hindi","english"
    language_enter=input("Enter the language that you want to watch [telugu,hindi,english]: ") 
    if language_enter in avl_language:
      print(f"Yes you can enjoy your Movie in {language_enter} language")   
    else:
     print(f"Sorry.. your language : {language_enter} is not avaliable right now :")
     print("select the a language which is avaliable ")
     return
    show= {"morning show","matniee","evening show","late show"}
    showtime=input("enter show time[morning show,matniee,evening show,late show]:")
    if showtime in show:
        print(f"Ok {showtime} show is there..")
    else:
        print(f"{showtime} Invalid showtime.")
        return 
    if seat=="balcony"and showtime:
         print('your seat cost for action movie is 150 Rs per person')
         var=input("do,you want to book this seat:")
         if var=="yes":
             per_person=150
             name=input("enter your full name:")
             num_of_persons=int(input("enter number of persons:"))
             if num_of_persons>=1:
                 print("ok")
             else:
                 print("invalid number..")
                 return
             total_amount=per_person*num_of_persons
             vac=input("do you want vechile parking:")  
         if vac=="yes":
             for_vechile=40
             sum=total_amount+for_vechile
             print(f"Mr/Ms {name} {num_of_persons} ticket is booked for action movie your bill is to pay {sum} ")
         else:
            print(f"Mr/Ms {name} {num_of_persons} ticket is booked for action movie for {showtime} and your total bill is to pay is {total_amount} ")       
         avl_seats_in_balcony=int(input("enter avaliable seats:"))
         diff= avl_seats_in_balcony-num_of_persons 
         if diff>=1:
           print(f"now avaliable seats are {diff} only")         
         else:
             print("Sorry seats are not avaliable right now in balcony")
    elif seat=="reserved clas"and showtime:
        print('your seat cost for action movie is 50 Rs per person')
        var=input("do,you want to book this seat:")
        if var=="yes":
             per_person=50
             name=input("enter your full name:")
             num_of_persons=int(input("enter number of persons:"))
             if num_of_persons>=1:
                 print("ok")
             else:
                 print("invalid number..")
                 return
             total_amount=per_person*num_of_persons
             vac=input("do you want vechile parking:")  
        if vac=="yes":
               for_vechile=40
               sum=total_amount+for_vechile
               print(f"Mr/Ms {name} {num_of_persons} ticket is booked for action movie your bill is to pay {sum} ")
        else:
            print(f"Mr/Ms {name} {num_of_persons} ticket is booked for action movie for {showtime} and your total bill is to pay is {total_amount} ")       
            avl_seats_in_reserved_class=int(input("enter avaliable seats:"))
            diff= avl_seats_in_reserved_class-num_of_persons 
            if diff>=1:
               print(f"now avaliable seats are {diff} only")         
            else:
               print("Sorry seats are not avaliable right now in reserved class")  
    else:
        print("sorry we are aware of this..enter valid entry")
def Comedy_Flick():
    seat=input("enter the seat type to enjoy the movie[balcony,reserved class]:")
    avl_language="telugu","hindi","english"
    language_enter=input("Enter the language that you want to watch [telugu,hindi,english]: ") 
    if language_enter in avl_language:
      print(f"Yes you can enjoy your Movie in {language_enter} language")   
    else:
     print(f"Sorry.. your language : {language_enter} is not avaliable right now :")
     print("select the a language which is avaliable ")
     return
    show= {"morning show","matniee","evening show","late show"}
    showtime=input("enter show time[morning show,matniee,evening show,late show]:")
    if showtime in show:
        print(f"Ok {showtime} show is there..")
    else:
        print(f"{showtime} Invalid showtime.")
        return 
    if seat=="balcony"and showtime:
         print('your seat cost for Comedy Flick is 150 Rs per person')
         var=input("do,you want to book this seat:")
         if var=="yes":
             per_person=150
             name=input("enter your full name:")
             num_of_persons=int(input("enter number of persons:"))
             if num_of_persons>=1:
                 print("ok")
             else:
                 print("invalid number..")
                 return
             total_amount=per_person*num_of_persons
             vac=input("do you want vechile parking:")  
         if vac=="yes":
             for_vechile=40
             sum=total_amount+for_vechile
             print(f"Mr/Ms {name} {num_of_persons} ticket is booked for Comedy Flick your bill is to pay {sum} ")
         else:
            print(f"Mr/Ms {name} {num_of_persons} ticket is booked for Comedy Flick for {showtime} and your total bill is to pay is {total_amount} ")       
         avl_seats_in_balcony=int(input("enter avaliable seats:"))
         diff= avl_seats_in_balcony-num_of_persons 
         if diff>=1:
           print(f"now avaliable seats are {diff} only ")         
         else:
             print("Sorry seats are not avaliable right now in balcony")
    elif seat=="reserved clas"and showtime:
        print('your seat cost for Comedy Flick is 50 Rs per person')
        var=input("do,you want to book this seat:")
        if var=="yes":
             per_person=50
             name=input("enter your full name:")
             num_of_persons=int(input("enter number of persons:"))
             if num_of_persons>=1:
                 print("ok")
             else:
                 print("invalid number..")
                 return
             total_amount=per_person*num_of_persons
             vac=input("do you want vechile parking:")  
        if vac=="yes":
               for_vechile=40
               sum=total_amount+for_vechile
               print(f"Mr/Ms {name} {num_of_persons} ticket is booked for Comedy Flick your bill is to pay {sum} ")
        else:
            print(f"Mr/Ms {name} {num_of_persons} ticket is booked for Comedy Flick for {showtime} and your total bill is to pay is {total_amount} ")       
            avl_seats_in_reserved_class=int(input("enter avaliable seats:"))
            diff= avl_seats_in_reserved_class-num_of_persons 
            if diff>=1:
               print(f"now avaliable seats are {diff} only")         
            else:
               print("Sorry seats are not avaliable right now in reserved class")  
    else:
        print("sorry we are aware of this..enter valid entry")
def Exit():
    print("Yes,The exit door is back ")
def main():
    print("1,Action Movie")
    print("2,Comedy Flick")
    print("3,Exit")
    choose_number=int(input("enter your choice :"))
    if choose_number==1:
        Action_Movie()
    elif choose_number==2:
        Comedy_Flick()
    elif choose_number==3:
        Exit() 
    else:
        print("invalid choise")
main()







