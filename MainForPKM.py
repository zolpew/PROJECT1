import ECONOTOMUS as eco
import matplotlib.pyplot as plt
import datetime as dt
result_list_rev = []
initdate = dt.datetime(2021, 12, 14, 0, 0)
endDate = dt.datetime(2022, 4, 23, 0, 0)
file_name = 'DATASET_2_CSV_REV2.csv'
EventCounter = eco.ECONOTOMUS(file_name=file_name, initDate = initdate, endDate = endDate)
results, inventory, inv_result = EventCounter.RUN_TO_COUNT()
lr = len(results)
plt.plot(range(len(results)), results, 'r-')
plt.legend(loc='upper left')
 # add the header
plt.title('result')
# display the chart
plt.show()





