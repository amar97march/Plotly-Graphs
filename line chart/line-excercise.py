import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('2010YumaAZ.csv')
days = ['TUESDAY','WEDNESSDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

data = []
for day in days:
    
    trace = go.Scatter(x = df['LST_TIME'],
                        y = df[df['DAY']== day]['T_HR_AVG'],
                        mode = 'lines',
                        name = day)
    data.append(trace)

layout = go.Layout(title = 'temp 01-07')
fig = go.Figure(data, layout)
pyo.plot(fig)