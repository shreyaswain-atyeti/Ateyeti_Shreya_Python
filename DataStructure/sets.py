#creating a set
#1
'''
s=set() #this is an empty set
s.add(9) #to add elements to a set
'''

#2
'''
s={"shreya",20,2,0.6}
print(type(s)) # 2nd way of creating a set
'''

#-------------------------------------------------------------
#if a list alreasy consist duplicates then we can get the unique elementsby using set and then the type of the list will be set
'''
l=[2,2,33,4,33,78,"Shreya",66,"Shreya"] 
l=set(l)
print(l)
print(type(l)) #will be a set now
'''
#------------------------------------------------------------------

#Methods
'''
s= {1,44,77,"Shreya"}
s.add("Swain")
s.update([123,"Atyeti"]) # this will update the list with the elements you give
s.remove("Swain")
print(s) #{1, 'Atyeti', 44, 77, 'Shreya', 123}----got this output
s.pop()
print(s) #{'Shreya', 'Atyeti', 44, 77, 123}----got this output after pop as pop randomly eliminates an element form the set
#s.clear()---this will clear all the elements
'''

#---------------------------------------------------------------------------------------------

#Ops in set

'''
s1={1,2,3,4}
s2={3,4,5,6}

print(s1.intersection(s2)) #this will give the common elements present in both the sets
print(s1.difference(s2))  # the uncommon elements from set s1 wrt to s2
print(s1.union(s2)) #will merge both the sets and give the unique values
'''

#-------------------------------------------------------------------------------



