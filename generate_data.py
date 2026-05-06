import pandas as pd
import random
from datetime import datetime, timedelta

brands = ["Vinamilk", "TH True Milk", "Nestle", "Masan", "Neptune", "Kinh Do", "Bibica", "Orion", "Sabeco", "Pepsi", "Coca-Cola", "Tan Hiep Phat"]

categories = {
    "Milk": ["Sweetened", "Unsweetened", "Condensed", "Vegan", "Low fat"],
    "Soft drink": ["Cola", "Lemon soda", "Orange soda", "Energy drink", "Green tea"],
    "Cooking oil": ["Vegetable", "Olive", "Vegan", "Sunflower"],
    "Candy": ["Chocolate", "Hard candy", "Fruit flavored", "Gummy"],
    "Instant noodle": ["Beef", "Chicken", "Vegetarian", "Spicy"]
}

sizes = ["180ml", "330ml", "500ml", "1L", "2L", "5L", "50g", "100g", "200g", "380g", "500g"]

today = datetime(2024, 5, 1)

def random_import_date(category, name):
    roll = random.random()
    if category in ["Milk", "Soft drink"]:
        if roll < 0.45:
            days_ago = random.randint(180, 500)
        elif roll < 0.60:
            days_ago = random.randint(90, 179)
        else:
            days_ago = random.randint(7, 89)
    else:
        if roll < 0.20:
            days_ago = random.randint(180, 400)
        elif roll < 0.35:
            days_ago = random.randint(90, 179)
        else:
            days_ago = random.randint(7, 89)
    return today - timedelta(days=days_ago)

rows = []
for i in range(500):
    category = random.choice(list(categories.keys()))
    product_type = random.choice(categories[category])
    brand = random.choice(brands)
    size = random.choice(sizes)
    last_import = random_import_date(category, product_type)
    days_since = (today - last_import).days
    stock = random.randint(300, 1200) if days_since > 180 else random.randint(50, 400)
    
    if days_since > 180:
        status = "Dead stock"
    elif days_since > 90:
        status = "Slow moving"
    else:
        status = "Active"
    
    rows.append({
        "brand": brand,
        "name": category,
        "type": product_type,
        "size": size,
        "stock_units": stock,
        "last_import_date": last_import.strftime("%Y-%m-%d"),
        "days_since_import": days_since,
        "status": status
    })

df = pd.DataFrame(rows)
df.to_csv("fmcg_inventory.csv", index=False)
print(df["status"].value_counts())
print(f"\nTotal units: {df['stock_units'].sum():,}")
