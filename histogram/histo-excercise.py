import plotly.graph_objs as go 
import plotly.offline as pyo 
import pandas as pd 

df = pd .read_csv('abalone.csv')

data = [go.Histogram(x = df['length'], xbins = dict(start = 0, end = 1, size = 0.02))]
layout = go.Layout(title = 'Histogram Exercise')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)