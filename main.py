menu = True
while menu: 
    print("Welcome to multitasking calculator!")
    print("~Menu~")
    print("1| Calculator \n"
        "2| Even or Odd \n"
        "3| Time-to-time \n" 
        "4| Factorial \n"
        "5| Physics \n"
        "0| About program")
    ch = input("Do your choose(num): ")
    print(" ")

    if ch == "1" :
        want = input("Are you want to infinity calculator?[y/n] ")
        print("Operators: \n"
        "+ - plus\n"
        "- - minus\n"
        "* - multiplication\n"
        "/ - division\n"
        "** - raising to a power")
        if want == "y" :
            print("For end press ctrl+c \n")
            while True: print(eval(input('>>>')))
        elif want == "n" :
             print(eval(input('>>>')))
        else :
            print("Error in y/n")
    elif ch == "2" :
        chnum = int(input("Enter an integier: ")) 
        if chnum%2 == 0 :
            print("even")
        else :
            print("odd")

    elif ch == "3" :
        print("/-SubMenu\ ")
        print("!Time-to-time!")
        print("1| Time-to-milliseconds\n"
               "2| Time-to-seconds\n"
               "3| Time-to-minutes\n"
                "4| Time-to-hours\n"
                "5| Time-to-days")
        chy = input("Do your choose(num): ")
        if chy == "1" :
            print("-SubMenu-\n"
                "!Time-to-milliseconds!")
            print("1| Seconds-to-milliseconds\n"
                "2| Minutes-to-milliseconds\n"
                "3| Hours-to-milliseconds\n"
                "4| Days-to-milliseconds")
            chmil = input("Do your choose(num): ")
            time = int(input("Input time(int): "))
            print(" ")
            if chmil == "1" :
                print("Seconds-to-milliseconds is " + str(time*1000)+ " milliseconds")
            elif chmil == "2" :
                print("Minutes-to-milliseconds is " + str(time*6000)+ " milliseconds")
            elif chmil == "3" :
                print("Hours-to-milliseconds is " + str(time*3600000)+ " milliseconds")
            elif chmil == "4" :
                print("Days-to-milliseconds is " + str(time*86400000) + " milliseconds")
            else :
                print("Error")
        elif chy == "2" :
            print("-SubMenu-\n"
                "!Time-to-seconds!")
            print("1| Milliseconds-to-seconds\n"
                "2| Minutes-to-seconds\n"
                "3| Hours-to-seconds\n"
                "4| Days-to-seconds")
            chmil = input("Do your choose(num): ")
            time = int(input("Input time(int): "))
            print(" ")
            if chmil == "1" :
                print("Millisecond-to-seconds is " + str(float(time/1000))+ " seconds")
            elif chmil == "2" :
                print("Minutes-to-seconds is " + str(time*60)+ " seconds")
            elif chmil == "3" :
                print("Hours-to-seconds is " + str(time*3600)+ " seconds")
            elif chmil == "4" :
                print("Days-to-seconds is " + str(time*86400) + " seconds")
            else :
                print("Error")
        elif chy == "3" :
            print("-SubMenu-\n"
                "!Time-to-minutes!")
            print("1| Milliseconds-to-minutes\n"
                "2| Seconds-to-minutes\n"
                "3| Hours-to-minutes\n"
                "4| Days-to-minutes")
            chmil = input("Do your choose(num): ")
            time = int(input("Input time(int): "))
            print(" ")
            if chmil == "1" :
                print("Millisecond-to-minutes is " + str(float(time/60000))+ " minutes")
            elif chmil == "2" :
                print("Seconds-to-minutes is " + str(float(time/60))+ " minutes")
            elif chmil == "3" :
                print("Hours-to-minutes is " + str(time*60)+ " minutes")
            elif chmil == "4" :
                print("Days-to-minutes is " + str(time*1440) + " minutes")
            else :
                print("Error")
        elif chy == "4" :
            print("-SubMenu-\n"
                "!Time-to-hours!")
            print("1| Milliseconds-to-hours\n"
                "2| Seconds-to-hours\n"
                "3| Hours-to-hours\n"
                "4| Days-to-hours")
            chmil = input("Do your choose(num): ")
            time = int(input("Input time(int): "))
            print(" ")
            if chmil == "1" :
                print("Millisecond-to-hours is " + str(float(time/36000000))+ " hours")
            elif chmil == "2" :
                print("Seconds-to-hours is " + str(float(time/3600))+ " hours")
            elif chmil == "3" :
                print("Minutes-to-hours is " + str(float(time/60))+ " hours")
            elif chmil == "4" :
                print("Days-to-hours is " + str(time*24) + " hours")
            else :
                print("Error")
        elif chy == "5" :
            print("-SubMenu-\n"
                "!Time-to-days!")
            print("1| Milliseconds-to-days\n"
                "2| Seconds-to-days\n"
                "3| Hours-to-days\n"
                "4| Days-to-days")
            chmil = input("Do your choose(num): ")
            time = int(input("Input time(int): "))
            print(" ")
            if chmil == "1" :
                print("Millisecond-to-days is " + str(float(time/86400000))+ " days")
            elif chmil == "2" :
                print("Seconds-to-days is " + str(float(time/86400))+ " days")
            elif chmil == "3" :
                print("Minutes-to-days is " + str(float(time/1440))+ " days")
            elif chmil == "4" :
                print("Hours-to-days is " + str(float(time/24)) + " days")
            else :
                print("Error")
            
    elif ch == "4" :
        print('Factorial:',eval(str([i for i in range(1,int(input('number -> '))+1)]).replace(', ','*')[1:-1]))
    elif ch == "5" :
        print("-SubMenu-\n"
              "!Physic!\n")
        print("1| Speed, distance, time")
        chp = input("Do your choose(num): ")
        if chp == "1" :
            print("~Speed, distance, time")
            print("1| Speed\n"
                  "2| Distance\n"
                  "3| Time")
            chp1 = input("Do your choose: ")
            if chp1 == "1" :
                print("=Speed=")
                s = float(input("Enter a distance(meter): "))
                t = float(input("Enter a time(seconds): "))
                v = s/t
                print("Speed equals " + str(v) + " m/s")
            elif chp1 == "2" :
                print("=Distance=")
                v = float(input("Enter a speed(m/s): "))
                t = float(input("Enter a time(seconds): "))
                s = v*t
                print("Distance equals " + str(s) + " meters")
            elif chp1 == "3" :
                print("=Time=")
                v = float(input("Enter a speed(m/s): "))
                s = float(input("Enter a distance(meters): "))
                t = s/v
                print("Time equals " + str(t) + " seconds")
            else :
                print("Error")

    elif ch == "0" :
        print(" |About program| \n"
            "   Version: pre1.2 \n"
            "   Changes: \n"
            "   Added: Physic\n"
            "   Creator: Dimonchikous")
    else :
        print("Error")
    print(" ")
    print("Are you want continue?")
    cont = input("[y/n] ")
    if cont == "y" :
        continue
    elif cont == "n":
        break
    else :
        print("Error, exiting...")
        break
