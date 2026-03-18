import numpy as np

def detect_outliers_iqr(df, column):

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower) |
        (df[column] > upper)
    ]

    return outliers


def detect_multiple_outliers(df):

    cols = [
        "MonthlyOrders",
        "AOV",
        "DeliveryRadiusKM"
    ]

    results = {}

    for col in cols:
        results[col] = detect_outliers_iqr(df,col)

    return results