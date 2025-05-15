# Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Page config
st.set_page_config(layout="wide", page_title="U.S. Traffic Accidents Dashboard")

st.title("U.S. Traffic Accidents Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("../data/us_accidents_cleaned.csv", parse_dates=["Start_Time"])
    df['Date'] = df['Start_Time'].dt.date
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

state = st.sidebar.selectbox("Select State", sorted(df['State'].dropna().unique()), index=0)
city_options = df[df['State'] == state]['City'].dropna().unique()
city = st.sidebar.selectbox("Select City", sorted(city_options))

severity = st.sidebar.multiselect(
    "Select Severity Level",
    sorted(df['Severity'].unique()),
    default=sorted(df['Severity'].unique())
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['Date'].min(), df['Date'].max()]
)

# Filtered data
filtered_df = df[
    (df['State'] == state) &
    (df['City'] == city) &
    (df['Severity'].isin(severity)) &
    (df['Date'] >= date_range[0]) &
    (df['Date'] <= date_range[1])

]

st.markdown(f"Showing {len(filtered_df):,} accidents in **{city}, {state}**")

# Charts
col1, col2 = st.columns(2)

with col1:
    by_hour = filtered_df['Hour'].value_counts().sort_index()
    fig_hour = px.bar(
        x=by_hour.index,
        y=by_hour.values,
        labels={'x': 'Hour of Day', 'y': 'Number of Accidents'},
        title='Accidents by Hour of Day'
    )
    st.plotly_chart(fig_hour, use_container_width=True)

with col2:
    by_weekday = filtered_df['Weekday'].value_counts()
    fig_weekday = px.bar(
        x=by_weekday.index,
        y=by_weekday.values,
        labels={'x': 'Day of Week', 'y': 'Number of Accidents'},
        title='Accidents by Day of Week'
    )
    st.plotly_chart(fig_weekday, use_container_width=True)

# Map
st.markdown("Accident Locations Map")

if not filtered_df.empty:
    m = folium.Map(location=[filtered_df['Start_Lat'].mean(), filtered_df['Start_Lng'].mean()], zoom_start=11)
    HeatMap(filtered_df[['Start_Lat', 'Start_Lng']].dropna().values.tolist(), radius=8).add_to(m)
    st_folium(m, width=700, height=500)
else:
    st.warning("No data available for these filters")

