
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

import scipy.constants #untuk konstanta
import tradingeconomics as te


te.login('guest:guest')




#login ke terminal metatrader 5
if not mt5.initialize(login=62239272, server="MetaQuotes-Demo",password="mlqzja8n"):
    print("initialize() failed")
    mt5.shutdown()
    

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())



# mndapatkan ticks emas dolar, terdapat bid dan ask
xauusd_ticks = mt5.copy_ticks_range("XAUUSD", datetime(2020,1,27,13), datetime(2020,1,28,13), mt5.COPY_TICKS_ALL)
 
#rates
xauusd_rates = mt5.copy_rates_range("XAUUSD", mt5.TIMEFRAME_M1, datetime(2020,1,27,13), datetime(2020,1,28,13))

#memutuskan hubungan
mt5.shutdown()



print('xauusd_ticks(', len(xauusd_ticks), ')')
for val in xauusd_ticks[:10]: print(val)

print('xauusd_rates(', len(xauusd_rates), ')')
for val in xauusd_rates[:10]: print(val)




ticks_frame = pd.DataFrame(xauusd_ticks)
# convert time in seconds into the datetime format
ticks_frame['time']=pd.to_datetime(ticks_frame['time'], unit='s')
#display ticks on the chart
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
 
# display the legends
plt.legend(loc='upper left')
 
# add the header
plt.title('XAUUSD ticks')
 
# display the chart
plt.show()





class EDGBOT:
    
    
    
    #insiasi
    def __init__(self, bid, ask, current, forecast, previous, event):
        
        self.bid = bid
        self.ask = ask
        self.point = 10
        self.gold_constanta = -1
        self.psi = scipy.constants.golden
        #self.memory = deque(maxlen = 1000)
        self.current = curent
        self.forecast = forecast
        self.previous = previous
        self.event = event
        self.inventory = []
        
    def get_event(self):
        inventory = self.inventory
        mydata = te.getCalendarData(country = 'United States', initDate = '2014-01-01', endDate = '2022-01-01', output_type= 'df')
        print(mydata)
        for i in range(0, len(mydata)):
           event = mydata['Event'][i]
           amp = mydata['Importance'][i]

           actual = mydata["Actual"][i]
           previous = mydata['Previous'][i]
           Forecast = mydata['Forecast'][i]
            
           
           inventory.append((event, amp, actual, previous, Forecast))
          
        return(inventory)

        
        
        
        
        
    # untuk rumus utama( perkalian SUM dengan konstanta lainnya)
    def counter_result(self, ISE):
        Total_ISE = self.intreval_sum_event()
        
        result = Total_ISE * self.point * self.gold_constanta
        
        return result
        
    #rumus mencari (Interval sum of event) dengan rumus sli(sigma dari perkalian
    #traits amplifikasi dan perubahan persen)
    def intreval_sum_event(self):
        
        
        #looping pada setiap event yang ada
        for i in range(0, len(event)-1):
            event_type, traits, amp, current, foecast, previous = event[i]
            orientation = self.get_orientation(current, forecast)
            percentage_change = self.get_percentage_change(orientation)
            
  
            ISE = traits * amp * percentage_change
            Total_ISE += ISE
            
        return Total_ISE
            
    #menghitung perubahan persen dengan menggunakan data forecast, previous, dan curent)
    def get_percentage_change(self, orientation):
        c = self.current
        f = self.forecast
        p = self.previous
        
        
        percentage_change = ((abs(c-f) + abs(p-f)) / abs(f)) * orientation
        
        return percentage_change
    
    #menghitung orientasi
    def get_orientation(self, curent, forecast):
        c = current
        f = forecast       
        if c == f:
            orientation = 0
        elif c > f:
            orientation = 1
        elif c < f:
            orientation = -1
            
        return orientation 
    
    
    
    
    
    
    
        
    def buy:
        
    def sell:
        
    def hold:
        
        
    def act:
    
        
    
        
        
        
        













    


