import array
arr=array.array('i',(1,2,3,4))
print(arr)

import math
print(math.sqrt(16))
print(math.pi)

import random
print(random.randint(1,100))
print(random.choice(['apple','banana','cherry']))

##file and directory access
import os

print(os.getcwd())
#os.mkdir('test_dir')  # creates a foloder in your working trees

# high level operations on files and collection of files

#import shutil
#shutil.copyfile('source.txt','destination.txt')  

# data serialization
import json
data={'name':'nikitha','age':12}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

passed_data = json.loads(json_str)
print(passed_data)
print(type(passed_data))

#csv 
import csv 
with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['nikihta','12'])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#date and time
from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)

##time
import time
print(time.time())
time.sleep(2)
print(time.time())

#regular expressions
import re      
pattern=r'\d+'      #used to find specific data types in the given content.Here \d+ gives the digits present in the text
text='There are 123 apples'
match=re.search(pattern,text)
print(match.group())


