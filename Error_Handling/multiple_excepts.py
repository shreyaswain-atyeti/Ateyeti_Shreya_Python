try:
    l=[2,3,4,5,6]
    n=int(input("Enter the index no u want to search-->"))
    print(l[n])

except ValueError:
    print("Please enter a integer value only")
except IndexError:
    print("Please enter a number within the range of the list")
