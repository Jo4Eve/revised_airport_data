#!/usr/bin/env python
# coding: utf-8

# In[43]:


import csv
from csv import DictReader
import json
import pandas as pd
import re

#use pandas to read the data
airport = pd.read_csv('airports.csv')

# creating a new csv file excluding data with word 'closed'
newFile = airport[(airport['type'] != 'closed')]
newFile.to_csv('newAirportData.csv')
newAirportfile = pd.read_csv('newAirportData.csv', usecols = ('iso_country','type','ident','id' ))
newAirportfile

# filtering the new file out for GB airports
GBfile = newAirportfile[(newAirportfile['iso_country'] == 'GB')]

# this pivots data in columns 'type' into rows
pivoted = GBfile.pivot(index = ('ident','iso_country'), columns = 'type', values = 'id')

#specifying which columns to be headers
file1 = pivoted.to_csv('pivotedData.csv')
file2 = pd.read_csv('pivotedData.csv', usecols = ('ident','iso_country','small_airport','medium_airport','large_airport'))
file2

#open the frequency file and merge columns with same data together
freq = pd.read_csv('airport-frequencies.csv', usecols = ['airport_ident' ,'id', 'frequency_mhz'])
# freq
# freq2 = freq.pivot(index = 'id', columns = 'frequency_mhz', values = 'airport_ident')
# freq2

#this merges airport data using the 'ident' column which matches frequecy file 'airport_ident'
airportPlusfreq = pd.merge(file2, freq, left_on = 'ident',right_on =  'airport_ident')

airportPlusfreq
#adding the runways file data  
runways = pd.read_csv('runways.csv')

#the three data files
threeFilesMerged = pd.merge(airportPlusfreq, runways, left_on = "airport_ident", right_on = "airport_ident")
threeFilesMerged2 = threeFilesMerged.to_csv('threeFiles.csv')

finalFile = pd.read_csv('threeFiles.csv', usecols  = ('ident','iso_country','large_airport','medium_airport',
                                                      'small_airport','frequency_mhz' ))

finalFile2 = finalFile.to_csv('finalFile.csv')
file   = pd.read_csv('finalFile.csv')
       
file                       


# ### converting the final file to JSON format                               

# In[82]:


jsonFile = file.to_json (orient= 'index',indent = 2) 

print (jsonFile)
        
        


# In[ ]:





# In[ ]:




