"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from collections import defaultdict
import csv
def find_max_dict(scores):
    max_value=0
    d={}      
    for key ,values in scores.items():
    
        if values > max_value:
            max_value=values
            d.clear()
            d[key]=values
          
    return d
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

#def test (calls=[[]]):
d=defaultdict(int)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    #calls = calls
    for i in calls:
        
        date_time_str = i[2].split()[0]
        print('lll',date_time_str)
        
        day, month, year = date_time_str.split('-')
        print(day, month, year)
        if month =='09' or '9':
        
            print(day, month, year)
            d[i[0]]+=int(i[3])
            d[i[1]]+=int(i[3])
    e=find_max_dict(d)
        
    print(e)
                
                
                    
                    
                
                
            
    
#assert test([['78130 00821','98453 94494','1-9-2016  6:01:12 AM','186'],['78298 91466','(022)28952819','1-9-2016  6:01:59 AM','2093']])== {'78298 91466':2093,'(022)28952819':2093,'78130 00821':186,'98453 94494':186}
print('completed')
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

