import streamlit as st
from utils.helpers import advanced_insights

def show(df):

    st.header("Business Insights")

    insights = advanced_insights(df)

    for ins in insights:
        st.write("•", ins)