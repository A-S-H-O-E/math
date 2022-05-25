import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv('data.csv')
ps = df.loc[df['student_id']=='TRL_xsl']
sdf = ps.groupby('level')['attempt'].mean()
graph = go.Figure(go.Bar(x = sdf,y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
graph.show()