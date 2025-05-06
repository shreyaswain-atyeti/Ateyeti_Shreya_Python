#1--len()
print(len([1,2,3])) # output=3

#2--sum()
print(sum([10,10])) # 20

#3-min()
print(min([44,3,2])) #2

#4---max()
print(max([1,2,344])) #344

#5--sorted() 
print(sorted([3,44,1])) #output--[1, 3, 44]

#6--reversed()
print(list(reversed([1, 2, 3]))) # output--[3, 2, 1]

#7--enumerate()
print(list(enumerate(["a","b"]))) #output--it gives index no along with the elements[(0, 'a'), (1, 'b')]

#8--zip()
print(list(zip([1,2],["a","b"]))) #output--[(1, 'a'), (2, 'b')]--basically pairs

#9-type()
type(3) #--int
type(5.5) #--float

#10--isinstance

print(isinstance("shreya",str)) # returns true if data type is matched and if not returns false

#11--conversions
print(int(10.5)) #--wil give the output 10
print(float(3)) # 3.0
print(str(123)) #int to str
print(list("abc")) #str to list--output--['a', 'b', 'c']
#similarly
tuple([1,2]) # will give (1,2)
set([1,1,1,2]) # will give {1,2}
print(dict([("a",1),("b",2)])) #will give {'a': 1, 'b': 2}

#12
print(abs(-7)) #will give 7--abslute value
#13
print(round(3.12456,3)) # will round off till 3 nos
#14
pow(2,3) # 2 to the power 3-->8 ans

#15
map(str,[1,2,3]) #converts to strings

#16
'''
find() and findall()---used to get elements ususally used in regex
'''

