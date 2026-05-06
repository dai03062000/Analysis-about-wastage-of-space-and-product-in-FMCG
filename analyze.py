import pandas as pd

df = pd.read_csv("fmcg_inventory.csv")

# overall summary
print("=== OVERALL ===")
print(df["status"].value_counts())
print(f"Total units: {df['stock_units'].sum():,}")

# units by status
print("\n=== UNITS BY STATUS ===")
print(df.groupby("status")["stock_units"].sum().sort_values(ascending=False))

# dead stock by category
print("\n=== DEAD STOCK BY CATEGORY ===")
dead = df[df["status"] == "Dead stock"]
print(dead.groupby("name")["stock_units"].sum().sort_values(ascending=False))

# space wasted
total_units = df["stock_units"].sum()
dead_units = df[df["status"] == "Dead stock"]["stock_units"].sum()
slow_units = df[df["status"] == "Slow moving"]["stock_units"].sum()
wasted = dead_units + slow_units

print(f"\n=== SPACE WASTE ===")
print(f"Wasted units (dead + slow): {wasted:,}")
print(f"Wasted percentage: {wasted/total_units*100:.1f}%")
