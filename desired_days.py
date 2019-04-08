#!/usr/bin/python
import datetime,sys,getopts

def getDesiredDay(start_date,end_date,desired_day):
  v1 = value_of_start_day = weekdays[start_date.strftime("%a")]
  v2 = value_of_desired_day = weekdays[desired_day]
  #print(v1)
  #print(v2)
  if v1 == v2:
   return start_date
  else:
    start_date = start_date + datetime.timedelta(days=(abs(v2-v1)))
    return start_date

weekdays = { "Mon" : 1, "Tue" : 2, "Wed" : 3, "Thu" : 4, "Fri" : 5, "Sat" : 6, "Sun" : 7 }
start_date = datetime.datetime(2019, 04,  8, 00, 00)
end_date   = datetime.datetime(2019, 04, 30, 00, 00)
desired_day = sys.argv[1]

#print(start_date.strftime("%Y-%m-%d"))
#print(start_date.strftime("%a"))

start_date = getDesiredDay(start_date,end_date,desired_day)
print("Next {0} is {1}".format(desired_day,start_date.strftime("%Y-%m-%d")))

while start_date <= end_date:
  print(start_date.strftime("%Y-%m-%d"))
  start_date= start_date + datetime.timedelta(days=7)

sys.exit(0)



  
