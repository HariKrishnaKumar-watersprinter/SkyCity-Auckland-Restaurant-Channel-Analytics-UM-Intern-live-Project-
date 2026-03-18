import streamlit as st
from dashboards import overview
from dashboards import subregion_analysis
from dashboards import cuisine_analysis
from dashboards import profitability_analysis
from dashboards import dependency_risk
from dashboards import marketshare
from dashboards import diversification_dashboard
from dashboards import insights_dashboard
def show(df):

    st.header("Executive Performance Overview")

    total_orders = df["MonthlyOrders"].sum()
    Restaurant=df['RestaurantName'].nunique()
    instore = df["InStoreOrders"].sum()/total_orders*100
    uber = df["UberEatsOrders"].sum()/total_orders*100
    doordash = df["DoorDashOrders"].sum()/total_orders*100
    self_delivery = df["SelfDeliveryOrders"].sum()/total_orders*100
    avg_order_value = df["AOV"].mean()

    col1, col2, col3, col4,col5, col6 = st.columns(6)

    col1.metric("Total Orders", f"{total_orders:,}")
    col2.metric('Total Restaurant',f"{Restaurant:,}")
    col3.metric("In-Store Orders", f"{instore:.2f}%")
    col4.metric("Uber Eats Orders", f"{uber:.2f}%")
    col5.metric("DoorDash Orders", f"{doordash:.2f}%")
    col6.metric("Self Delivery Orders", f"{self_delivery:.2f}%")
    
    col7=st.columns(1)
    col7[0].metric("Average Order Value", f"${avg_order_value:.2f}")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Channel Mix Overview",
    "💼 Channel Market Share",
    "🗺️ Subregion Heatmaps",
    "🍕 Cuisine & Segment Charts",
    "🚨 Dependency Risk Panels",
    "📈 Profitability Analysis",
    "📈 Diversification Analysis",
    "💡 Insights Dashboard"
    ])

    with tab1 :
        overview.show(df)
    with tab2 :
        marketshare.show(df)
    with tab3 :
        subregion_analysis.show(df)
    with tab4 :
        cuisine_analysis.show(df)
    with tab5 :
        dependency_risk.show(df)
    with tab6 :
        profitability_analysis.show(df)
    with tab7 :
        diversification_dashboard.show(df)
    with tab8 :
        insights_dashboard.show(df)
