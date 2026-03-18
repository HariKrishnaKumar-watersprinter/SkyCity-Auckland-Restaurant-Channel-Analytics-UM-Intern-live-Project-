import streamlit as st
import plotly.express as px
from src.analytics import profit_analysis
def show(df):

    st.header("Channel Profitability Analysis")

    profit_data =profit_analysis(df)

    fig = px.bar(
        profit_data,
        x="Channel",
        y="NetProfit",
        color="Channel",
        title="Total Profit by Channel",
        color_discrete_sequence=px.colors.qualitative.Dark2
    )
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='outside',)
    fig.update_layout(
        width=800,   # Sets the width in pixels
        height=500   # Sets the height in pixels
    )
    st.plotly_chart(fig,)