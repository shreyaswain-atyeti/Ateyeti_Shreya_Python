#1
'''
def company():
    print("Atyeti")

company()
'''

#--------------------------------------------------------------------

#2
'''
def company_details(company_name,location):
    return f"Working in {company_name}, {location}"

response = company_details("Atyeti","Pune")
print(response)
'''

#--------------------------------------------------------------------------

#3---multiple returns
'''
def company_details():
    return "Atyeti", "Pune", 500

company_name, location, employees_strength= company_details()
print(company_name, location, employees_strength)
'''

