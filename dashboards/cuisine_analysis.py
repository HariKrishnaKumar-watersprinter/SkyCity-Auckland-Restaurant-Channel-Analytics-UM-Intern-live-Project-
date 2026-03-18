import streamlit as st
import plotly.express as px
from src.analytics import cuisine_channel_mix
def show(df):

    st.header("Cuisine vs Channel Distribution")

    cuisine_data,segment_data= cuisine_channel_mix(df)

   
    melted = cuisine_data.melt(
        id_vars="CuisineType",
        var_name="Channel",
        value_name="Orders"
    )

    fig = px.bar(
        melted,
        x="CuisineType",
        y="Orders",
        color="Channel",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Prism
    )
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='inside',textangle=270,textfont_size=50)
    st.plotly_chart(fig, use_container_width=True)
    st.header("Segment vs Channel Distribution")
    
    

    melted_segment = segment_data.melt(
        id_vars="Segment",
        var_name="Channel",
        value_name="Orders"
    )

    fig2= px.bar(
        melted_segment,
        x="Segment",
        y="Orders",
        color="Channel",
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Antique
    )

    fig2.update_traces(texttemplate='%{y:,.0f}', textposition='outside',)
    st.plotly_chart(fig2, use_container_width=True)
