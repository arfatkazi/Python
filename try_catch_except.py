try:
    numbers = int(input("Enter a number you want: "))
    print(1/numbers)
except ZeroDivisionError:
    print("You can't divide with zero!")
except ValueError:
    print("Enter only number please!")
except TypeError:
    print("you can't  enter any other value!")
finally:
    print("Do some cleanup here!")

