import pandas as pd

# veri oku
df = pd.read_csv("../data/sales.csv")

# toplam satış kolonu oluştur
df["revenue"] = df["units"] * df["price"]

# KPI hesapla
total_revenue = df["revenue"].sum()
best_product = df.groupby("product")["revenue"].sum().idxmax()

print("Toplam Ciro:", total_revenue)
print("En iyi ürün:", best_product)
