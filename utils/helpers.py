import streamlit as st
def advanced_insights(df):

    insights = []

    top_channel = df[
        [
            "InStoreOrders",
            "UberEatsOrders",
            "DoorDashOrders",
            "SelfDeliveryOrders"
        ]
    ].sum().idxmax()

    insights.append(f"{top_channel} is the dominant ordering channel.")
    top_cuisine = df.groupby("CuisineType")["MonthlyOrders"].sum().idxmax()

    insights.append(f"{top_cuisine} is the highest demand cuisine.")
    risky = (df["UE_share"] + df["DD_share"] >= 0.70).sum()

    insights.append(
        f"{risky} restaurants rely heavily on third-party aggregators."
    )

    best_region = df.groupby(
        "Subregion"
    )["MonthlyOrders"].sum().idxmax()

    insights.append(
        f"{best_region} has the highest order demand."
    )

    return insights
