import pandas as pd
import streamlit as st

st.set_page_config(page_title="Smart Decision Support", layout="wide")

st.title("📊 Akıllı Karar Destek Sistemi")
st.caption("KPI + Basit analiz (demo satış verisi)")

# Veri oku
df = pd.read_csv("../data/sales.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["units"] * df["price"]

# Filtreler
st.sidebar.header("Filtreler")
regions = ["All"] + sorted(df["region"].unique().tolist())
products = ["All"] + sorted(df["product"].unique().tolist())

selected_region = st.sidebar.selectbox("Bölge", regions)
selected_product = st.sidebar.selectbox("Ürün", products)

fdf = df.copy()
if selected_region != "All":
    fdf = fdf[fdf["region"] == selected_region]
if selected_product != "All":
    fdf = fdf[fdf["product"] == selected_product]


# KPI'lar
total_revenue = fdf["revenue"].sum()
total_units = fdf["units"].sum()
best_product = fdf.groupby("product")["revenue"].sum().idxmax() if len(fdf) else "-"


c1, c2, c3 = st.columns(3)
c1.metric("Toplam Ciro", f"{total_revenue:,.0f}")
c2.metric("Toplam Adet", f"{total_units:,}")
c3.metric("En iyi ürün", best_product)

st.divider()

# Aylık (bu veri günlük ama yine de örnek)
fdf["month"] = fdf["date"].dt.to_period("M").astype(str)
monthly = fdf.groupby("month")["revenue"].sum().reset_index()

st.subheader("📈 Aylık Ciro")
st.line_chart(monthly, x="month", y="revenue")

st.subheader("🧭 Bölge Bazlı Ciro")
region_rev = fdf.groupby("region")["revenue"].sum().sort_values(ascending=False)
st.bar_chart(region_rev)

st.subheader("🧾 Ham Veri")
st.dataframe(fdf)
from sklearn.linear_model import LinearRegression
import numpy as np

st.divider()
st.subheader("🔮 Basit Tahmin (Trend)")

# Günlük toplam ciro
daily = fdf.groupby("date")["revenue"].sum().reset_index().sort_values("date")

if len(daily) >= 3:
    X = np.arange(len(daily)).reshape(-1, 1)
    y = daily["revenue"].values

    model = LinearRegression()
    model.fit(X, y)

    next_day_index = np.array([[len(daily)]])
    pred_next = model.predict(next_day_index)[0]

    st.metric("Bir sonraki gün tahmini ciro", f"{pred_next:,.0f}")
else:
    st.info("Tahmin için en az 3 gün veri lazım.")

