import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd 

df = pd.read_csv('2018WinterOlympics.csv')
print(df)

trace0 = go.Bar(x= df['NOC'],
                y= df['Gold'],
                marker = dict(color = '#FFD700'))

trace1 = go.Bar(x= df['NOC'],
                y= df['Silver'],
                marker = dict(color = '#9EA0A1'))

trace2 = go.Bar(x= df['NOC'],
                y= df['Bronze'],
                marker = dict(color = '#CD7F32'))

data = [trace0,trace1,trace2]

layout = go.Layout(title = 'Medals',barmode = 'stack')
fig = go.Figure(data = data,layout = layout)
pyo.plot(fig)