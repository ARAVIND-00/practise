"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""


import csv

telephone_number=set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for i in range (len(texts)):
        telephone_number.add(texts[i][0])
        telephone_number.add(texts[i][1])


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for i in range (0,len(calls)):
        telephone_number.add(calls[i][0])
        telephone_number.add(calls[i][1])
print(f"There are {len(telephone_number)} different telephone numbers in the records.")
        


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
