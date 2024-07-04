# -*- coding: utf-8 -*-

# Import Libraries
import streamlit as st
import plotly.express as px
import pandas as pd

# List of countries that I have visited
visited_countries = ['United States of America', 'Ireland', 'United Kingdom', 'France','Iceland',
                     'Spain', 'Netherlands', 'Belgium', 'Germany', 'Denmark', 'Sweden', 'Finland',
                     'Italy', 'Switzerland', 'Austria', 'Croatia', 'Poland', 'Greece', 'Ghana',
                     'Namibia', 'Botswana', 'Zambia', 'Zimbabwe', 'South Africa', 'Mauritius', 'Israel',
                     'Turkey', 'China', 'Serbia']

# Path to the csv file
csv_path = r'Countries-Continents.csv'  # Update this path if necessary

# Load country and continent data from CSV
df = pd.read_csv(csv_path)

# App Title
st.title("Countries Visited")

# Ensure the DataFrame has 'country' and 'continent' columns
df.columns = ['continent', 'country']

# Add a column to indicate if a country has been visited
df['visited'] = df['country'].isin(visited_countries)

# Create the world map
fig = px.choropleth(
    df,
    locations='country',
    locationmode='country names',
    color='visited',
    color_continuous_scale=[[0, 'lightgrey'], [1, 'green']],
    #title="Countries Visited"
)

# Increase the size of the map and remove the border
fig.update_layout(
    autosize=False,
    width=2500,  # Adjust the width
    height=350,  # Adjust the height
    margin=dict(l=0, r=0, b=0, t=0),  # Remove the border
    paper_bgcolor='rgba(0,0,0,0)',  # Set the background color to transparent
    plot_bgcolor='rgba(0,0,0,0)'  # Set the plot background color to transparent
)

fig.update_geos(showcoastlines=False, showframe=False)

# Calculate continent statistics
continent_stats = df.groupby('continent').agg(
    total_countries=('country', 'count'),
    visited_countries=('visited', 'sum')
).reset_index()

continent_stats['percentage_visited'] = (continent_stats['visited_countries'] / continent_stats['total_countries']) * 100

# Create a row of summary boxes
#st.subheader("Continent Statistics")
cols = st.columns(len(continent_stats))
for col, (continent, total, visited, percentage) in zip(cols, continent_stats.values):
    col.metric(continent, f"{visited}/{total}", f"{percentage:.0f}%")

# Show figure
st.plotly_chart(fig)

#st.subheader("Continent Statistics")
#st.dataframe(continent_stats)
