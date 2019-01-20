import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go


df = pd.read_csv("2014_World_Power_Consumption")

data = dict(type='choropleth',
            locations=df['Country'],
            locationmode='country names',
            colorscale='YlGnBu',
            text=df['Text'],
            #marker=dict(line={'color':'rgb(255,255,255)','width':1}),
            z=df['Power Consumption KWH'],
            colorbar={'title':'Consumo de energia mundial'})
#Show lakes vai mostrar os lagos e lakecolor é acor
layout=dict(title='Exportações agricolas por estado', geo={'showframe':True, 'projection':{'type':'natural earth'}})
choromap = go.Figure(data=[data], layout=layout)
#plot(choromap)

df = pd.read_csv("2012_Election_Data")

data = dict(type='choropleth',
            locations=df['State Abv'],
            locationmode='USA-states',
            colorscale='Viridis',
            #text=df['Voting-Age Population (VAP)'],
            #marker=dict(line={'color':'rgb(255,255,255)','width':1}),
            z=df['Voting-Age Population (VAP)'],
            colorbar={'title':'Idade da população votante'})
#Show lakes vai mostrar os lagos e lakecolor é acor
layout=dict(title='Exportações agricolas por estado', geo={'scope':'usa', 'showlakes':True, 'lakecolor':'rgb(85,177,230)'})
choromap = go.Figure(data=[data], layout=layout)
plot(choromap)