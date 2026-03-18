import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src.analytics import subregion_channel_analysis
def show(df):
    st.header("Subregion Channel Analysis")

    subregion_data = subregion_channel_analysis(df).round(2)

    melted = subregion_data.reset_index().melt(
        id_vars="Subregion",
        var_name="Channel",
        value_name="Orders"
    )

    fig = px.density_heatmap(
        melted,
        x="Channel",
        y="Subregion",
        z="Orders",
        color_continuous_scale="RdYlBu_r",title="Channel Share by Subregion (Heatmap)",text_auto=True)
    
    fig.update_layout(height=500)

    st.plotly_chart(fig, use_container_width=True)


    subregion_data_percent = (subregion_data.div(subregion_data.sum(axis=1),axis=0)).round(2)*100
    subregion_data_percent = subregion_data_percent.reset_index()
    melted_percent = subregion_data_percent.melt(
        id_vars="Subregion",
        var_name="Channel",
        value_name="Orders"
    )
    fig2 = px.density_heatmap(
        melted_percent,
        x="Channel",
        y="Subregion",
        z="Orders",
        color_continuous_scale="RdYlBu_r",title="Channel Share % by Subregion (Heatmap)",text_auto=True)
    
    fig2.update_layout(height=500)

    st.plotly_chart(fig2, use_container_width=True)
