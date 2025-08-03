"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
callers=set()
reciver=set()
text_receiver=set()
text_sender=set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
for text in texts:
    text_sender.add(text[0])
    text_receiver.add(text[1])



with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
for call in calls:
    callers.add(call[0])
    reciver.add(call[1])
telemarketer=callers.copy()

all=text_sender.union(text_receiver)
all=all.union(reciver)

for caller in callers:
    if caller in all:
        telemarketer.remove(caller)
    else:
        pass
print("These numbers could be telemarketers:")
for number in sorted(telemarketer):
    print(number)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

