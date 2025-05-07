class NegativeAgeError(Exception):
    pass
    
def age(age):
    if age<0:
        raise NegativeAgeError("Negative ages can not be given")
    print(f"Age is set to {age}")

try:
    age(-5)
except NegativeAgeError as e:
    print(f"Custom error: ",e)



    