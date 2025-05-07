try:
    num=int(input("enter-->"))
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("10 can't be divided by 0")
except ValueError:
    print("Enter a number only")
