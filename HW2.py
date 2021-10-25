# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:53:26 2021

@author: philip.moffatt
"""

import pandas as pd
import matplotlib as plt
from matplotlib import *
import sys
from pylab import *
import numpy as np

#3b data manipulation
# load data files for each model 
china4 = pd.read_csv('hw2RawData/China4.csv', parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
china8 = pd.read_csv('hw2RawData/China8.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
Norway4 = pd.read_csv('hw2RawData/NorESM1_M4.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
Norway8 = pd.read_csv('hw2RawData/NorESM1_M8.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
US4 = pd.read_csv('hw2RawData/GFDL_ESM2M4.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
US8 = pd.read_csv('hw2RawData/GFDL_ESM2M8.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)
history = pd.read_csv('hw2RawData/GRIDMET.csv', header=9, parse_dates= {'Date': ['Year', 'Month', 'Day']},keep_date_col=True)

# change columns names
china4.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
china8.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
Norway4.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
Norway8.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
US4.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
US8.columns = ['Date','Year', 'Month', 'Day', 'taMax', 'taMin', 'prcp']
history.columns = ['Date','Year', 'Month', 'Day', 'taMin', 'taMax', 'prcp']

# group into annually monthly sum of precipitation
C4prcp_monthly = china4.groupby(["Year", "Month"])[["prcp"]].sum()
C8prcp_monthly = china8.groupby(["Year", "Month"])[["prcp"]].sum()
N4prcp_monthly = Norway4.groupby(["Year", "Month"])[["prcp"]].sum()
N8prcp_monthly = Norway8.groupby(["Year", "Month"])[["prcp"]].sum()
US4prcp_monthly = US4.groupby(["Year", "Month"])[["prcp"]].sum()
US8prcp_monthly = US8.groupby(["Year", "Month"])[["prcp"]].sum()
Hist_prcp_monthly = history.groupby(["Year", "Month"])[["prcp"]].sum()

# group into annual months average max and min temperature
C4taMax_monthly = china4.groupby(["Year", "Month"])[["taMax"]].mean()
C8taMax_monthly = china8.groupby(["Year", "Month"])[["taMax"]].mean()
N4taMax_monthly = Norway4.groupby(["Year", "Month"])[["taMax"]].mean()
N8taMax_monthly = Norway8.groupby(["Year", "Month"])[["taMax"]].mean()
US4taMax_monthly = US4.groupby(["Year", "Month"])[["taMax"]].mean()
US8taMax_monthly = US8.groupby(["Year", "Month"])[["taMax"]].mean()
Hist_taMax_monthly = history.groupby(["Year", "Month"])[["taMax"]].mean()
C4taMin_monthly = china4.groupby(["Year", "Month"])[["taMin"]].mean()
C8taMin_monthly = china8.groupby(["Year", "Month"])[["taMin"]].mean()
N4taMin_monthly = Norway4.groupby(["Year", "Month"])[["taMin"]].mean()
N8taMin_monthly = Norway8.groupby(["Year", "Month"])[["taMin"]].mean()
US4taMin_monthly = US4.groupby(["Year", "Month"])[["taMin"]].mean()
US8taMin_monthly = US8.groupby(["Year", "Month"])[["taMin"]].mean()
Hist_taMin_monthly = history.groupby(["Year", "Month"])[["taMin"]].mean()

# Merge temp and prcp files together for each model
C4_monthly = pd.merge(pd.merge(C4taMax_monthly, C4taMin_monthly, left_index=True, 
                      right_index=True), C4prcp_monthly, left_index=True,
                      right_index=True)
C8_monthly = pd.merge(pd.merge(C8taMax_monthly, C8taMin_monthly, left_index=True, 
                      right_index=True), C8prcp_monthly, left_index=True,
                      right_index=True)
N4_monthly = pd.merge(pd.merge(N4taMax_monthly, N4taMin_monthly, left_index=True, 
                      right_index=True), N4prcp_monthly, left_index=True,
                      right_index=True)
N8_monthly = pd.merge(pd.merge(N8taMax_monthly, N8taMin_monthly, left_index=True, 
                      right_index=True), N8prcp_monthly, left_index=True,
                      right_index=True)
US4_monthly = pd.merge(pd.merge(US4taMax_monthly, US4taMin_monthly, left_index=True, 
                      right_index=True), US4prcp_monthly, left_index=True,
                      right_index=True)
US8_monthly = pd.merge(pd.merge(US8taMax_monthly, US8taMin_monthly, left_index=True, 
                      right_index=True), US8prcp_monthly, left_index=True,
                      right_index=True)
Hist_monthly = pd.merge(pd.merge(Hist_taMax_monthly, Hist_taMin_monthly, left_index=True, 
                      right_index=True), Hist_prcp_monthly, left_index=True,
                      right_index=True)

# save each model's data to csv
C4_monthly.to_csv('C4_monthly.csv')
C8_monthly.to_csv('C8_monthly.csv')
N4_monthly.to_csv('N4_monthly.csv')
N8_monthly.to_csv('N8_monthly.csv')
US4_monthly.to_csv('US4_monthly.csv')
US8_monthly.to_csv('US8_monthly.csv')
Hist_monthly.to_csv('Hist_monthly.csv')

# completed tAvg and concotenation in excel to produce the below csv
data = pd.read_csv('HW2MonthlyData.csv')

# plotting the RCP 4.5 data over a monthly time scale
x = data['Month']

fig, axs = plt.subplots(2, 1)
axs[0].plot(x, data['C4_prcp'], ls='--', label='China')
axs[0].plot(x, data['Hist_prcp'], ls='solid', label='1980-2021')
axs[0].plot(x, data['N4_prcp'], ls="-.", label='Norway')
axs[0].plot(x, data['US4_prcp'], ls=":", label='US')
axs[1].plot(x, data['C4_taAvg'], ls="--")
axs[1].plot(x, data['Hist_taAvg'], ls="solid")
axs[1].plot(x, data['N4_taAvg'], ls="-.")
axs[1].plot(x, data['US4_taAvg'], ls=":")
axs[0].set_ylabel('Monthly Prcp, (mm)')
axs[1].set_ylabel('Monthly Temp, ($^\circ$C)')

fig.align_ylabels()

fig.legend(loc='upper right', bbox_to_anchor=(1.15, 0.8))

axs[0].text(-0.2,600,'Forecasted Precipitation and Temperature 2040-2069',
            style= 'oblique', size='14')
axs[0].text(2,500,'Wenatchee Forest, Washington State, USA (47.5,-121)')

# 3b Plotting RCP 8.5 over a monthly time scale
data8 = pd.read_csv('HW2MonthlyDataRCP8.csv')

x = data8['Month']

fig, axs = plt.subplots(2, 1)
axs[0].plot(x, data8['C8_prcp'], ls='--', label='China')
axs[0].plot(x, data8['Hist_prcp'], ls='solid', label='1980-2021')
axs[0].plot(x, data8['N8_prcp'], ls="-.", label='Norway')
axs[0].plot(x, data8['US8_prcp'], ls=":", label='US')
axs[1].plot(x, data8['C8_taAvg'], ls="--")
axs[1].plot(x, data8['Hist_taAvg'], ls="solid")
axs[1].plot(x, data8['N8_taAvg'], ls="-.")
axs[1].plot(x, data8['US8_taAvg'], ls=":")
axs[0].set_ylabel('Monthly Prcp, (mm)')
axs[1].set_ylabel('Monthly Temp, ($^\circ$C)')

fig.align_ylabels()

fig.legend(loc='upper right', bbox_to_anchor=(1.15, 0.8))

axs[0].text(-0.2,600,'Forecasted Precipitation and Temperature 2040-2069 (RCP8.5)',
            style= 'oblique', size='14')
axs[0].text(2,500,'Wenatchee Forest, Washington State, USA (47.5,-121)')


#------------------------------------------------------

# 3a
# pull ensemble precip data for 4.5 and 8.5, rename columns 
esblPrcpData = pd.read_csv('hw2RawData/EnsebleAnnualPrcpRCP4_8.csv')
esblPrcpData.columns = ['Year', '4avg', '4Lwr', '4Upr', '8avg', '8Lwr', '8Upr','HisAvg', 'HisLwr', 'HisUpr']

# pull ensemble temp data for 4.5 and 8.5
esblTempData = pd.read_csv('hw2RawData/EnsebleAnnualTempRCP4_8.csv')
esblTempData.columns = ['Year', '4avg', '4Lwr', '4Upr', '8avg', '8Lwr', '8Upr','HisAvg', 'HisLwr', 'HisUpr']

xP = esblPrcpData['Year']
xT = esblTempData['Year']

fig, axs = plt.subplots(2, 1)
axs2= axs[0].twinx()
axs3= axs[1].twinx()
axs[0].plot(xP, esblPrcpData['4Lwr'], ls='-.', color= 'm', alpha= 0.3)
axs[0].plot(xP, esblPrcpData['4avg'], ls='solid', color= 'm',
            label='Prcp')
axs[0].plot(xP, esblPrcpData['4Upr'], ls="-.", color= 'm', alpha= 0.3)
axs2.plot(xT, esblTempData['4Lwr'], ls=":", color= 'b', alpha= 0.3)
axs2.plot(xT, esblTempData['4avg'], ls="solid", color= 'b',
          label='Temp')
axs2.plot(xT, esblTempData['4Upr'], ls=":", color= 'b', alpha= 0.3)

axs[1].plot(xP, esblPrcpData['8Lwr'], ls='-.', color= 'm', alpha= 0.3)
axs[1].plot(xP, esblPrcpData['8avg'], ls='solid', color= 'm')
axs[1].plot(xP, esblPrcpData['8Upr'], ls="-.", color= 'm', alpha= 0.3)
axs3.plot(xT, esblTempData['8Lwr'], ls=":", color= 'b', alpha= 0.3)
axs3.plot(xT, esblTempData['8avg'], ls="solid", color= 'b')
axs3.plot(xT, esblTempData['8Upr'], ls=":", color= 'b', alpha= 0.3)

axs[1].set_ylabel('Annual Avg Prcp, (mm)')
axs[1].yaxis.set_label_coords(-0.1,1)
axs3.set_ylabel('Annual Avg Temp, ($^\circ$C)')
axs3.yaxis.set_label_coords(1.1,1)

fig.align_ylabels()

fig.legend(loc='upper right', bbox_to_anchor=(1.1, 0.85))

axs[0].text(2007,3300,'Forecasted Precipitation and Temperature',
            style= 'oblique', size='14')
axs[0].text(2010,3000,'Wenatchee Forest, Washington State, USA (47.5,-121)')
axs[0].text(2010,2500,'RCP 4.5')
axs[1].text(2010,2500,'RCP 8.5')

# plot normalized ranges for RCP4.5 and 8.5 Temp and Precip overtime
# pull data
rangeData = pd.read_csv('NormalizedRangeEnsembleT_P.csv')

x = rangeData['Year']

fig, axs = plt.subplots(1, 2)
axs[0].plot(x, rangeData['pRange4.5%'], ls='-.', label='RCP 4.5')
#axs[0].plot(x, rangeData['pRange8.5%'], ls=':', label='RCP 8.5')
axs[0].plot(x, rangeData['pRangeHis%'], ls="solid", label='Historic')
axs[1].plot(x, rangeData['tRange4.5%'], ls="-.")
#axs[1].plot(x, rangeData['tRange8.5%'], ls=":")
axs[1].plot(x, rangeData['tRangHis%'], ls="solid")

axs[0].set_ylim(0,1)
axs[1].set_ylim(0,1)
axs[0].set_ylabel('Estimate Range %')
#axs[1].set_ylabel('Monthly Temp, ($^\circ$C)')

fig.align_ylabels()
fig.legend(loc='upper right', bbox_to_anchor=(0.75, 0.3))
axs[0].text(1950,1.1,'Range of Ensemble Model Forecasts',
            style= 'oblique', size='14')
axs[0].text(1950,1.05,'Wenatchee Forest, Washington State, USA (47.5,-121)')
axs[0].text(2010,0.9,'Precip')
axs[1].text(2010,0.9,'Temp')













