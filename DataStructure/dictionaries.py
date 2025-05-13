#creating a dictionary
#1---empty dictionary and then adding elements
'''
d={}
d["id"]=1
d["company"]="Atyeti"
d["location"]="Pune"
print(d)
'''

#2---givng keys and values directly
'''
d={
    "Company":"Atyeti",
    "Location":"Pune"
    
}
print(d["Company"]) # will print value of the key
print(d.get("Location")) #this will return the value of the key mentioned
'''
#--------------------------------------------------------------------------------------

# Modification in dictionary
'''
d={
    "name":"Shreya",
    "id":1149,
    "location":"Pune"
}
d["id"]=1144

print(d)
'''
#--------------------------------------------------------------

#Deleting and accessing in dictionary
'''
d={
    "id": [1111,2222],
    "department":["Delivery","Corporate"],
    "company":"Atyeti"
}
del d["id"] #output---{'department': ['Delivery', 'Corporate'], 'company': 'Atyeti'}
print(d)
print(d["department"]) #output ---['Delivery', 'Corporate']
print(d.keys())
print(d.values())
print(d.items())
'''
#---------------------------------------------------------------------------------

#Looping through the items in dictionary
'''

d={
    "a":10,
    "b":20,
    "c":30,
    "d":40
}
for i in d:
    print(i,d[i]) #this will give you the key and vlues of the dictionary
'''
#------------------------------------------------------------------------

#Topics remaining
#sorting in dictionary
#zip dictionary

