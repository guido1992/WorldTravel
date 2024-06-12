# -*- coding: utf-8 -*-

import streamlit as st
import plotly.express as px
import pandas as pd

# List of countries you've visited
visited_countries = ['United States of America', 'Ireland', 'United Kingdom', 'France',
                     'Spain', 'Netherlands', 'Belgium', 'Germany', 'Denmark', 'Sweden', 'Finland',
                     'Italy', 'Switzerland', 'Austria', 'Croatia', 'Poland', 'Greece', 'Ghana',
                     'Namibia', 'Botswana', 'Zambia', 'Zimbabwe', 'South Africa', 'Israel', 'Turkey',
                     'China']

# Load country and continent data from CSV
csv_url = r'C:\Users\alexa\Desktop\Streamlit\Countries-Continents.csv'
df = pd.read_csv(csv_url)

### ----- TITLE -----
st.title("Countries Visited")

# Ensure the DataFrame has 'country' and 'continent' columns
df.columns = ['continent', 'country']

# Add a column to indicate if a country has been visited
df['visited'] = df['country'].isin(visited_countries)

# Create the world map
fig = px.choropleth(df, locations='country', locationmode='country names', color='visited',
                    color_continuous_scale=[[0, 'lightgrey'], [1, 'green']])
                    #title="Countries Visited")

st.plotly_chart(fig)

# Calculate continent statistics
continent_stats = df.groupby('continent').agg(
    total_countries=('country', 'count'),
    visited_countries=('visited', 'sum')
).reset_index()

continent_stats['percentage_visited'] = (continent_stats['visited_countries'] / continent_stats['total_countries']) * 100

st.subheader("Continent Statistics")
st.dataframe(continent_stats)