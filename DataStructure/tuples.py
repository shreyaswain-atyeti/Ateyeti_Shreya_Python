#creating tuple and can not be changed later
'''
t = (1, 2, "Shreya", 3.14)
'''
#---------------------------------------------------------

#indexing
'''
t = (1, 2, "Shreya", 3.14)
print(t[0])
'''
#---------------------------------------------------------

#Slicing
'''
t = (0, 1, 2, 3, 4, 5)

print(t[1:4])     # will print--- (1, 2, 3)
print(t[:3])      # will print--- (0, 1, 2)
print(t[::2])     # will print--- (0, 2, 4)
'''

#--------------------------------------------------------

#Immutability
'''
t = (1, 2, 3)
t[0] = 10   #this will through an error cuz tuples are immutable
'''

#-----------------------------------------------------------------------
#Methods
''''
t=(2,33,2,4,5,2,66,2,78)
print(t.count(2)) #will give the count of occurance of 2
print(t.index(33)) # will give theb index no. where 33 is present
print(t.index(2)) # will give the index of first occurance of 2
'''
#--------------------------------------------------------------------------

#Though tuples does'nt support comprehension still it can be done by using list comprhension and then conversion to tuples
'''
squared = tuple(x**2 for x in range(5))
print(squared)
'''

#-------------------------------------------------------------------------
