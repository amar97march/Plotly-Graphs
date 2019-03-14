import plotly.offline as pyo 
import plotly.graph_objs as go 
import pandas as pd
import numpy as np 

df = pd.read_csv('abalone.csv')
data1 = np.random.choice(df['rings'], 10, replace = False)
data2 = np.random.choice(df['rings'], 10, replace = False)

data = [go.Box(y = data1, name = 'Data 1'),
        go.Box(y = data2, name = 'Data 2')]

layout = go.Layout(title = 'Box Compare')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)
