import pandas as pd
from src.data_loader import df
def validate_order_counts(df):

    df["CalculatedOrders"] = (
        df["InStoreOrders"] +
        df["UberEatsOrders"] +
        df["DoorDashOrders"] +
        df["SelfDeliveryOrders"]
    )

    df["OrderMismatch"] = df["CalculatedOrders"] != df["MonthlyOrders"]

    return df


def validate_channel_share(df):

    df["ShareTotal"] = (
        df["InStoreShare"] +
        df["UE_share"] +
        df["DD_share"] +
        df["SD_share"]
    )

    df["ShareMismatch"] = df["ShareTotal"].round(2) != 1.00

    return df