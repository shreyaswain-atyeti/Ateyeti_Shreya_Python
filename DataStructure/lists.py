#creation
#1
'''
l=[] #can create an empty list and later on add th elements using list.append()
l.append("Shreya")
l.append(1149)
l.append(1.1)
'''
#2
''''
l=[22,34,"Swain",0.9]
'''

#------------------------------------------------------------------------------------

#Indexing
'''
l=[22,34,"Shreya",7,0.8,[22,"Swain",99]]
print(l[2]) #will print Shreya
print(l[5][1]) #will print Swain
'''

#--------------------------------------------------------------------------------------

#Slicing
'''
l = [10, 20, 30, 40, 50, 60, 70]

print(l[1:4])    # will print-- [20, 30, 40] - elements from index 1 to 3
print(l[:3])     # will print-- [10, 20, 30] - from beginning to index 2
print(l[4:])     # will print-- [50, 60, 70] - from index 4 to end
print(l[-3:])    # will print-- [50, 60, 70] - last 3 elements
print(l[::2])    # will print-- [10, 30, 50, 70] - every 2nd element
'''

#-----------------------------------------------------------------------------------------

#Methods
'''
l = [3, 1, 4, 1, 5, 9]

l.append(2)       # adds 2 at the end
l.insert(2, 8)    # will insert 8 at index 2
l.remove(1)       # it will remove the first occurrence of 1
l.pop()           # removes the last element
l.sort()          # sorts the list in ascending order
l.reverse()       # reverses the list

'''

#---------------------------------------------------------------------------------

#Comprehensions
'''
squares = [x**2 for x in range(5)]         
evens = [x for x in range(10) if x % 2 == 0] 
nested = [[x, x+1] for x in range(3)]      

print(squares) #this will print [0, 1, 4, 9, 16]
print(evens) #output will be [0, 2, 4, 6, 8]
print(nested) #output--[[0, 1], [1, 2], [2, 3]]
'''

