import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path=r"https://raw.githubusercontent.com/HariKrishnaKumar-watersprinter/SkyCity-Auckland-Restaurant-Channel-Analytics-UM-Intern-live-Project-/main/data/SkyCity Auckland Restaurants & Bars.csv"):
    df = pd.read_csv(path)
    return df

df = load_data()
