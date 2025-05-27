menu = True
while menu: 
    print("Welcome to multitasking calculator!")
    print("~Menu~")
    print("1| Calculator \n"
        "2| Even or Odd \n"
        "3| Time to milliseconds \n" 
        "4| Factorial \n"
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
        print("-SubMenu-\n"
            "!Time to milliseconds!")
        print("1| Seconds to milliseconds\n"
            "2| Minutes to milliseconds\n"
            "3| Hours to milliseconds\n"
            "4| Days to milliseconds")
        chmil = input("Do your choose(num): ")
        time = int(input("Input time(int): "))
        print(" ")
        if chmil == "1" :
            print("Seconds to milliseconds is " + str(time*1000)+ " milliseconds")
        elif chmil == "2" :
            print("Minutes to milliseconds is " + str(time*6000)+ " milliseconds")
        elif chmil == "3" :
            print("Hours to milliseconds is " + str(time*3600000)+ " milliseconds")
        elif chmil == "4" :
            print("Days to milliseconds is " + str(time*86400000) + " milliseconds")
        else :
            print("Error")
    elif ch == "4" :
        print('Factorial:',eval(str([i for i in range(1,int(input('number -> '))+1)]).replace(', ','*')[1:-1])) #copied from browser
    elif ch == "0" :
        print("|About program| \n"
            "Version: 1 \n"
            "Creator: Dimonchikous")
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
