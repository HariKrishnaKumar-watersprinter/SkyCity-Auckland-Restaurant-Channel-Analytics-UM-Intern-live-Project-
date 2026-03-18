import pandas as pd

def diversification_score(row):

    shares = [
        row["InStoreShare"],
        row["UE_share"],
        row["DD_share"],
        row["SD_share"]
    ]

    return 1 - max(shares)


def create_kpis(df):

    df["AggregatorDependence"] = df["UE_share"] + df["DD_share"]
        

    df["DiversificationScore"] = df.apply(diversification_score, axis=1)

    df["InStoreReliance"] = df["InStoreOrders"] / df["MonthlyOrders"]

    return df

