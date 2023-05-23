import serial as s
import time as t
import requests

# insert your real key here!
access_key = '162ebda4-2467-4478-9e15-73174d62fbbb'

headers = {
    'X-Meteum-API-Key': access_key
}

response = requests.get('https://api.meteum.ai/v1/forecast?lat=12.972623092425923&lon=79.16267637937521', headers=headers)

print(response.json()), 

data = response.json()


# In[2]:


# Write Python3 code here

import json


# Indent keyword while dumping the
# data decides to what level
# spaces the user wants.
#print(json.dumps(data, indent = 1))

# Difference in the spaces
# near the brackets can be seen
print(json.dumps(data, indent = 3))


# In[3]:


from datetime import date

today = date.today()
print("Today's date:", today)


# In[4]:


print(data['forecasts'])


# In[5]:


print(json.dumps(data['forecasts'][1], indent = 3))


# In[6]:


data_to_work = data['forecasts'][1]["hours"]
print(data_to_work)


# In[7]:


dici = {}
for a in data_to_work :
    dici[a["hour"]] = [a["soil_temp"] , a["soil_moisture"] , a["prec_mm"] , a["prec_prob"] , a["prec_period"]]
    print(dici[a["hour"]])


# In[8]:


import pandas as pd
new1 = pd.DataFrame.from_dict(dici)
new1 = new1.transpose()
print(new1)


# In[9]:


print(new1.head())
new1.columns =["soil_temp" , "soil_moisture" , "prec_mm" , "prec_prob" , "prec_period"]
  
# Change the row indexes
#df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4']


# In[10]:


new1


# In[11]:


a = sum(new1["prec_mm"]/10)
a


# In[12]:


import json
  
# Opening JSON file
f = open("E:\TARP\crop_data.json")
  
data = json.load(f)
  
for i in data['Rice']:
    print(i)
  
# Closing file
f.close()


# In[13]:


f = open("E:\TARP\crop_data.json")
data = json.load(f)
threshold = 35 
import pandas as pd


# In[14]:


crop = "Rice"
my_lis = [data[crop][0]['Stage'] , data[crop][0]['Days']]   
new = pd.DataFrame(my_lis)
new  = new.transpose()
new.columns = ['Water_Percentage', 'Total_Days']
new['Crop_Period'] = new.index + 1
new["Total_Water/M^2"] = (data[crop][0]['Total_Water'] * new["Water_Percentage"])/4046.86
new["Daily_Water/M^2"] = (new["Total_Water/M^2"])/30
new["Soil_Moisture"] = (new["Daily_Water/M^2"])/threshold
first_column = new.pop('Crop_Period')
new.insert(0, 'Crop_Period', first_column)
new.head()


# In[15]:


crop = "Sugar Cane"
my_lis = [data[crop][0]['Stage'] , data[crop][0]['Days']]   
new = pd.DataFrame(my_lis)
new  = new.transpose()
new.columns = ['Water_Percentage', 'Total_Days']
new['Crop_Period'] = new.index + 1
new["Total_Water/M^2"] = (data[crop][0]['Total_Water'] * new["Water_Percentage"])/4046.86
new["Daily_Water/M^2"] = (new["Total_Water/M^2"])/30
new["Soil_Moisture"] = (new["Daily_Water/M^2"])/threshold
first_column = new.pop('Crop_Period')
new.insert(0, 'Crop_Period', first_column)
new.head()


# In[16]:


crop = "Wheat"
my_lis = [data[crop][0]['Stage'] , data[crop][0]['Days']]   
new = pd.DataFrame(my_lis)
new  = new.transpose()
new.columns = ['Water_Percentage', 'Total_Days']
new['Crop_Period'] = new.index + 1
new["Total_Water/M^2"] = (data[crop][0]['Total_Water'] * new["Water_Percentage"])/4046.86
new["Daily_Water/M^2"] = (new["Total_Water/M^2"])/30
new["Soil_Moisture"] = (new["Daily_Water/M^2"])/threshold
first_column = new.pop('Crop_Period')
new.insert(0, 'Crop_Period', first_column)
new.head()


# In[17]:


crop = "Potato"
my_lis = [data[crop][0]['Stage'] , data[crop][0]['Days']]   
new = pd.DataFrame(my_lis)
new  = new.transpose()
new.columns = ['Water_Percentage', 'Total_Days']
new['Crop_Period'] = new.index + 1
new["Total_Water/M^2"] = (data[crop][0]['Total_Water'] * new["Water_Percentage"])/4046.86
new["Daily_Water/M^2"] = (new["Total_Water/M^2"])/30
new["Soil_Moisture"] = (new["Daily_Water/M^2"])/threshold
first_column = new.pop('Crop_Period')
new.insert(0, 'Crop_Period', first_column)
new.head()


# In[18]:


crop = "Corn"
my_lis = [data[crop][0]['Stage'] , data[crop][0]['Days']]   
new = pd.DataFrame(my_lis)
new  = new.transpose()
new.columns = ['Water_Percentage', 'Total_Days']
new['Crop_Period'] = new.index + 1
new["Total_Water/M^2"] = (data[crop][0]['Total_Water'] * new["Water_Percentage"])/4046.86
new["Daily_Water/M^2"] = (new["Total_Water/M^2"])/30
new["Soil_Moisture"] = (new["Daily_Water/M^2"])/threshold
first_column = new.pop('Crop_Period')
new.insert(0, 'Crop_Period', first_column)
new.head()


# In[19]:


new3 = pd.DataFrame(new["Soil_Moisture"])


# In[20]:


new3["Prec_mm"] = sum(new1["prec_mm"]/10)


# In[21]:


new3["Soil_Moisture_Tomorrow"] = sum(new1["soil_moisture"]/24)


# In[22]:


new3["Soil_Moisture_Total"] = new3["Soil_Moisture_Tomorrow"] + new3["Prec_mm"] 


# In[23]:


new3


# In[24]:


import datetime

x = datetime.date(2023, 4, 2)

print(x)


# In[25]:


a = today-x
cal_day = a.days


# In[26]:


cal_day


# In[27]:


for a in new3:
    print(a)


# In[28]:


i = 1
temp = 1
for a in new["Crop_Period"]:
    temp += new["Total_Days"][i] 
    if(temp>cal_day):
        break ;
    i+=1


# In[29]:


print("Crop Stage : " , i) 
print("Day : " , cal_day)
Prec_mm = sum(new1["prec_mm"]/10)
Soil_Moisture_Tomorrow = sum(new1["soil_moisture"]/24)
Soil_Moisture_Total = Soil_Moisture_Tomorrow + Prec_mm
print("Soil Moisture Tomorrow : " , Soil_Moisture_Tomorrow)
print("Precipitaion Tomorrow : " , Prec_mm)
print("Total Soil Moisture : " , Soil_Moisture_Total)
print("Ideal Soil Moisture : " , new["Soil_Moisture"][i-1])


# In[30]:


if(new["Soil_Moisture"][i-1]>Soil_Moisture_Total):
    print(0)
else :
    print(1)


# In[5]:



ser = s.Serial('COM5', 9600, timeout=0)   # check your com port
t.sleep(2)
print(ser.name,"connected")
import serial as s
import time as t
ser = s.Serial('COM5', 9600, timeout=0)   # check your com port
t.sleep(2)
print(ser.name,"connected")
   
if(new["Soil_Moisture"][i-1]>Soil_Moisture_Total):
    ser.write(b'0')    
    print ("MOTOR OFF")
elif(new["Soil_Moisture"][i-1]<=Soil_Moisture_Total):
    ser.write(b'1')
    print ("MOTOR ON")
else: 
    ser.close()

while True:
    if ser.in_waiting > 0:
        moisture_data = ser.readline().decode().strip()
        print(f"Moisture Percentage = {moisture_data}%")
        print(type(moisture_data))
        # Check if humidity has reached 60%
        if float(moisture_data.strip()) >= new["Soil_Moisture"][i-1]:
            print("Ideal Moisture reached, turning off motor")
            ser.write(b'0')
            break
        t.sleep(1)



