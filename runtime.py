x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong')
except RuntimeError :
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')



while True:
    try:
        x = int(input("Please enter a number: "))
        print("You've entered a number" + str(x))
        break
    except ValueError:
        print("The value you entered is not a valid number try again")
