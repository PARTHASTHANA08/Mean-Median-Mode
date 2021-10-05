import csv

with open('data.csv') as f:
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
newData = []    
for i in range(len(file_data)):
    num = file_data[i][2]    
    newData.append(float(num))
n = len(newData)    
total = 0
for x in newData:
    total += x
mean = total/n 
print("The Mean of the Weight is ", mean)   