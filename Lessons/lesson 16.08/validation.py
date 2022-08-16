counter = 3
pin = 4444
blocked = False
while True:
    if counter == 0:
        print("You card is blocked, have a good day")
        blocked = True
        break

    # user_input = input("Please enter the date in the dd/mm/yyyy format:\n")
    pin_answer = input("Enter your pin:\n")

    if len(pin_answer) != 4:
        print("The pin must consist of the 4 digits")
        continue

    if not pin_answer.isdigit():
        print("The pin must consist of some digits only")
        continue

    pin_answer = int(pin_answer)

    if pin_answer != pin:
        counter -= 1
        print(f"The pin is not correct, you have {counter} attempts left")
        continue

    break

if not blocked:
    print("main logic")