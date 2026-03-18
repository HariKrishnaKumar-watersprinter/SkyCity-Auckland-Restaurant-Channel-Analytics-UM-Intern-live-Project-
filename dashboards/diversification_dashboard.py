import streamlit as st
import plotly.express as px

def show(df):

    st.header("Channel Diversification Analysis")

    st.write(
        "Measures how balanced restaurant order channels are."
    )

    # Distribution histogram
    fig = px.histogram(
        df,
        x="DiversificationScore",
        nbins=30,
        title="Diversification Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

    # Boxplot by segment
    fig2 = px.box(
        df,
        x="Segment",
        y="DiversificationScore",
        title="Diversification Score by Restaurant Segment"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # Scatter view
    fig3 = px.scatter(
        df,
        x="MonthlyOrders",
        y="DiversificationScore",
        color="CuisineType",
        hover_data=["RestaurantName"]
    )

    st.plotly_chart(fig3, use_container_width=True)