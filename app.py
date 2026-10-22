
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

st.title("🛍️ Online Retail Customer Segmentation")
st.write("Analyze customer purchasing behavior using RFM and K-Means.")

uploaded_file = st.file_uploader(
    "Upload online_retail.csv",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    required = ["CustomerID", "InvoiceDate", "Quantity", "UnitPrice"]
    missing = [col for col in required if col not in df.columns]

    if missing:
        st.error(f"Missing columns: {', '.join(missing)}")
    else:
        df = df.dropna(
            subset=["CustomerID", "InvoiceDate"]
        )
        df = df[
            (df["Quantity"] > 0) &
            (df["UnitPrice"] > 0)
        ].copy()

        df["InvoiceDate"] = pd.to_datetime(
            df["InvoiceDate"], errors="coerce"
        )
        df = df.dropna(subset=["InvoiceDate"])
        df["Revenue"] = df["Quantity"] * df["UnitPrice"]

        if df.empty:
            st.error("No valid records found in the CSV.")
        else:
            snapshot = df["InvoiceDate"].max() + pd.Timedelta(days=1)

            rfm = df.groupby("CustomerID").agg(
                Recency=("InvoiceDate",
                         lambda x: (snapshot - x.max()).days),
                Frequency=("InvoiceDate", "nunique"),
                Monetary=("Revenue", "sum")
            )

            if len(rfm) < 2:
                st.error("At least two customers are required.")
            else:
                scaled = StandardScaler().fit_transform(rfm)
                k = min(4, len(rfm))

                rfm["Segment"] = KMeans(
                    n_clusters=k,
                    random_state=42,
                    n_init=10
                ).fit_predict(scaled)

                c1, c2, c3 = st.columns(3)
                c1.metric("Total Customers", len(rfm))
                c2.metric("Total Segments", k)
                c3.metric("Total Revenue", f"{rfm['Monetary'].sum():,.2f}")

                st.subheader("Customer Segment Summary")
                summary = rfm.groupby("Segment")[
                    ["Recency", "Frequency", "Monetary"]
                ].mean().round(2)
                st.dataframe(summary, use_container_width=True)

                st.subheader("Customer Segments")
                st.bar_chart(summary["Monetary"])

                st.subheader("Customer Details")
                st.dataframe(rfm.reset_index(), use_container_width=True)

                st.download_button(
                    "Download Segmented Customers CSV",
                    data=rfm.reset_index().to_csv(index=False),
                    file_name="customer_segments.csv",
                    mime="text/csv"
                )
else:
    st.info("Upload your online_retail.csv file to start analysis.")
