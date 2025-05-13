from datetime import datetime, timedelta

#to print current dat and time
'''
now = datetime.now() #this will give the current date and time
print(now)
'''

#----------------------------------------------------------

#date arithmetic
'''
now=datetime.now()
tomorrow = now + timedelta(days=1)
print("Tomorrow: ", tomorrow)
'''

#--------------------------------------------------------------

#creating some date--
'''
some_date = datetime(2025,1,5)
print("created date is: ",some_date)
'''

#----------------------------------------------------------------

#date difference

'''
some_date = datetime(2025,1,5)
now = datetime.now()
difference = now - some_date
print(difference)
'''

