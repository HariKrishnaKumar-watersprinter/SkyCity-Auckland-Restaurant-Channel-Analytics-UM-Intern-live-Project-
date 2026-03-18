import pandas as pd
import streamlit as st
path="https://raw.githubusercontent.com/HariKrishnaKumar-watersprinter/SkyCity-Auckland-Restaurant-Channel-Analytics-UM-Intern-live-Project-/main/data/SkyCity Auckland Restaurants & Bars.csv"
@st.cache_data
def load_data():
    df = pd.read_csv(path)
    return df

df = load_data()
