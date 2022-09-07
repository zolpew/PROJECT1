
import tradingeconomics as te



te.login('guest:guest')

#without a client key only a small sample of data will be given.






#To get calendar data by country, category and date
mydata = te.getCalendarData(country = 'United States', initDate = '2019-01-01', endDate = '2022-01-01', output_type= 'df')
print(mydata)

inventory = []


for i in range(0, len(mydata)):

   event = mydata['Event'][i]
   amp = mydata['Importance'][i]
   try:
       forecast = float(mydata['Forecast'][i].strip('%').strip('K'))
       print(forecast)
        
   except ValueError:
       
       forecast = 0
   
    
   try:
       actual = float(mydata["Actual"][i].strip('%').strip('K'))
       
   except ValueError:
       actual = 0
       
   try:
        previous = float(mydata['Previous'][i].strip('%').strip('K'))
    
   except ValueError:
        previous = 0
          
   if forecast == 0 :
       print("forecast = 0")
   
   elif actual == 0 :
       print("actual = 0")
   
   elif previous == 0:
       print("previous = 0")
    
   else:
       percentage_change = ((abs(actual-forecast) + abs(previous-forecast)) / abs(forecast)) * 1
       inventory.append((event, amp, actual, previous, forecast, percentage_change))



       
        
        
    
    
   