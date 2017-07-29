def marubozo(df, dffull, var=0.01, oc=.05):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date
  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0)
  dfo = dfy[(dfy.DATE ==dfy.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True)
  dfx =dfo[['DATE','OPEN','HIGH','LOW','CLOSE','SC_CODE','SC_NAME']].copy()

  dfx['HIGHVAR'] = abs((dfx['HIGH']-dfx['CLOSE'])/dfx['HIGH'])
  dfx['LOWVAR'] = abs((dfx['LOW']-dfx['OPEN'])/dfx['LOW'])
  dfx['MARUP'] = abs(dfx['CLOSE']-dfx['OPEN'])/dfx['OPEN']
  dfx['MARYESNO'] = 0
  dfx.MARYESNO[(dfx['HIGHVAR']<var) & (dfx['LOWVAR']<var) & (dfx['MARUP']>oc)] = 1
  return dfx['MARUP']*dfx['MARYESNO']

    

def hangingman(df, dffull):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date
  
  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfo = dfy[(dfy.DATE == dfy.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True)
  dfx =dfo[['DATE','OPEN','HIGH','LOW','CLOSE','SC_CODE','SC_NAME']].copy()
  dfx['HANGING'] =0
  
  dfx['OCVAR'] = (dfx['CLOSE']-dfx['OPEN'])/dfx['CLOSE']
  dfx['CLVAR'] = (dfx['CLOSE']-dfx['LOW'])/dfx['CLOSE']
  dfx.HANGING[( abs(dfx['CLVAR'])> abs(2*dfx['OCVAR']) )] = 1
  #print dfx

  return dfx['HANGING']

def bullisheng(df, dffull):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','OPEN','HIGH','LOW','CLOSE','SC_CODE','SC_NAME']].copy()
  
  
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['BULLISHENG'] = 0
  for a in dfo.SC_CODE:
    df1 = dfx[(dfx['SC_CODE'] == a)].sort_values(by =['DATE'],ascending =1).reset_index(drop = True).copy()
          
    k= len(df1)-2
    if (dfy.CLOSE[k] > dfy.OPEN[k+1]) and (dfy.OPEN[k] < dfy.CLOSE[k+1]) and (dfy.CLOSE[k] <dfy.OPEN[k]):
      z = dfo[dfo['SC_CODE'] == a].index
      dfo.set_value(z,'BULLISHENG',1) 

  return dfo['BULLISHENG']


def pearcingpattern(df, dffull):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','OPEN','HIGH','LOW','CLOSE','SC_CODE','SC_NAME']].copy()
  
  
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['PEARCING'] = 0

  for a in dfo.SC_CODE:
    df1 = dfx[(dfx['SC_CODE'] == a)].sort_values(by =['DATE'],ascending =1).reset_index(drop = True).copy()
          
    k= len(df1)-2
    if (dfy.OPEN[k] > dfy.CLOSE[k]) and (dfy.OPEN[k]> dfy.OPEN[k+1]) and \
       (dfy.OPEN[k+1] < dfy.CLOSE[k+1]) and (abs(dfy.OPEN[k]-dfy.CLOSE[k]) > 0.5*abs(dfy.OPEN[k+1] - dfy.CLOSE[k+1])) and \
       (abs(dfy.OPEN[k]-dfy.CLOSE[k]) < abs(dfy.OPEN[k+1]-dfy.CLOSE[k+1])):    
      z = dfo[dfo['SC_CODE'] == a].index
      dfo.set_value(z,'PEARCING',1) 

  return dfo['PEARCING']


def crossover(df, dffull):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','OPEN','HIGH','LOW','CLOSE','SC_CODE','SC_NAME']].copy()
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['CROSSOVER'] = 0

def month6profit(df, dffull):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','CLOSE','SC_CODE','SC_NAME']].copy()
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['Profit'] = 0

  for a in dfo.SC_CODE:
    df1 = dfx[(dfx['SC_CODE'] == a)].sort_values(by =['DATE'],ascending =1).reset_index(drop = True).copy()
    prof = df1.CLOSE[len(df1)-1] - df1.CLOSE[0]
    z = dfo[dfo['SC_CODE'] == a].index
    dfo.set_value(z,'Profit',prof)
  return dfo['Profit']


def volumepercent(df,dffull,n=10):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','NO_OF_SHRS','SC_CODE','SC_NAME']].copy()
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['Volumeper'] = 0.0
  
  for a in dfo.SC_CODE:
    df1 = dfx[(dfx['SC_CODE'] == a)].sort_values(by =['DATE'],ascending =1).reset_index(drop = True).copy()
    volper = df1.NO_OF_SHRS[-1:].mean()/df1.NO_OF_SHRS[-n:].mean()
    z = dfo[dfo['SC_CODE'] == a].index.item()
    dfo.set_value(z,'Volumeper',volper)
  return dfo['Volumeper']

def rsifun(df,dffull, n=14):
  import pandas as pd
  import csv
  import numpy as np
  from datetime import date

  dfy = pd.merge(dffull, df, how='inner', on=['SC_CODE']).sort_values(by =['DATE'],ascending =0).reset_index(drop = True)
  dfx =dfy[['DATE','CLOSE','SC_CODE','SC_NAME']].copy()
  dfo = dfx[(dfx.DATE ==dfx.DATE.head(n=1).item())].sort_values(by = ['SC_CODE']).reset_index(drop = True).copy()
  dfo['RSI'] = 0.0
    
  for a in dfo.SC_CODE:
    df1 = dfx[(dfx['SC_CODE'] == a)].sort_values(by =['DATE'],ascending =1).reset_index(drop = True).copy()
    delta = df1[['CLOSE']].diff()
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0    

    rollup = dUp.rolling(window=n,center=False).mean()
    rolldown = dDown.rolling(window=n,center=False).mean()
    #print rollup
    #print rolldown
    RS = rollup/abs(rolldown)

    rsi= 100.0 - (100.0 / (1.0 + RS))
    z = dfo[dfo['SC_CODE'] == a].index.item()

    dfo.set_value(z,'RSI',rsi[-1:].mean())
  return dfo['RSI']

def plotcandlestick(sccode, df):
  from matplotlib.dates import date2num
  import datetime, os
  import pandas as pd
  import csv
  import numpy as np
  from datetime import datetime
  import calendar

  dfx = df[(df['SC_CODE'] == sccode)].sort_values(by = 'DATE', ascending = 1).reset_index(drop = True)
  scname = dfx.SC_NAME.head(n=1).item()
  dfx['DATE2'] = 0
  for x in range(0,len(dfx)):
    dfx.DATE2[x] = date2num(datetime.strptime(dfx.DATE[x], "%m/%d/%Y"))

  dfx1 = dfx[['DATE2','OPEN','HIGH','LOW','CLOSE']]
  from pylab import *
  import matplotlib.pyplot as plt
  from datetime import datetime
  import time
  from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, DayLocator, MONDAY
  from matplotlib.finance import candlestick_ohlc 


  mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
  alldays    = DayLocator()              # minor ticks on the days
  weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
  dayFormatter = DateFormatter('%d')      # e.g., 12


  #Prices format date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]

  Prices = dfx1.values.tolist()
  #and then following the official example. 
  fig, ax = plt.subplots()
  fig.subplots_adjust(bottom=0.2)
  ax.xaxis.set_major_locator(mondays)
  ax.xaxis.set_minor_locator(alldays)
  ax.xaxis.set_major_formatter(weekFormatter)
  candlestick_ohlc(ax, Prices, width=0.6)

  ax.xaxis_date()
  ax.autoscale_view()
  plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
  plt.title(scname)
  plt.show()



