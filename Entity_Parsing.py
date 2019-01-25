#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:04:35 2018
@author: mliang
"""

import datetime
import pandas as pd
import dateutil.parser # Date parser library 1      (English only)
import dateparser      # Date parser library 2     (multi-languages)
import datefinder      # Date parser library 3     (extracts dates from text)
from postal.parser import parse_address    # Address parser library   (multi-languages)


#%% functions    
def parse_incomplete_date(dt_str):  
    # This function detects incomplete dates and replace default day/month/year with '0'
    global ranking_Y, ranking_m, ranking_d, df, i

    DEFAULT_DATE2 = datetime.datetime(2, 2, 2)   #set a different set of default values for incomplete dates
    dt2 = dateutil.parser.parse(dt_str, default=DEFAULT_DATE2).date()  # parsing
    outY = dt.strftime('%Y')
    outm = dt.strftime('%m')
    outd = dt.strftime('%d')
    
    # see if parsed day/month/year changes with default values
    # if yes, day/month/year is not provided in the input string, replace default value with '0'
    if dt.strftime('%Y') == DEFAULT_DATE.strftime('%Y') and\
     dt2.strftime('%Y') == DEFAULT_DATE2.strftime('%Y'):
       outY = '0000'
       ranking_Y = '0'
    if dt.strftime('%m') == DEFAULT_DATE.strftime('%m') and\
     dt2.strftime('%m') == DEFAULT_DATE2.strftime('%m'):
       outm = '00'
       ranking_m = '0'
    if dt.strftime('%d') == DEFAULT_DATE.strftime('%d') and\
     dt2.strftime('%d') == DEFAULT_DATE2.strftime('%d'):
       outd = '00'
       ranking_d = '0'
    
    output = outY + '-' + outm + '-' +outd  # update parsed dates  
    df.loc[i]['date_iso'] = output  # update dataframe





def parse_address_details(addr_str):
    # This function splits road/city/country from parsed addresses, and updates output dataframe
    # It uses parsed addresses produced from library 4 (Postal.parser), for example, (('Broadway','Road'),('NYC','City'))
    
    global df, i, ranking_addr

    for j in range(0,len(addr_str)):
        if addr_str[j][1] == 'city':
            df.loc[i]['city'] = addr_str[j][0]
            ranking_addr = '1'
        elif addr_str[j][1] == 'country':
            df.loc[i]['country'] = addr_str[j][0]
            ranking_addr = '1'
        elif addr_str[j][1] == 'road':
            df.loc[i]['road'] = addr_str[j][0]
            ranking_addr = '1'
        elif addr_str[j][1] == 'house_number':
            df.loc[i]['number'] = addr_str[j][0]
            ranking_addr = '1'           

                        

#%% converting json dataset to dataframe
df = pd.read_json('parsing_challenge.json')
df.columns = ['original_data']
df['original_data'] = df['original_data'].astype(str)

df['date_iso'] = df['number'] = df['road'] =\
df['city'] = df['country'] = df['ranking'] = ''


#%% Parsing
length = len(df)
for i in range(0, length): 
    string=df.loc[i]['original_data']
    ranking_addr = ranking_Y = ranking_m = ranking_d = '0'   #default ranking '0000'
    
    #%% Using dateutil.parser (library 1) to parse dates
    try:
        DEFAULT_DATE = datetime.datetime(1, 1, 1)   #set random default values for incomplete dates
        dt = dateutil.parser.parse(string, default=DEFAULT_DATE).date() # parse datetime
        df.loc[i]['date_iso'] = dt.strftime('%Y-%m-%d')  # output datetime
        ranking_Y = ranking_m = ranking_d = '1'  #update ranking
    
        # see if default values are used (which also means input datetime is incomplete) 
        if dt.strftime('%Y') == DEFAULT_DATE.strftime('%Y') or\
            dt.strftime('%m') == DEFAULT_DATE.strftime('%m') or\
            dt.strftime('%d') == DEFAULT_DATE.strftime('%d'):  
    
            parse_incomplete_date(string)  # replace default values with '0', update dataframe
       



    except:
        #%% Using dateparser (library 2) to parse dates in non-English
        is_date = dateparser.parse(string) #parsing
        if is_date:
            date_str = is_date.strftime('%Y-%m-%d')   #set format for dates (e.g., 2011-01-01)
            df.loc[i]['date_iso'] = date_str
            ranking_Y = ranking_m = ranking_d = '1'   # update ranking
         
            
        #%% If library 1&2 fail, use datefinder (library 3) to extract dates from texts
        else:                             
            matches = datefinder.find_dates(string,index=True)  # parsing dates, return date index
            #%% if dates are found in texts, extract dates
            if list(datefinder.find_dates(string,index=True)):   
                for match in matches:                                      
                    date = match[0]
                    date_str = date.strftime('%Y-%m-%d') #set format for dates (e.g., 2011-01-01)
                    df.loc[i]['date_iso'] = date_str
                    ranking_Y = ranking_m = ranking_d = '1'    
                    
                    #%% then use the remaining string to parse addresses
                    letters = string[:match[1][0]]   # extract address from text using date index
                    Parsed_address = parse_address(letters)   # parsing addresses, output example: (('Broadway','Road'),('NYC','City'))
                    parse_address_details(Parsed_address)  #split parsed addresses into road/city/country 
            
            
            #%% if dates are not found in text, use the whole string to parse address
            else:                    
                letters = string
                Parsed_address = parse_address(letters)  # parsing addresses, output example: (('Broadway','Road'),('NYC','City'))
                parse_address_details(Parsed_address)  #split parsed addresses into road/city/country
    
    # output ranking
    ranking_all = ranking_addr + ranking_Y + ranking_m +ranking_d # ranking is a four digit number
    df.loc[i]['ranking'] = ranking_all
  
 



#%% save dataframe to json
df.drop(['original_data'],axis = 1,inplace=True) #drop original data
df.to_json('result.json',orient='records',lines='True')   # output parsed dates and addresses 











                        
                        

