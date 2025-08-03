"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

# with open('texts.csv', 'r') as f:
#     reader = csv.reader(f)
#     texts = list(reader)

# with open('calls.csv', 'r') as f:
#     reader = csv.reader(f)
#     #calls = list(reader)
#     unique_numbers=set()
#     calls = [
#     ['(080)1234567', '(080)7654321', '01-09-2016 06:01:12', '60'],       # fixed → fixed (Bangalore)
#     ['(080)2345678', '(022)1234567', '01-09-2016 06:03:51', '120'],      # fixed → fixed (Mumbai)
#     ['(080)3456789', '93412 66159', '01-09-2016 06:05:35', '240'],       # fixed → mobile
#     ['(080)4567890', '98453 94494', '01-09-2016 06:07:10', '300'],       # fixed → mobile
#     ['(080)5678901', '1402316533', '01-09-2016 06:09:12', '90'],         # fixed → telemarketer
#     ['(022)6789012', '(080)6789012', '01-09-2016 06:11:00', '180'],      # not from Bangalore (skip)
#     ['93412 34567', '98453 12345', '01-09-2016 06:13:22', '60'],         # mobile → mobile (skip)
# ]
#     iterator=iter(calls)
#     first=next(iterator)
#     #d=first[0][0:3]
#     #d=d.split(')')[0].split('(')[1]
#     #str_to_int = lambda x: int(x)
#     for call in calls:
#       caller = call[0]
#       receiver = call[1]

#       if caller.startswith("(080)"):
#           if receiver.startswith("("):
#               code = receiver.split(')')[0][1:]  # gets area code without '(' and ')'
#               unique_numbers.add(code)
#           elif receiver[0] in ['7', '8', '9']:
#               unique_numbers.add(receiver[:4])
#           elif receiver.startswith("140"):
#               unique_numbers.add("140")

# # Print in sorted order
# print("The numbers called by people in Bangalore have codes:")
# for code in sorted(unique_numbers):
#     print(code)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    #calls = list(reader)
    calls = [
    ['(080)1234567', '(080)7654321', '01-09-2016 06:01:12', '60'],       # fixed → fixed (Bangalore)
    ['(080)2345678', '(022)1234567', '01-09-2016 06:03:51', '120'],      # fixed → fixed (Mumbai)
    ['(080)3456789', '93412 66159', '01-09-2016 06:05:35', '240'],       # fixed → mobile
    ['(080)4567890', '98453 94494', '01-09-2016 06:07:10', '300'],       # fixed → mobile
    ['(080)5678901', '1402316533', '01-09-2016 06:09:12', '90'],         # fixed → telemarketer
    ['(022)6789012', '(080)6789012', '01-09-2016 06:11:00', '180'],      # not from Bangalore (skip)
    ['93412 34567', '98453 12345', '01-09-2016 06:13:22', '60'],         # mobile → mobile (skip)
]


total_caller=0
total_reciver=0
for row in calls:
  caller=row[0]
  reciever=row[1]
  if caller.startswith('(080)'):
    total_caller+=1
    if reciever.startswith('(080)'):
      total_reciver+=1
print((total_reciver/total_caller)*100)
    
"""

TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
