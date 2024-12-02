import pandas as pd

def fahrenheit_to_celsius(value:float):
    value-=32
    return round(value/1.8,1)

def mph_to_kmh(value:float):
    return round(value*1.609344,1)

data = pd.read_csv('./data.csv')
data.info(show_counts=True)
pd.set_option("display.max_columns", None)
'''print(pd.unique(data['City']))
print(pd.unique(data['Season'])) #Obrisati ovaj parametar jer je uvek Fall
print(pd.unique(data['preciptype']))
print(pd.unique(data['description']))
#print(pd.unique(data['stations']))#Verovatno nepotreban parametar
#print(pd.unique(data['source']))#Verovatno nepotreban parametar
#print(pd.unique(data['Month']))#Obrisati ovaj parametar jer je uvek 9
print(pd.unique(data['windspeed']))'''
print(data.head())

data['temp']=data['temp'].apply(fahrenheit_to_celsius)
data['tempmax']=data['tempmax'].apply(fahrenheit_to_celsius)
data['tempmin']=data['tempmin'].apply(fahrenheit_to_celsius)
data['feelslikemax']=data['feelslikemax'].apply(fahrenheit_to_celsius)
data['feelslikemin']=data['feelslikemin'].apply(fahrenheit_to_celsius)
data['feelslike']=data['feelslike'].apply(fahrenheit_to_celsius)
data['dew']=data['dew'].apply(fahrenheit_to_celsius)
data['Temp_Range']=data['Temp_Range'].apply(fahrenheit_to_celsius)
data['windspeed']=data['windspeed'].apply(mph_to_kmh)
print(data.head())