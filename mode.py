import csv 
from collections import Counter

with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []
for i in range(len(file_data)):
    num = file_data[i][2]
    newData.append(num)
data = Counter(newData) 
modeRange = {
    "80-90":0,
    "90-100":0,
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140:150":0,
    "150-160":0,
    "160-170":0
}    
for weight,occurance in data.items():
    if 80 < float(weight) < 90 :
        modeRange["50-60"] += occurance
    elif 90 < float(weight) < 100:
        modeRange["60-70"] += occurance 
    elif 100 < float(weight) < 110:
        modeRange["70-80"] += occurance
    elif 110 < float(weight) < 120 :
        modeRange["50-60"] += occurance
    elif 120 < float(weight) < 130:
        modeRange["60-70"] += occurance 
    elif 130 < float(weight) < 140:
        modeRange["70-80"] += occurance
    elif 140 < float(weight) < 150 :
        modeRange["50-60"] += occurance
    elif 150 < float(weight) < 160:
        modeRange["60-70"] += occurance 
    elif 160 < float(weight) < 170:
        modeRange["70-80"] += occurance    
mode_r,modeOccurance = 0,0
for range , occurance in modeRange.items(): 
    if occurance > modeOccurance:
           mode_r , mode_occurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance 
mode  = float((mode_r[0] + mode_r[1])/2) 
print("The mode of the Weight is", mode)