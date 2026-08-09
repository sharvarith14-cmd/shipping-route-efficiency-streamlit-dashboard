# ========================================
# NASSAU CANDY - DATA CLEANING SCRIPT
# ========================================

# Import libraries
import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 60)
print("STARTING DATA CLEANING PROCESS")
print("=" * 60)

# ========== STEP 1: LOAD DATA ==========
print("\n[STEP 1] Loading data...")
df = pd.read_csv('shipping_data.csv')  # ← FILE NAME SAME HONA CHAHIYE

print(f"✅ Data loaded successfully!")
print(f"   Total rows: {len(df)}")
print(f"   Total columns: {len(df.columns)}")

# ========== STEP 2: INITIAL INSPECTION ==========
print("\n[STEP 2] Inspecting data...")
print("\nFirst 5 rows:")
print(df.head())

print("\n\nColumn names:")
print(df.columns.tolist())

print("\n\nData types:")
print(df.dtypes)

# ========== STEP 3: CHECK MISSING VALUES ==========
print("\n[STEP 3] Checking missing values...")
missing = df.isnull().sum()
if missing.sum() > 0:
    print("Missing values found:")
    print(missing[missing > 0])
else:
    print("✅ No missing values!")

# ========== STEP 4: STANDARDIZE DATES ==========
print("\n[STEP 4] Standardizing date formats...")

# Convert to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

print("✅ Dates converted successfully!")

# ========== STEP 5: CALCULATE LEAD TIME ==========
print("\n[STEP 5] Calculating shipping lead time...")

df['Shipping Lead Time (Days)'] = (df['Ship Date'] - df['Order Date']).dt.days

print("✅ Lead time calculated!")
print(f"\nLead time statistics:")
print(df['Shipping Lead Time (Days)'].describe())

# ========== STEP 6: REMOVE INVALID RECORDS ==========
print("\n[STEP 6] Validating records...")

# Check for negative lead times
negative_count = (df['Shipping Lead Time (Days)'] < 0).sum()
if negative_count > 0:
    print(f"⚠️  Found {negative_count} records with negative lead time - REMOVING")
    df = df[df['Shipping Lead Time (Days)'] >= 0]
else:
    print("✅ No negative lead times found!")

# Remove duplicates
initial_rows = len(df)
df = df.drop_duplicates(subset=['Order ID'], keep='first')
duplicates_removed = initial_rows - len(df)

if duplicates_removed > 0:
    print(f"⚠️  Removed {duplicates_removed} duplicate orders")
else:
    print("✅ No duplicates found!")

# ========== STEP 7: FINAL SUMMARY ==========
print("\n" + "=" * 60)
print("CLEANING COMPLETED!")
print("=" * 60)

print(f"\n📊 Final Dataset:")
print(f"   Rows: {len(df)}")
print(f"   Columns: {len(df.columns)}")
print(f"   Average Lead Time: {df['Shipping Lead Time (Days)'].mean():.2f} days")
print(f"   Min Lead Time: {df['Shipping Lead Time (Days)'].min()} days")
print(f"   Max Lead Time: {df['Shipping Lead Time (Days)'].max()} days")

# ========== STEP 8: SAVE CLEANED DATA ==========
print("\n[STEP 8] Saving cleaned data...")

df.to_csv('cleaned_shipping_data.csv', index=False)

print("✅ Cleaned data saved as: cleaned_shipping_data.csv")
print("\n" + "=" * 60)
print("READY FOR ANALYSIS!")
print("=" * 60)