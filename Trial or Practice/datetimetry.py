"""import datetime
#dates = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
current_day = datetime.datetime.now().weekday
print(current_day)"""

"""import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
 
# Driver program
date = (str(datetime.datetime.now().day) + " " + str(datetime.datetime.now().month) + " " + str(datetime.datetime.now().year))
print(findDay(date))
current_date = datetime.datetime.now().day

current_month = datetime.datetime.now().month

current_year = datetime.datetime.now().year

weekday_number = datetime.date(current_year,current_month,current_date).weekday()

week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']"""
import datetime
current_hour = datetime.datetime.now().hour
print(current_hour)