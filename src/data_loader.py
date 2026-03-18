import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    repo = "HariKrishnaKumar-watersprinter/SkyCity-Auckland-Restaurant-Channel-Analytics-UM-Intern-live-Project-"
    branch = "main"
    file_path = "data/SkyCity Auckland Restaurants & Bars.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()
