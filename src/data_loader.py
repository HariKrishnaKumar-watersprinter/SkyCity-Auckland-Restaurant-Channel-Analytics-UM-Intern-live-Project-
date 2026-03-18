import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path=r"F:\Project\unified mentor\skycity_channel_analytics\data\SkyCity Auckland Restaurants & Bars.csv"):
    df = pd.read_csv(path)
    return df

df = load_data()
