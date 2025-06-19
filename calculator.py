import os
import time
import cmath

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print("\033[1;32m\n====MENU====")
    print("\033[0;37m 1 - Addition")
    print(" 2 - Subtraction")
    print(" 3 - Multiplication")
    print(" 4 - Division")
    print(" 5 - Exponetiation")
    print(" 6 - Square Root")
    print(" 7 - Quit")

while True:
    clean_screen()
    menu()
    choice = input("\033[1;32mPlease select one option.")

    if choice == "1":
        clean_screen()
        num1 = float(input("Select one number"))
        num2 = float(input("Select another number"))
        result = num1 + num2
        print(f"Your result is {result}")
        print("Press ENTER to return to the menu")
        input()

    elif choice == "2":
        clean_screen()
        num1 = float(input("Select one number"))
        num2 = float(input("Selecet another number"))
        result = num1 - num2
        print(f"Your result is {result}")
        print("Press ENTER to return to the menu")
        input()
    
    elif choice == "3":
        clean_screen()
        num1 = float(input("Select one number"))
        num2 = float(input("Select another number"))
        result = num1 * num2
        print(f"Your result is {result}")
        print("Press ENTER to return to the menu")
        input()

    elif choice == "4":
        clean_screen()
        num1 = float(input("Select one number"))
        num2 = float(input("Select one number"))
        if num2 != 0:
            result = num1 / num2 # Entire value
            remainder = num1 % num2 # Remainder
            print(f"Your result is {result}, with a remainder of {remainder}")
        else:
            print("\033[0;31mError: DIvision by 0!")
        print("Press ENTER to return to the menu")
        input()

    elif choice == "5":
        clean_screen()
        num1 = float(input("Select the base number"))
        num2 = float(input("Select the exponent"))
        result = pow(num1, num2)
        print(f"Your result is {result}")
        print("Press ENTER to return to the menu")
        input()

    elif choice == "6":
        clean_screen()
        num1 = float(input("Calculate the square root of:"))
        result = cmath.sqrt(num1)
        print(f"Your square root is {result}")
        print("Press ENTER to return to the menu")
        input()

    elif choice == "7":
        print("\033[0;31mClosing tab...")
        time.sleep(2)
        break

    else:
        print("\033[0;31mInvalid option!")


