def classify_channel_risk(row):

    agg_share = row["UE_share"] + row["DD_share"]

    if agg_share < 0.40:
        return "Balanced"

    elif agg_share > 0.40 and agg_share < 0.70 :
        return "Medium Risk"

    else:
        return "High Risk"


def apply_risk_classification(df):

    df["AggregatorDependence"] = df["UE_share"] + df["DD_share"]

    df["ChannelRiskProfile"] = df.apply(
        classify_channel_risk,
        axis=1
    )

    return df