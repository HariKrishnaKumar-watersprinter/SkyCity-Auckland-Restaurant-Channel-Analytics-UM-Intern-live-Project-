import streamlit as st
import plotly.express as px
from src.anomaly_detection import detect_multiple_outliers

def show(df):

    st.header("Outlier Detection")

    results = detect_multiple_outliers(df)

    for col,outliers in results.items():

        st.subheader(col)

        fig = px.box(df,y=col)

        st.plotly_chart(fig)

        if len(outliers)>0:

            st.dataframe(
                outliers[
                    ["RestaurantName","Subregion",col]
                ]
            )