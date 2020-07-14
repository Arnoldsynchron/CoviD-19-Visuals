# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:59:11 2020

@author: Arnauld
"""

import pandas as pd
import numpy as np
import plotly as py
import dash
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

data = pd.read_csv('covid_19_data.csv')

data.rename(columns={'SNo':'Serial Number','ObservationDate':'Date','Country/Region':'Country'}, inplace=True)

df_countries =  data.groupby(['Country','Date']).sum().reset_index().sort_values('Date',ascending=False)
df_countries = df_countries.drop_duplicates(['Country'])
df_countries= df_countries[df_countries['Confirmed']>0]

fig = go.Figure(data =go.Choropleth(locations = df_countries['Country'],locationmode = 'country names', z = df_countries['Confirmed'], colorscale = 'Reds', marker_line_color = 'black', marker_line_width = 0.5))
fig.update_layout(title_text = 'Confirmed Cases as of April 08, 2020', title_x = 0.5, geo=dict(showframe=False,
                                                                                               showcoastlines=False,projection_type ='equirectangular'))
fig.show(renderer = 'png')


#Animated choropleth (Dataset and Visualization)
df_countrydate = data[data['Confirmed']>0]
df_countrydate = data.groupby(['Country','Date']).sum().reset_index()
#df_countrydate = df_countrydate.drop_duplicates(['Country'])

gig = px.choropleth(df_countrydate,locations="Country", locationmode='country names',color='Confirmed',hover_name = 'Country',animation_frame='Date')
gig.update_layout(title_text = 'Global Spread of Coronavirus', title_x = 0.5, geo = dict(showframe=False,showcoastlines=False))
gig.show()

