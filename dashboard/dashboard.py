import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")

with st.sidebar:
    st.image("https://www.ppsthane.com/wp-content/uploads/2014/11/Air-Pollution.jpg")
    
    available_years = sorted(all_df['year'].unique())
    selected_year = st.sidebar.selectbox("Pilih Tahun", available_years)
    filtered_data = all_df[all_df['year'] == selected_year]

st.header('Air Quality :fog:')

st.subheader("Tingkat Rata-rata Konsentrasi Polusi Udara per-Tahun")
col1, col2 = st.columns(2)
with col1:
    avg_pm25 = filtered_data['PM2.5'].mean()
    avg_pm25_rounded = round(avg_pm25, 2)
    st.metric("Rata-rata Konsentrasi PM2.5", value=avg_pm25_rounded)

with col2:
    avg_pm10 = filtered_data['PM10'].mean()
    avg_pm10_rounded = round(avg_pm10, 2)
    st.metric("Rata-rata Konsentrasi PM10", value=avg_pm10_rounded)

avg_pm25_by_year = all_df.groupby('year')['PM2.5'].mean()
fig, ax = plt.subplots()
ax.plot(avg_pm25_by_year.index, avg_pm25_by_year.values, marker='o')
ax.set_xlabel('Tahun')
ax.set_ylabel('Rata-rata Konsentrasi PM2.5')
st.pyplot(fig)

st.subheader("Tingkat Rata-rata Konsentrasi Polusi Udara berdasarkan Stasiun")

avg_pollution_by_station = all_df.groupby('station')['PM2.5'].mean()
min_pollution_station = avg_pollution_by_station.idxmin()

fig, ax = plt.subplots()
avg_pollution_by_station.plot(kind='bar', ax=ax)
ax.set_ylabel('Rata-rata PM2.5')
ax.set_xlabel('Stasiun')
st.pyplot(fig)

st.caption('Copyright (c) Figo Kurniawan Siswanto-ML 50')
