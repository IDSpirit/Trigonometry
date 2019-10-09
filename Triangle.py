#!/usr/bin/env python3

#Code that will give you the side or angle of a triangle that you ask for using trigonometry 
import time #This module brings time in so that there can be timed pauses between messages
import math #This module allows me to use different maths processes that I'll need for this

def redirect(): #This is the redirect function that will be recalled if the user does an incorrect input
    print("\nError: Redirecting you to the start...\n") #An error message comes up
    time.sleep(2) #Then a 2 second timed pause (Roughly)
    first() #And the code goes to the "first" function

def first(): #This is the beginning of the code that the user will see
    ang_side=input('''\nAre you looking for a side or angle:
1: Side
2: Angle
3: Intro
4: Quit- ''') #Here they choose whether they want to find an angle or side
    if ang_side=="1": #If their choice is 1
        side_func() #Then the side function comes up to get the side they want
    elif ang_side=="2": #If their choice is 2
        angle_func() #Then the angle function comes up that works out the angle
    elif ang_side=="3": #Th their choice is 3
        print("\nThis is a program made by me to help me (Or you) to work out the angle or side of a triangle to 'Check' HW answers") #This is a short intro of code
        time.sleep(4)
        first()
    elif ang_side=="4": #Then if they choose to quit (Option 4)
        quit() #The code quits
    else: #However if they type any other incorrect comman (Such as any number that isn't a choice)
        redirect() #The code goes all the way back to the start to do it again

def side_func(): #This is the function for working out a chosen side
    def option2():
        global side #This "global" means that the variable "side" is a global variable 
        side=input('''\nWhat side do you have:
1: Opposite
2: Adjacent
3: Hypotenuse
4: Quit- ''') #I can access the variable from any function which you can't do with a local variable
        try: #This is a try statement that will let me do validation for strings
            if int(side)>4 or int(side)<1: #If find is greater than 4 or less than 1 which it shouldn't
                redirect() #The code redirects to the start
        except ValueError: #However if they input something other than an integer and is invalid (Like a string)
            redirect() #The code will also redirect
        if side=="4": #If the user's choice is 4 for this menu
            quit() #The code quits
        else: #Otherwise if they haven't chosen to quit
            option4() #They carry on to the next part of the code

    def option4():
        global side_num #I've made "side_num" a global variable so I can use it later on
        side_num=float(input("\nWhat's the size of this side- ")) #The user is asked the size of the side they chose
        global unit #"unit" is a global variable too 
        unit=input("\nWhat's the unit you're using- ") #This will ask the unit that the user wants the answer in
        option1() #Then the code goes to the next section

    def option1():
        global find #"find" is also a global variable so I can use it in another function
        find=input('''\nWhat side are you looking for:
1: Opposite
2: Adjacent
3: Hypotenuse
4: Quit- ''') #The user chooses what side that they want to work out
        try: #I've used the try statement again here to validate this section of the code
            if int(find)>4 or int(find)<1: #If side is greater than 4 or less than 1
                redirect() #Then the code quits
        except ValueError: #Also if the input is a string which it shouldn't
            redirect() #The code will redirect
        if find=="1": #If the user chose the first option for the "find" menu
            side_name="opposite" #Then a variable "side_name" is made which is called "opposite" (The angle the user wants to find)
            option3() #And the user goes onto the next part
        elif find=="2": #If the "find" variable is 2
            side_name="adjacent" #Then "side_name" becomes "adjacent"
            option3() #And the code continues
        elif find=="3": #Or if they chose 3
            side_name="hypotenuse" #The variable is called "hypotenuse"
            option3() #And the code continues
        elif side==find: #If the side they want and the side they have are the same which they shouldn't
            redirect() #The code goes back to the start
        elif find=="4": #Also if they want to quit
            quit() #The code quits
        else: #Otherwise if they've done their choice right 
            redirect() #The user is redirected to the start

    def option3():
        global angle #The angle that they have is also a global variable
        angle=float(input("\nWhat is the angle that you have (Write nom. only): ")) #The user is asked what angle they have (Barring the 90 degrees right angle)
        try: #Validation for the angle of the triangle
            if int(angle)>89 or int(angle)<1: #If their input is more than 89 or less than 1 which it shouldn't
                redirect() #The code redirects
        except ValueError: #Or if they inputted an invalid input
            redirect() #The code will also redirect

        if side=="1" and find=="2": #If the side they have is the opposite and the side they want is the adjacent
            answer=float(side_num/math.tan(math.radians(angle))) #The answer is worked out (The math.radians converts the answer from degrees to radians)
            print("\nThe opposite side will be " + str(answer) + str(unit) + ", see that skill lad, don't even watch") #Then the answer is printed
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif side=="1" and find=="3": #If the side they have is the opposite and the side they want is the hypotenuse
            answer=float(side_num/math.sin(math.radians(angle))) #The answer is worked out 
            print("\nThe opposite side will be " + str(answer) + str(unit) + ", can't believe me? Well it's just skill") #Then the answer outputs
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif side=="2" and find=="1": #If the side they have is the adjacent and the side they want is the opposite
            answer=float(side_num*math.tan(math.radians(angle))) #The answer is worked out 
            print("\nThe adjacent side will be " + str(answer) + str(unit) + ", bantz, don't even tell me I'm wrong lad") #Then the answer outputs
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif side=="2" and find=="3": #If the side they have is the adjacent and the side they want is the hypotenuse
            answer=float(side_num/math.cos(math.radians(angle))) #The answer is worked out 
            print("\nThe adjacent side will be " + str(answer) + str(unit) + ", what a cheeky ballhead") #Then the answer outputs
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif side=="3" and find=="1": #If the side they have is the hypotenuse and the side they want is the opposite
            answer=float(side_num*math.sin(math.radians(angle))) #The answer is worked out 
            print("\nThe adjacent side will be " + str(answer) + str(unit) + ", wow what a lucky guess") #Then the answer outputs
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif side=="3" and find=="2": #If the side they have is the hypotenuse and the side they want is the adjacent
            answer=float(side_num*math.cos(math.radians(angle))) #The answer is worked out 
            print("\nThe adjacent side will be " + str(answer) + str(unit) + ", I recommend you check the result, not that I'm wrong or anything") #The answer outputs
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu

    option2() #This starts the first function within the "side_func"

def angle_func(): #This is the function for working out an angle
    def work_angle(): #I did the functions back to front (Reverse chronological order) so that I can define them before I call them
        if opp=="1" and adj=="1": #If they chose both the opposite and the adjacent as the sides that they have
            a=opp1/adj1 #The variable "a" is the opposite side divided by the adjacent side
            answer=float(math.degrees(math.atan(a))) #Then the "answer" variable is the inverse tan of "a"
            print("The angle you want is " + str(answer) + "°, my 'brain' is maaaaad") #The answer is outputted with a cheeky message
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif opp=="1" and hyp=="1": #If they chose both the opposite and the hypotenuse as the sides that they have
            a=opp1/hyp1 #The variable "a" is the opposite side divided by the hypotenuse side
            answer=float(math.degrees(math.asin(a))) #Then the "answer" variable is the inverse sin of "a"
            print("The angle you want is " + str(answer) + "°, check me on a roll") #The answer is outputted 
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu
        elif adj=="1" and hyp=="1": #If they chose both the adjacent and the hypotenuse as the sides that they have
            a=adj1/hyp1 #The variable "a" is the adjacent side divided by the hypotenuse side
            answer=float(math.degrees(math.acos(a))) #Then the "answer" variable is the inverse cos of "a"
            print("The angle you want is " + str(answer) + "°, solid lad") #The answer is outputted 
            print("---------------------------------------------------------------------------------------------------------------------------------") #A break is made
            time.sleep(3) #And a 3 second timed pause is made for the user to read the answer
            first() #Then the code goes all the way back to the beginning at the first menu

    def hypotenuse(): #This is the hypotenuse function to ask if the user has the hypotenuse
        global hyp #I made "hyp" a global variable so that I can use it again outside this function for working out the angle
        hyp=input('''\nDo you have a hypotenuse side:
1: Yes
2: No
3: Quit- ''') #The "hyp" variable is the choice that the user puts in
        try: #This is a "Try" statement
            if int(hyp)>3 or int(hyp)<0: #If the score is more than 3 or less than 0 (Which it shouldn't)...
                redirect() #...then the user is taken back to the start
        except ValueError: #However if there is an exception (Such as if the input to score is a string or float and not integers)...
            redirect() #...then the user is taken back to the start 
        if hyp=="3": #If the user's choice was 3 
            quit() #The code quits like they want it too
        elif hyp=="1": #If their choice was 1
            global hyp1 #"hyp1" is made into a global variable
            hyp1=float(input("\nWhat's the size of this hypotenuse side- ")) #The user is asked the size of the side they chose
            work_angle() #Then the code goes to the function that works out the angle
        elif hyp=="2" and adj=="2" or hyp=="2" and opp=="2": #If the user's choices to the hypotenuse and either the opposite or adjacent are both no
            redirect() #The code redirects
        else: #Otherwise 
            work_angle() #The code goes to the angle function

    def adjacent(): #This is the adjacent function to ask if the user has the adjacent side
            global adj #"hyp" was also made into a global variable so that I can use it outside this function
            adj=input('''\nDo you have an adjacent side:
1: Yes
2: No
3: Quit- ''') #The "adj" variable is the choice that the user puts in
            try: #This is a "Try" statement
                if int(adj)>3 or int(adj)<0: #If the score is more than 3 or less than 0 (Which it shouldn't)...
                    redirect() #...then the user is taken back to the start
            except ValueError: #However if there is an exception (Such as if the input to score is a string or float and not integers)...
                redirect() #...then the user is taken back to the start 
            if adj=="3": #If the user's choice was 3 
                quit() #The code quits like they want it too
            elif adj=="2" and opp=="2": #However if the user doesn't have both the adjacent and the opposite
                redirect() #The code redirects 
            elif adj=="2" and opp=="1": #And if the adjacent is
                hypotenuse()
            else: #If they chose 1 (The only other possible choice)
                global adj1 #"adj1" is made into a global variable
                adj1=float(input("\nWhat's the size of this adjacent side- ")) #The user is asked the size of the side they chose
                if opp=="1" and adj=="1": #Also if the user has both the opposite and the adjacent side
                    work_angle() #The code won't go onto the hypotenuse function and will go straight to the function that works out the angle
                elif opp=="2" and adj=="1": #Also if the user doesn't have the opposite side and has the adjacent angle
                    hypotenuse() #The code goes to the hypotenuse function
            
    def opposite(): #This is the opposite function for seeing if the user has the opposite side
        global opp #"opp" is also a global variable sfor use outside the function 
        opp=input('''\nDo you have an opposite side:
1: Yes
2: No
3: Quit- ''') #The "opp" variable is the choice that the user puts in
        try: #This is a "Try" statement
            if int(opp)>3 or int(opp)<0: #If the score is more than 3 or less than 0 (Which it shouldn't)...
                redirect() #...then the user is taken back to the start
        except ValueError: #However if there is an exception (Such as if the input to score is a string or float and not integers)...
            redirect() #...then the user is taken back to the start 
        if opp=="3": #If the user's choice is 3
            quit() #Then the code quits in accordance with the user's wishes
        elif opp=="2": #If the user's choice is 2 instead
            adjacent() #The adjacent function is done
        elif opp=="1": #If the user's choice is 1
            global opp1 #"adj1" is made into a global variable
            opp1=float(input("\nWhat's the size of this opposite side- ")) #The user is asked the size of the side they chose
            adjacent() #Then the code moves on to the adjacent function
        else: #Otherwise if they didn't choose any of these options
            redirect() #The code redirects to the start

    opposite() #The opposite function starts the angle_func 
                             
first() #This starts the entire code from the first menu
