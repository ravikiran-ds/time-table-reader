# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:16:23 2020

@author: HP
"""
import pandas as pd
import numpy as np
import datetime
import calendar
from  speak import SpeakText
import speech_recog as sr

df=pd.read_csv('time_table.csv')
sp=SpeakText()
text='today'
#reader
def curr_day_schedule():
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    date="{} {} {}".format(day,month,year)
    curr_day=datetime.datetime.strptime(date, '%d %m %Y').weekday()
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                             "Friday", "Saturday", "Sunday"] 
    today=days[curr_day]
    sp.Speak("Hello")
    sp.Speak("today is {}".format(today))
    periods=df.columns[1:]
    #df.loc[df["Day\Period"]==today,periods]
    for i in range(0,6):
        sp.Speak(periods[i])
        sp.Speak(df.loc[df["Day\Period"]==today,periods[i]].values)
        #print(df.loc[df["Day\Period"]==today,periods[i]].values)
    sp.Speak("Thats it!")

#for speech recog un-comment the get_text_from_speech line
#say today
#text=sr.get_text_from_speech() 

if text=='today':
    curr_day_schedule()



    
