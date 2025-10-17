from simpleeval import simple_eval
menu = True
while menu: 
    print("Welcome to multitasking calculator!")
    print("~Menu~")
    print("1| Calculator \n"
        "2| Even or Odd \n"
        "3| Time-to-time \n" 
        "4| Physics \n"
        "5| Data converter \n"
        "0| About program")
    ch = input("Do your choose(num): ")
    print(" ")
    match ch:
        case "1" :
            want = input("Are you want to infinity calculator?[y/n] ")
            print("Operators: \n"
            "+ - plus\n"
            "- - minus\n"
            "* - multiplication\n"
            "/ - division\n"
            "** - raising to a power")
            if want == "y" :
                print("For end press ctrl+c \n")
                while True: print(simple_eval(input('>>>')))
            elif want == "n" :
                 print(simple_eval(input('>>>')))
            else :
                print("Error in y/n")
        case "2" :
            chnum = int(input("Enter an integier: ")) 
            if chnum%2 == 0 :
                print("even")
            else :
                print("odd")

        case "3" :
            print("/-SubMenu\ ")
            print("!Time-to-time!")
            print("1| Time-to-milliseconds\n"
                   "2| Time-to-seconds\n"
                   "3| Time-to-minutes\n"
                    "4| Time-to-hours\n"
                    "5| Time-to-days")
            chy = input("Do your choose(num): ")
            match chy:
                case "1" :
                    print("-SubMenu-\n"
                        "!Time-to-milliseconds!")
                    print("1| Seconds-to-milliseconds\n"
                        "2| Minutes-to-milliseconds\n"
                        "3| Hours-to-milliseconds\n"
                        "4| Days-to-milliseconds")
                    chmil = input("Do your choose(num): ")
                    time = int(input("Input time(int): "))
                    print(" ")
                    match chmil:
                        case "1" :
                            print("Seconds-to-milliseconds is " + str(time*1000)+ " milliseconds")
                        case "2" :
                            print("Minutes-to-milliseconds is " + str(time*6000)+ " milliseconds")
                        case "3" :
                            print("Hours-to-milliseconds is " + str(time*3600000)+ " milliseconds")
                        case "4" :
                            print("Days-to-milliseconds is " + str(time*86400000) + " milliseconds")
                        case _:
                            print("Error")
                case "2" :
                    print("-SubMenu-\n"
                        "!Time-to-seconds!")
                    print("1| Milliseconds-to-seconds\n"
                        "2| Minutes-to-seconds\n"
                        "3| Hours-to-seconds\n"
                        "4| Days-to-seconds")
                    chmil = input("Do your choose(num): ")
                    time = int(input("Input time(int): "))
                    print(" ")
                    match chmil:
                        case "1" :
                            print("Millisecond-to-seconds is " + str(float(time/1000))+ " seconds")
                        case "2" :
                            print("Minutes-to-seconds is " + str(time*60)+ " seconds")
                        case "3" :
                            print("Hours-to-seconds is " + str(time*3600)+ " seconds")
                        case "4" :
                            print("Days-to-seconds is " + str(time*86400) + " seconds")
                        case _:
                            print("Error")
                case "3" :
                    print("-SubMenu-\n"
                        "!Time-to-minutes!")
                    print("1| Milliseconds-to-minutes\n"
                        "2| Seconds-to-minutes\n"
                        "3| Hours-to-minutes\n"
                        "4| Days-to-minutes")
                    chmil = input("Do your choose(num): ")
                    time = int(input("Input time(int): "))
                    print(" ")
                    match chmil:
                        case "1" :
                            print("Millisecond-to-minutes is " + str(float(time/60000))+ " minutes")
                        case "2" :
                            print("Seconds-to-minutes is " + str(float(time/60))+ " minutes")
                        case "3" :
                            print("Hours-to-minutes is " + str(time*60)+ " minutes")
                        case "4" :
                            print("Days-to-minutes is " + str(time*1440) + " minutes")
                        case _:
                            print("Error")
                case "4" :
                    print("-SubMenu-\n"
                        "!Time-to-hours!")
                    print("1| Milliseconds-to-hours\n"
                        "2| Seconds-to-hours\n"
                        "3| Hours-to-hours\n"
                        "4| Days-to-hours")
                    chmil = input("Do your choose(num): ")
                    time = int(input("Input time(int): "))
                    print(" ")
                    match chmil:
                        case "1" :
                            print("Millisecond-to-hours is " + str(float(time/36000000))+ " hours")
                        case "2" :
                            print("Seconds-to-hours is " + str(float(time/3600))+ " hours")
                        case "3" :
                            print("Minutes-to-hours is " + str(float(time/60))+ " hours")
                        case "4" :
                            print("Days-to-hours is " + str(time*24) + " hours")
                        case _:
                            print("Error")
                case "5" :
                    print("-SubMenu-\n"
                        "!Time-to-days!")
                    print("1| Milliseconds-to-days\n"
                        "2| Seconds-to-days\n"
                        "3| Hours-to-days\n"
                        "4| Days-to-days")
                    chmil = input("Do your choose(num): ")
                    time = int(input("Input time(int): "))
                    print(" ")
                    match chmil:
                        case "1" :
                            print("Millisecond-to-days is " + str(float(time/86400000))+ " days")
                        case "2" :
                            print("Seconds-to-days is " + str(float(time/86400))+ " days")
                        case "3" :
                            print("Minutes-to-days is " + str(float(time/1440))+ " days")
                        case "4" :
                            print("Hours-to-days is " + str(float(time/24)) + " days")
                        case _:
                            print("Error")
                    
        case "4" :
            print("-SubMenu-\n"
                  "!Physic!\n")
            print("1| Speed, distance, time\n"
                  "2| Speed converter")
            chp = input("Do your choose(num): ")
            match chp:
                case "1" :
                    print("~Speed, distance, time")
                    print("1| Speed\n"
                          "2| Distance\n"
                          "3| Time")
                    chp1 = input("Do your choose: ")
                    match chp1:
                        case "1" :
                            print("=Speed=")
                            s = float(input("Enter a distance(meter): "))
                            t = float(input("Enter a time(seconds): "))
                            v = s/t
                            print("Speed equals " + str(v) + " m/s")
                        case "2" :
                            print("=Distance=")
                            v = float(input("Enter a speed(m/s): "))
                            t = float(input("Enter a time(seconds): "))
                            s = v*t
                            print("Distance equals " + str(s) + " meters")
                        case "3" :
                            print("=Time=")
                            v = float(input("Enter a speed(m/s): "))
                            s = float(input("Enter a distance(meters): "))
                            t = s/v
                            print("Time equals " + str(t) + " seconds")
                        case _:
                            print("Error")
                case "2" :
                    print("~Speed converter~")
                    print("1|Knot to m/s\n"
                          "2|m/s to Knot\n"
                          "3|k/h to m/s\n"
                          "4|m/s to k/h")
                    chp2 = input("Do your choose: ")
                    match chp2:
                        case "1" :
                            print("=Knot to m/s=")
                            knot = float(input("Enter a knot: "))
                            v = knot/1.944
                            print("Knot to m/s is equal " + str(v))
                        case "2" :
                            print("=m/s to knot=")
                            v = float(input("Enter a speed(m/s): "))
                            knot = v*1.944
                            print("m/s to knot is equal " + str(knot))
                        case "3" :
                            print("=k/h to m/s=")
                            kv = float(input("Enter a k/h: "))
                            v = kv/3.6
                            print("k/h to m/s is equal: " + str(v))
                        case "4" :
                            print("=m/s to k/h=")
                            v = float(input("Enter a m/s: "))
                            kv = v*3.6
                            print("m/s to k/h is equal: " + str(kv))
                        case _:
                            print("Error")
                case _:
                    print("Error")
        case "5" :
            print("-Submenu-")
            print("ATTENTION! DATA IS IN 1024(kib)")
            print("!Data converter!")
            print("1| Bytes converter") 
            chd = input("Do your choose: ")
            match chd:
                case "1" :
                    print("!Bytes converter!")
                    print("1|B to GiB\n"
                          "2|B to MiB\n"
                          "3|B to kiB\n"
                          "4|B to bits")
                    chd1 = input("Do your choose: ")
                    match chd1:
                        case "1" :
                            print("=byte to Gib=")
                            byte = float(input("Bytes = "))
                            gigabyte = byte/1073741824
                            print("Bytes to GiB = " + str(gigabyte))
                        case "2" :
                            print("=byte to MiB=")
                            byte = float(input("Bytes = "))
                            megabyte = (byte/1024)/1024
                            print("Bytes to MiB = " + str(megabyte))
                        case "3" :
                            print("=byte to kiB")
                            byte = float(input("Bytes = "))
                            kilobytes = byte/1024
                            print("Bytes to kiB = " +str(kilobytes))
                        case "4" :
                            print("=byte to bits=")
                            byte = float(input("Bytes = "))
                            bits = byte*8
                            print("Bytes to bits = " +str(bits))
                        case _:
                            print("ERROR")
                case _:
                    print("ERROR")

        case "0" :
            print(" |About program| \n"
                "   Version:pre-2-1.4 \n"
                "   Changes: \n"
                "   If-elif-else construction replaced by match-case\n"
                "   Creator: Dimonchikous")
        case _:
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
