import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("online_retail.csv").dropna(subset=["CustomerID", "InvoiceDate"])
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df = df.dropna(subset=["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
snapshot = df["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm = df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot - x.max()).days),
    Frequency=("InvoiceDate", "nunique"),
    Monetary=("Revenue", "sum"))
if len(rfm) < 2:
    raise ValueError("Need at least two customers.")
scaled = StandardScaler().fit_transform(rfm)
k = min(4, len(rfm))
rfm["Segment"] = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(scaled)
print(rfm.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().round(2))
print(rfm.head())