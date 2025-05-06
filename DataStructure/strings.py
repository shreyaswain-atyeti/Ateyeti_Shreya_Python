#Slicing in Strings
'''
s="Shreya"
print(s[:5]) #will print Shrey
print(s[2:4]) #will print re
print(s[0:]) #will print the whole word
print(s[::-1]) #will print in reverse
print(s[-4:-1]) #will print rey

'''

#Modifying strings

'''
s1="shreya"
s2=" SHREYA! "
s3= "This company's name is Atyeti"
print(s1.upper()) #will print s1 as SHREYA
print(s2.lower()) #will print s2 as shreya
print(s2.strip()) #this will remove whitespace from the start and end
print(s1.replace("e","i")) #this will make the spelling "shriya"
print(s3.split(" ")) #output--['This', "company's", 'name', 'is', 'Atyeti']
'''

#----------------------------------------------------------------------
#String concatenation and formating
'''
a="shreya"
b="swain"
print(a+b) #output--shreyaswain
print(a+" "+b) #output--shreya swain
print(f"My initial name is {a}") #My initial name is shreya
'''

#----------------------------------------------------------------------------

#String Methods
'''
s = "I am based out of Pune location. "
#1--strip()
print(s.strip()) #output--I am based out of Pune location.---it removed the extra space at the end

#2--lower()
print(s.lower()) #output-- i am based out of pune location

#3--upper()
print(s.upper()) #output---I AM BASED OUT OF PUNE LOCATION.

#4--title()--it basically capitalize the first letter of each word
print(s.title()) #output--I Am Based Out Of Pune Location.

#5--capitalize()--will capitalize only the first character
print(s.capitalize()) # output-I am based out of pune location.

#6--replace()
print(s.replace("out","in")) #output--I am based in of Pune location.

#7--find()
print(s.find("based")) # will return the index of "b" that is 5

#8--count()
print(s.count("a")) # output--3

#9--split()--will seperate every element with a ,
print(s.split(" ")) #output---['I', 'am', 'based', 'out', 'of', 'Pune', 'location.', '']

#10- join()--joins elements of the list o the string
words=["In", "India"]
print(s.join(words))

#11--isalpha()
print("shreya".isalpha()) # will give true cuz all the characters are alphabets 


#12--isdigit()
print("1234".isdigit()) #will check for all digits only

#13--startswith()
print(s.startswith("Shreya")) #output will be false
print(s.startswith("I")) #will be true

#14--endswith()
print(s.endswith(" ")) #will give output as true cuz there is a space at the end
'''







