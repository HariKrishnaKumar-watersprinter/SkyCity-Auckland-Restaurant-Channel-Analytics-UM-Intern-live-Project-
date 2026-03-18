import streamlit as st
from src.data_loader import load_data
from src.data_validation import validate_order_counts, validate_channel_share
from src.feature_engineering import create_kpis
from dashboards import overview
from dashboards import subregion_analysis
from dashboards import cuisine_analysis
from dashboards import profitability_analysis
from dashboards import executive_dashboard
from dashboards import dependency_risk
from dashboards import marketshare
from dashboards import diversification_dashboard
from dashboards import insights_dashboard


st.set_page_config(
    page_title="SkyCity Channel Analytics",
    page_icon="🍔",
    layout="wide"
)

st.title("🏙️ SkyCity Auckland Restaurant Channel Analytics")
st.markdown("**SkyCity Auckland Restaurants & Bars** • Hospitality Analytics Dashboard")
# Load data
df = load_data()

df = validate_order_counts(df)
df = validate_channel_share(df)
df = create_kpis(df)


# Sidebar Filters
st.sidebar.header("Filters")

subregion = st.sidebar.multiselect(
    "Subregion",
    df["Subregion"].unique()
)

cuisine = st.sidebar.multiselect(
    "Cuisine Type",
    df["CuisineType"].unique()
)

segment = st.sidebar.multiselect(
    "Restaurant Segment",
    df["Segment"].unique()
)

# Apply filters
if subregion:
    df = df[df["Subregion"].isin(subregion)]

if cuisine:
    df = df[df["CuisineType"].isin(cuisine)]

if segment:
    df = df[df["Segment"].isin(segment)]


# Page navigation
page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Dashboard",
        "Channel Overview",
        "Market Share",
        "Subregion Analysis",
        "Cuisine Analysis",
        "Profitability Analysis",
        "Dependency Risk",
        "Diversification Analysis",
        "Insights Dashboard"
    ]
)
if page == "Executive Dashboard":
    executive_dashboard.show(df)
elif page == "Channel Overview":
    overview.show(df)
elif page == "Market Share":
    marketshare.show(df)
elif page == "Subregion Analysis":
    subregion_analysis.show(df)

elif page == "Cuisine Analysis":
    cuisine_analysis.show(df)
elif page == "Profitability Analysis":
    profitability_analysis.show(df)
elif page == "Dependency Risk":
    dependency_risk.show(df)
elif page == "Diversification Analysis":
    diversification_dashboard.show(df)
elif page == "Insights Dashboard":
    insights_dashboard.show(df)
