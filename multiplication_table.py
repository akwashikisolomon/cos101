# VERITAS UNIVERSITY
# Course: COS 101
# Assignment: Multiplication Table Program
# Name: Enter your full name here
# Matric Number: Enter your matric number here

while True:
    number = int(input("Enter a number (5 to stop): "))

    if number == 5:
        print("Program stopped.")
        break

    print("Multiplication Table of", number)

    for i in range(1, 13):
        print(number, "x", i, "=", number * i)
