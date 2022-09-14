import scipy.constants
import pandas as pd
import datetime as dt
from datetime import timedelta

#untuk kalkulasi menggunakan CSV 

class ECONOTOMUS:
    
    #inisiasi variabel
    def __init__(self, initDate, endDate, file_name):
        self.point = 10
        self.gold_constanta = -1
        self.psi = scipy.constants.golden
        self.inventory = []
        self.Total_ISE = 0
        self.file_name = file_name
        self.initDate = initDate
        self.endDate = endDate
        self.Results = []
        self.dates = []
    #membaca file csv
    def load_csv(self):
        file_name = self.file_name
        df = pd.read_csv(file_name)
        print("membuka file"+ str(file_name))
        print("jumlah event:" +str( len(df)))
        return df
    
   
    # merapihkan struktur, merubah pandas dataframe ke aray
    def APPEND_TO_INVENTORY(self, df):
        inventory = self.inventory
        
        for i in range(len(df)):
            date = df['Date'][i]
            date = date.split('/')
            year = int(date[2])
            month = int(date[1])
            day = int(date[0])
            event = df['Event'][i]
            clock= df['clock'][i]
            clock = clock.split(':')
            hour = int(clock[0])
            minute = int(clock[1])
            
            date = dt.datetime(year, month, day, hour, minute)
            print("test"+ str(date))
        
            try:
                current = float(df['Curr'][i].strip('%').strip('K'))
            except ValueError:
                current = 0
                
            try:
                forecast = float(df['Fore'][i].strip('%').strip('K'))
            except ValueError:
                forecast = 0
                
            try:
                previous = float(df['Prev'][i].strip('%').strip('K'))
            except ValueError:
                previous = 0
                
            try:
                amp = float(int(df['amp'][i]))
            except ValueError:
                amp = 0
                
            try:
                traits = float(int(df['Traits'][i]))
            except ValueError:
                traits = 0
                
                
            if forecast == 0 :
                print("forecast = 0")
            elif current == 0 :
                print("actual = 0")
            elif previous == 0:
                print("previous = 0")
            elif amp == 0:
                print("amplification = 0")
            elif traits == 0:
                print("traits = 0")
            
                
            else:
                 percentage_change = self.get_percentage_change(current, forecast, previous)
                 inventory.append((date, event, traits, current, forecast, previous,amp, percentage_change ))
                 
        print("Data berhasil diappend ke inventory")
        print("penambahan kolom baru yaitu percentage_change")


    def get_result(self, Total_ISE):
        result = Total_ISE * self.point * self.gold_constanta * self.psi
        return result
    
    def daterange(self, start_date, end_date):
        for n in range(int ((end_date - start_date).hour)):
            yield start_date + timedelta(n)
            
    def hourly_it(self, start, finish):
        while finish> start:
            start = start + timedelta(minutes = 15)
            yield start

    
    
    def get_Total_ISE(self,date_to_sum,):
        
        inventory = self.inventory
        Total_ISE = self.Total_ISE
        inv_date = self.dates
        for i in range(len(inventory)):
            date,  event, traits, current, forecast, previous,amp, percentage_change = inventory[i]
            if date == date_to_sum:
                
                
                print(date)
                ISE = traits * amp * percentage_change
                Total_ISE += ISE
                
                
                print(str('percentage change =' + str(percentage_change)))
                print("ini total_ISE" + str(Total_ISE))
                print("INI  ISE" + str(ISE))
                
                
               
          
                inv_date.append(date)
                    
            
        
        return Total_ISE, inv_date

        
        
    
            
        
        
    def get_percentage_change(self, current, forecast, previous):
        orientation = self.get_orientation(current, forecast)
        
        
        
        
        
        if orientation == 0:
            percentage_change = 0 
            
        else:
            percentage_change = ((abs(current-forecast) + abs(previous-forecast)) / abs(forecast)) * orientation
            
            
        
        
        
        return percentage_change
    
    
    
    def get_orientation(self, current, forecast):
        c = current
        f = forecast       
        if c == f:
            orientation = 0
        elif c > f:
            orientation = 1
        elif c < f:
            orientation = -1            
        return orientation
    

        
        
        
    def RUN_TO_COUNT(self):
        
        df = self.load_csv()
        self.APPEND_TO_INVENTORY(df)
        results = self.Results
        
        
           
        for hour in self.hourly_it(self.initDate, self.endDate):
            Total_ISE, inv_date = self.get_Total_ISE(date_to_sum = hour )
            result = self.get_result(Total_ISE)
            
            if result != 0:
                result = result 
                results.append(result)
                
            
                
        return results, self.inventory, inv_date
    
    
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        