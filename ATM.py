balance = 20000
pin = 2004

print("======================================")
print("           WELCOME TO ATM             ")
print("======================================")

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:

    print("\nLogin Successful!")

    while True:

        print("\n========== ATM MENU ===========")
        print("1. Check Balance")
        print("2. Withdram Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")
        print("=================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nYour balance is:", balance)

        elif choice == 2:

            amount = int(input("Enter withdrawal amount."))

            if amount <= 0:
                print("Enter a valid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", balance)

        elif choice == 3:
            
            amount = int(input("Enter deposit amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            else:
                balance += amount
                print("Money deposited successfully.")
                print("Updated balance:", balance)

        elif choice == 4:

            old_pin = int(input("Enter your current PIN: "))

            if old_pin == pin:

                new_pin = int(input("Enter your new PIN: "))

                if 1000 <= new_pin <= 9999:
                    pin = new_pin
                    print("PIN change successfully.")
                else:
                    print("PIN must contain 4 digits.")

            else:
                print("Incorrect PIN.")

        elif choice == 5:

            print("\nThank you for using the ATM!")
            break

        else:

            print("Invalid choice.")

else:

    print("Incorrect PIN.")
            