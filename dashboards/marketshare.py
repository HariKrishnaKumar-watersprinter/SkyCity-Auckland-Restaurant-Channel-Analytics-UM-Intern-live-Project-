import streamlit as st
import plotly.express as px
import pandas as pd
from src.analytics import market_share
def show(df):
    st.header("Channel order Overview")

    # Create a DataFrame directly

    share_df= market_share(df)

    # Sort the DataFrame by 'Orders' in descending order
    share_df = share_df.sort_values(by="share", ascending=False)

    c1, c2 = st.columns([2, 1])
    
    with c2:
        # Plotly Pie Chart
        fig = px.pie(
            share_df,
            names="Channel",
            values="share",
            title=" Channel share Distribution %",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        st.plotly_chart(fig, use_container_width=True)

    with c1:
        # Plotly Bar Chart (Vertical)
        fig2 = px.bar(
            share_df,
            x="Channel",    
            y="share",
            color="Channel",
            title="Channel share (Ranked)",
            color_discrete_sequence=px.colors.qualitative.Pastel1
        )
        
        # Update layout to enforce the ranking order on the x-axis
        fig2.update_layout(xaxis={'categoryorder': 'array', 'categoryarray': share_df['Channel']})
        
        # Add text labels
        fig2.update_traces(texttemplate='%{y:,.0f}', textposition='inside')
        
        st.plotly_chart(fig2, use_container_width=True)