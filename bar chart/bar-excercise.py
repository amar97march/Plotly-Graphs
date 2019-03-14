import pandas as pd 
import plotly.graph_objs as go 
import plotly.offline as pyo 

df = pd.read_csv('mocksurvey.csv')


col = ['Strongly Agree','Somewhat Agree','Neutral','Somewhat Disagree','Strongly Disagree']
data = [go.Bar(x = df.ix[:,0], y = df[column], name = column) for column in col]

layout = go.Layout(title = 'Poll Graph', barmode= 'stack')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig)