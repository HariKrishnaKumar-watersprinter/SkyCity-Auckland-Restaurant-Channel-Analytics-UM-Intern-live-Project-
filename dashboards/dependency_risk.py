import streamlit as st
import pandas as pd
from src.risk_model import apply_risk_classification
import plotly.express as px
def show(df):

    st.header("Channel Dependency Risk Profiles")

    df = apply_risk_classification(df)

    st.write(
        "Restaurants categorized based on reliance on delivery aggregators."
    )

    # KPI Summary
    balanced = len(df[df["ChannelRiskProfile"]=="Balanced"])
    medium = len(df[df["ChannelRiskProfile"]=="Medium Risk"])
    high = len(df[df["ChannelRiskProfile"]=="High Risk"])

    col1,col2,col3 = st.columns(3)

    col1.metric("Balanced Restaurants", balanced)
    col2.metric("Medium Risk Restaurants", medium)
    col3.metric("High Risk Restaurants", high)

    st.divider()

    # Distribution Chart
    fig = px.histogram(
        df,
        x="AggregatorDependence",
        color="ChannelRiskProfile",
        nbins=30,
        title="Aggregator Dependence Distribution"
    )
    fig.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

    # Risk by Subregion
    st.subheader("Risk Profile by Subregion")

    subregion_risk = df.groupby(
        ["Subregion","ChannelRiskProfile"]
    ).size().reset_index(name="Count")

    fig2 = px.bar(
        subregion_risk,
        x="Subregion",
        y="Count",
        color="ChannelRiskProfile",
        barmode="stack"
    )
    fig2.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Restaurant Risk Table")

    st.dataframe(
        df[
            [
                "RestaurantName",
                "Subregion",
                "CuisineType",
                "AggregatorDependence",
                "ChannelRiskProfile"
            ]
        ].sort_values(
            "AggregatorDependence",
            ascending=False
        )
    )


   
    
