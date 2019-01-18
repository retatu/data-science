import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

data = dict(type='choropleth',
            locations=['IL','CA','PA'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['Illinois','California','Phila'],
            z=[1.0,2.0,3.0],
            colorbar={'title':'Titulo da barra de cores'})
layout=dict(geo={'scope':'usa'})
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)

df = pd.read_csv("2011_US_AGRI_Exports")

data = dict(type='choropleth',
            locations=df['code'],
            locationmode='USA-states',
            colorscale='YlOrRd',
            text=df['text'],
            marker=dict(line={'color':'rgb(255,255,255)','width':2}),
            z=df['total exports'],
            colorbar={'title':'Milhões de dolares'})
#Show lakes vai mostrar os lagos e lakecolor é acor
layout=dict(title='Exportações agricolas por estado', geo={'scope':'usa', 'showlakes':True, 'lakecolor':'rgb(85,177,230)'})
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)