from datetime import datetime, timedelta 
 
date = datetime(2024, 12, 31) + timedelta(weeks=1) 
date2 = datetime(2012, 5, 14) 
 
delta = date - date2 
 
print(delta) 
print("Days", delta.days) 
print("Seconds", delta.seconds)
print("microseconds" ,delta.microseconds)
print("total_seconds()", delta.total_seconds())
 
  
# Con Timedelta se puede agregar o restar fechas a un objeto datetime.