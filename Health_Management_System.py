import time


def curnttime():
    localtime = time.asctime(time.localtime(time.time()))
    return localtime


print("_____Welcome_____")
print("\n")

print("Keys for updating files are ::\n"
      "1 : Aditya\n"
      "2 : Harry\n"
      "3 : Rohan\n")
print("Keys for updating files ::\n"
      "A : Diet\n"
      "B : Exercise\n")


user_inp = int(input("Enter Number to update the file :: "))

if user_inp == 1:
    adi_upd = input("What do u want to update for Aditya :: ")
    if adi_upd == "a" or adi_upd == "A":
        f = open("Aditya_Diet.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")

    elif adi_upd == "b" or adi_upd == "B":

        f = open("Aditya_Exercise.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")
    else:
        print("___Error___(Invalid Input)")


elif user_inp == 2:
    har_upd = input("What do u want to update for Harry :: ")
    if har_upd == "a" or har_upd == "A":

        f = open("Harry_Diet.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")
    elif har_upd == "b" or har_upd == "B":

        f = open("Harry_Exercise.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")

    else:
        print("___Error___(Invalid Input)")

elif user_inp == 3:
    roh_upd = input("What do u want to update for Rohan:: ")
    if roh_upd == "a" or roh_upd == "A":
        f = open("Rohan_Diet.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")

    elif roh_upd == "b" or roh_upd == "B":
        f = open("Rohan_Exercise.txt", "a")
        a = f.write(f"{curnttime()} :")
        b = input("Start Updating ::")
        c = f.write(b)
        d = f.write("\n")
        print("______File Successfully updated______")

    else:
        print("___Error___(Invalid Input)")

else:
    print("___Error___(Invalid Input)")

print("\n"
      "\n"
      "\n"
      "\n")
print("Health Management System Created by :: ADITYA PHADTARE")