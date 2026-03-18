from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def restaurant_clustering(df):

    features = df[
        [
            "InStoreShare",
            "UE_share",
            "DD_share",
            "SD_share",
            "MonthlyOrders"
        ]
    ]

    scaler = StandardScaler()

    X = scaler.fit_transform(features)

    model = KMeans(n_clusters=4, random_state=42)

    df["Cluster"] = model.fit_predict(X)

    return df