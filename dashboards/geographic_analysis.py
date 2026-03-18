import streamlit as st
import pydeck as pdk

def show(df):

    st.header("Geographic Order Distribution")

    data = df.groupby("Subregion")[
        "MonthlyOrders"
    ].sum().reset_index()

    coords = {
        "CBD":[-36.8485,174.7633],
        "North Shore":[-36.8,174.75],
        "West Auckland":[-36.9,174.6],
        "South Auckland":[-37.0,174.8],
        
        
    }

    data["lat"] = data["Subregion"].map(lambda x:coords[x][0])
    data["lon"] = data["Subregion"].map(lambda x:coords[x][1])

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position="[lon,lat]",
        get_radius="MonthlyOrders",
        get_fill_color="[200,30,0,160]"
    )

    st.pydeck_chart(pdk.Deck(layers=[layer]))