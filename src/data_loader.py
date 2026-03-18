import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path=r"https://github.com/HariKrishnaKumar-watersprinter/SkyCity-Auckland-Restaurant-Channel-Analytics-UM-Intern-live-Project-/blob/main/data/SkyCity%20Auckland%20Restaurants%20%26%20Bars.csv"):
    df = pd.read_csv(path)
    return df

df = load_data()
