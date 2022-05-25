import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('data.csv')
data = df.groupby('level')['attempt'].mean()
graph = go.Figure(go.Bar(x = data, y = ['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
graph.show()