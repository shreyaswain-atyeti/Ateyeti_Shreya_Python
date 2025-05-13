import random

print(random.randint(1,10)) #will print anything between 1-10
print(random.random()) #this will give any random float number between 0-1

#this one will any random item from this list
names=["shreya","riya","mamata","mami"]
print(random.choice(names))

nums = [1,2,3,4,5,6] #this will shuffle the list 
random.shuffle(nums)
print("Shuffeled dices are: ", nums)
