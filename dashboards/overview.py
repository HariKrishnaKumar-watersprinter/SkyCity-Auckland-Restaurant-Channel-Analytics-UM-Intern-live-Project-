import streamlit as st
import plotly.express as px
import pandas as pd
from src.analytics import channel_volume,delivery_instore




def show(df):
    st.header("Channel order Overview")

    # Create a DataFrame directly
    orders_df = channel_volume(df)
    # Sort the DataFrame by 'Orders' in descending order
    orders_df = orders_df.sort_values(by="Orders", ascending=False)

    c1, c2 = st.columns([2, 1])
    
    with c2:
        # Plotly Pie Chart
        fig = px.pie(
            orders_df,
            names="Channel",
            values="Orders",
            title=" Channel Order Distribution %",
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)

    with c1:
        # Plotly Bar Chart (Vertical)
        fig2 = px.bar(
            orders_df,
            x="Channel",
            y="Orders",
            color="Channel",
            title="Channel Order Volume (Ranked)"
        )
        
        # Update layout to enforce the ranking order on the x-axis
        #fig2.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': orders_df['Channel']})
        
        # Add text labels
        fig2.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
        
        st.plotly_chart(fig2, use_container_width=True)

    comp_df=delivery_instore(df)

    fig3=px.bar(
        comp_df,
        x="Channel",
        y="Orders",
        color="Channel",
        title="Delivery vs In-Store Orders"
    )
    fig3.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
    st.plotly_chart(fig3, use_container_width=True)
    