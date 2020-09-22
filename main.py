option = int(input(
    "1: Ik wil weten hoeveel kluizen nog vrij zijn \n"
    "2: Ik wil een nieuwe kluis  \n"
    "3: Ik wil even iets uit mijn kluis halen  \n"
    "4: Ik geef mijn kluis terug \n"))
file = open("fa_kluizen.txt", "r+")
amountOfLockers = 12
lines = file.readlines()


def show_lockers():
    print("Er zijn {} kluizen vrij\n".format(amountOfLockers - len(lines)))
    return


def new_locker():
    if (amountOfLockers - len(lines)) == 0:
        print("Er zijn geen kluizen meer vrij\n")
        return
    available_numbers = []
    for x in range(amountOfLockers):
        available_numbers.append(x + 1)
        for y in lines:
            if int(y[:2].replace(';', '')) == x + 1:
                available_numbers.remove(x + 1)
    code = input("Voer een code in voor je kluisje\n")
    print("je kunt nu inloggen met je code op kluisje " + str(available_numbers[0]))
    file.write(str(available_numbers[0]) + ";" + code + "\n" )


def open_locker():
    number = input("Voer het nummer in van je kluisje\n")
    code = input("Voer de code in voor je kluisje\n")
    for y in lines:
        line_array = y.split(";", 1)
        if line_array[0] == number and line_array[1].replace("\n", "") == code:
            print("Je kan nu je kluisje openmaken!")
            #             Implement opening locker here
            return
    print("geen kluisje gevonden met deze code")


def return_locker():
    number = input("Voer het nummer in van je kluisje\n")
    code = input("Voer de code in voor je kluisje\n")
    file.seek(0)
    deleted = False
    for y in lines:
        line_array = y.split(";", 1)
        if line_array[0] != number or line_array[1].replace("\n", "") != code:
            file.write(y)
        if line_array[0] == number and line_array[1].replace("\n", "") == code:
            print("Kluisje is vrijgegeven")
            deleted = True
    if not deleted:
        print("geen kluisjes gevonden")
    file.truncate()


if option == 1:
    show_lockers()
elif option == 2:
    new_locker()
elif option == 3:
    open_locker()
elif option == 4:
    return_locker()
else:
    print("invalid option")

file.close()
