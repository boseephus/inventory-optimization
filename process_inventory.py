import pandas as pd

# --- 1. LOAD DATA ---
# Load the raw, messy data
inv_df = pd.read_csv('data/inventory_data.csv')
sales_df = pd.read_csv('data/sales_data.csv')

# --- 2. CLEAN DATA ---
# Standardize column names and data for reliable merging
inv_df.columns = inv_df.columns.str.lower()
sales_df.columns = sales_df.columns.str.lower()

inv_df['sku'] = inv_df['sku'].str.strip()
sales_df['sku_sold'] = sales_df['sku_sold'].str.strip().str.lower()
inv_df['sku'] = inv_df['sku'].str.lower() # Standardize SKU case

# --- 3. MERGE & ENRICH DATA ---
# Combine the two data sources to get a complete picture
df = pd.merge(inv_df, sales_df, left_on='sku', right_on='sku_sold', how='left')

# Calculate the total value of inventory on hand for each item
df['inventory_value'] = df['quantity_on_hand'] * df['unit_cost']

# Calculate the cost of goods sold for each transaction
df['cogs_per_transaction'] = df['quantity_sold'] * df['unit_cost']

# --- 4. AGGREGATE & ANALYZE ---
# Create a summary DataFrame for the dashboard
dashboard_df = inv_df.copy()

# Calculate total sales per SKU
total_sales = df.groupby('sku')['quantity_sold'].sum()
dashboard_df = dashboard_df.merge(total_sales.rename('total_units_sold'), on='sku', how='left')
dashboard_df['total_units_sold'] = dashboard_df['total_units_sold'].fillna(0)

# Identify overstock (e.g., items with zero sales)
dashboard_df['inventory_status'] = 'Healthy'
dashboard_df.loc[dashboard_df['total_units_sold'] == 0, 'inventory_status'] = 'Overstock Risk'

# Calculate total value of inventory on hand
dashboard_df['inventory_value'] = dashboard_df['quantity_on_hand'] * dashboard_df['unit_cost']


# --- 5. EXPORT TO EXCEL ---
# Create the final Excel file that will be used for the dashboard
# This cleanly separates the Python "engine" from the Excel "user interface"
with pd.ExcelWriter('Inventory_Dashboard_Data.xlsx') as writer:
    dashboard_df.to_excel(writer, sheet_name='Dashboard_Data', index=False)
    df.to_excel(writer, sheet_name='Combined_Raw_Data', index=False)

print("Processing complete. 'Inventory_Dashboard_Data.xlsx' has been created.")
