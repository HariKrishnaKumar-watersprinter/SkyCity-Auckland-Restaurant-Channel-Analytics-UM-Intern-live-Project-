import pandas as pd
from src.data_loader import df
def channel_volume(df):

    return pd.DataFrame({
        "Channel": ["InStore", "UberEats", "DoorDash", "SelfDelivery"],
        "Orders": [
            df["InStoreOrders"].sum(),
            df["UberEatsOrders"].sum(),
            df["DoorDashOrders"].sum(),
            df["SelfDeliveryOrders"].sum()
        ]
    })

def delivery_instore(df):
    delivery=df['DoorDashOrders'].sum()+df['UberEatsOrders'].sum()+df['SelfDeliveryOrders'].sum()
    instore=df['InStoreOrders'].sum()
    comp_df=pd.DataFrame({
        "Channel": ["Delivery", "In-Store"],
        "Orders": [delivery, instore]
    })
    return comp_df
def market_share(df):
    
    df["ShareSum"] = (
    df["InStoreShare"] +
    df["UE_share"] +
    df["DD_share"] +
    df["SD_share"])
    Totalshare=df["ShareSum"].sum()

    share_df = pd.DataFrame({
        "Channel": ["InStore", "UberEats", "DoorDash", "SelfDelivery"],
        "share": [
            df["InStoreShare"].sum()/Totalshare*100,
            df["UE_share"].sum()/Totalshare*100,
            df["DD_share"].sum()/Totalshare*100,
            df["SD_share"].sum()/Totalshare*100
        ]
    })
    return share_df
def subregion_channel_analysis(df):

    return df.groupby("Subregion")[
        [
            "InStoreOrders",
            "UberEatsOrders",
            "DoorDashOrders",
            "SelfDeliveryOrders"
        ]
    ].sum()


def cuisine_channel_mix(df):

    cuisine_data = df.groupby("CuisineType")[
        [
            "InStoreOrders",
            "UberEatsOrders",
            "DoorDashOrders",
            "SelfDeliveryOrders"
        ]
    ].sum().reset_index()

    segment_data = df.groupby("Segment")[
        [
            "InStoreOrders",
            "UberEatsOrders",
            "DoorDashOrders",
            "SelfDeliveryOrders"
        ]
    ].sum().reset_index()

    return cuisine_data, segment_data
def profit_analysis(df):
    profit_data = {
        "Channel": [
            "InStore",
            "UberEats",
            "DoorDash",
            "SelfDelivery"
        ],
        "NetProfit": [
            df["InStoreNetProfit"].sum(),
            df["UberEatsNetProfit"].sum(),
            df["DoorDashNetProfit"].sum(),
            df["SelfDeliveryNetProfit"].sum()
        ]
    }
    return pd.DataFrame(profit_data)