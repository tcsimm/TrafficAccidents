# U.S. Traffic Accidents Analysis Dashboard

This project explores and visualizes over 4 million traffic accidents across the U.S. using Python, SQL, and Streamlit. It highlights peak accident times, high-risk states and cities, and how weather conditions correlate with severity. The goal is to provide clear, data-driven insights into road safety patterns and help build a public-facing interactive dashboard.

---

## Dataset

- Source: [Kaggle – U.S. Accidents (Dec 2023)](https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents)
- Contains records from 2016 to 2023
- Key features:
  - `Start_Time`, `End_Time`, `Severity`, `State`, `City`
  - Environmental: `Weather_Condition`, `Visibility`, `Temperature`, etc.
  - Geolocation: `Latitude`, `Longitude`

---

## Key insights overall

- **Rush hours (around 7–9 AM and 4–6 PM)** are peak accident times.
- **California, Texas, and Florida** have the most reported accidents.
- **Fog, rain, and snow** conditions are correlated with higher accident severity.

These insights were derived using SQL queries and visualized in Python and Streamlit.

---

## Tools and technologies

- **Python** – Data manipulation & analysis
- **Pandas, Plotly, Seaborn, Matplotlib** – Visualization & EDA
- **SQLite + SQL** – Querying structured accident data
- **Streamlit + Folium** – Interactive dashboard and geospatial mapping
