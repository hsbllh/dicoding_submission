import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setting the theme for Seaborn plots
sns.set(style='dark')

# Load the data
days_df = pd.read_csv("dashboard/clean_data_day.csv")
Hour_df = pd.read_csv("dashboard/clean_data_hour.csv")

# Pastikan kolom 'Date' diformat dengan benar
if 'Date' in days_df.columns:
    days_df['Date'] = pd.to_datetime(days_df['Date'])

if 'Date' in Hour_df.columns:
    Hour_df['Date'] = pd.to_datetime(Hour_df['Date'])

# Sidebar - date input
min_date_days = days_df["Date"].min()
max_date_days = days_df["Date"].max()

with st.sidebar:
    st.image("dashboard/profile.png")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )

# Filter data based on the selected date range
main_df_days = days_df[(days_df["Date"] >= str(start_date)) & 
                       (days_df["Date"] <= str(end_date))]
main_df_Hour = Hour_df[(Hour_df["Date"] >= str(start_date)) & 
                        (Hour_df["Date"] <= str(end_date))]

# Dashboard Header
st.header('Bike Sharing Data Dashboard')

# Chart 1: Hubungan antara Temperatur dan Jumlah Transaksi
st.subheader('Pengaruh cuaca terhadap jumlah transaksi')

# Korelasi antara variabel
correlations = main_df_days[['Temperature', 'Humidity', 'Wind Speed', 'Count']].corr()
st.write(correlations)

# Scatter plot: Temperature vs Count
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Count', data=main_df_days, ax=ax)
ax.set_title('Hubungan antara Temperatur dan Jumlah Transaksi')
ax.set_xlabel('Temperatur')
ax.set_ylabel('Jumlah Transaksi')
st.pyplot(fig)

# Bar plot: Rata-rata Jumlah Transaksi per Kondisi Cuaca
st.subheader('Rata-rata Jumlah Transaksi per Kondisi Cuaca')

weather_group = main_df_days.groupby('Weather Condition')['Count'].mean()
st.write(weather_group)

fig, ax = plt.subplots(figsize=(10, 6))
weather_group.plot(kind='bar', ax=ax)
ax.set_title('Rata-rata Jumlah Transaksi per Kondisi Cuaca')
ax.set_xlabel('Kondisi Cuaca')
ax.set_ylabel('Rata-rata Jumlah Transaksi')
st.pyplot(fig)

# Chart 2: Tren Peminjaman Sepeda Sepanjang Tahun
st.subheader('Tren Peminjaman Sepeda Sepanjang Tahun')

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='Date', y='Count', data=main_df_days, ax=ax)
ax.set_title('Tren Peminjaman Sepeda Sepanjang Tahun')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Peminjaman')
st.pyplot(fig)

# Footer: Insights

