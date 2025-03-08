#1.1 
import pandas as pd

df = pd.read_csv("task/sales_data.csv")
df['Date'] = pd.to_datetime(df['Date']) 
df['Total_Sale'] = df['Quantity'] * df['Price'] 

category_stats = df.groupby("Category").agg(
    Total_Quantity_Sold=("Quantity", "sum"),
    Average_Price=("Price", "mean"),
    Max_Quantity_Single_Transaction=("Quantity", "max")
).reset_index()

print(category_stats)

# 1.2 Identify top-selling product in each category
top_selling_products = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_selling_products = top_selling_products.loc[top_selling_products.groupby("Category")["Quantity"].idxmax()]

print(top_selling_products)

# 1.3 Find the date with the highest total sales
best_sales_date = df.groupby("Date")["Total_Sale"].sum().idxmax()
best_sales_value = df.groupby("Date")["Total_Sale"].sum().max()

print(f"\nDate with Highest Total Sales: {best_sales_date}, Total Sales: {best_sales_value}")

#2.1
import pandas as pd

df = pd.read_csv("task/customer_orders.csv")

df['Total_Price'] = df['Quantity'] * df['Price']  

customer_order_counts = df.groupby("CustomerID")["OrderID"].count()
eligible_customers = customer_order_counts[customer_order_counts >= 20].index
filtered_customers = df[df["CustomerID"].isin(eligible_customers)]

print(filtered_customers["CustomerID"].unique())

# 2.2 Identify customers who have ordered products with an average price per unit > $120
high_avg_price_customers = df.groupby("CustomerID")["Price"].mean()
high_price_customers = high_avg_price_customers[high_avg_price_customers > 120].index
filtered_high_price_customers = df[df["CustomerID"].isin(high_price_customers)]

print(filtered_high_price_customers["CustomerID"].unique())

# 2.3. Compute total quantity and total price for each product
product_stats = df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("Total_Price", "sum")
).reset_index()

filtered_products = product_stats[product_stats["Total_Quantity"] >= 5]

print(filtered_products)

