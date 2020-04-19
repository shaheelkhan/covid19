# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:53:52 2020

@author: Shaheel
"""


#Import required libraries
import os
import glob
import pandas as pd
from datetime import datetime


#URLs to be used
confirmed_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
death_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovered_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

#Creating a DataFrame 
confirmed_data = pd.read_csv(confirmed_url)
death_data = pd.read_csv(death_url)
recovered_data = pd.read_csv(recovered_url)

#Function to upivot and concatenate the three dataframe into one
def combined_csv(data1,data2,data3):
        data = [data1,data2,data3]
        x =[]
        
        for item in data:
                df = pd.melt(item,id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Updated_date',value_name='cases')
                x.append(df)
        confirmed_clean = x[0].rename(columns={'cases':'No:Confirmed'})
        death_clean = x[1].rename(columns={'cases':'No:Death'})
        recovered_clean = x[2].rename(columns={'cases':'No:Recovered'})
        
        combined = pd.concat([confirmed_clean,death_clean['No:Death'],recovered_clean['No:Recovered']],axis=1)
        
        return combined


combined_data = combined_csv(confirmed_data,death_data,recovered_data)

#Change the datatype of date column to datetime
combined_data['Updated_date'] = pd.to_datetime(combined_data['Updated_date'])

#Export the combine data as a csv file

path = os.getcwd()
path = path + '\\'
os.chdir(path)
all_filenames = [file for file in glob.glob('*.{}'.format('csv'))]

if 'combined_data.csv' in all_filenames:
                os.remove(path+'combined_data.csv')
combined_data.to_csv('combined_data.csv',index=False,encoding='utf-8-sig')

        

