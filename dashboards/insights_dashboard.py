import streamlit as st
from utils.helpers import advanced_insights

def show(df):

    st.header("Business Insights")

    insights = advanced_insights(df)

    for ins in insights:
        st.write("•", ins)
    if st.button("Generate Executive Report"):
        path = generate_report(df)

        with open(path, "rb") as f:
            st.download_button(
                "Download Report",
                    f,
                file_name="SkyCity_Report.pdf")
