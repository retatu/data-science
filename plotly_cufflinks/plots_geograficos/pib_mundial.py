import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go


df = pd.read_csv("2014_World_GDP")

data = dict(type='choropleth',
            locations=df['CODE'],
            #locationmode='USA-states',
            #colorscale='YlOrRd',
            text=df['COUNTRY'],
            #marker=dict(line={'color':'rgb(255,255,255)','width':2}),
            z=df['GDP (BILLIONS)'],
            colorbar={'title':'PIB em bilhões de dolares'})
#Show lakes vai mostrar os lagos e lakecolor é acor
layout=dict(title='PIB Mundo 2014', geo={'showframe':True, 'projection':{'type':'natural earth'}})
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)