# ========================================
# NASSAU CANDY - ROUTE ANALYSIS SCRIPT
# ========================================

import pandas as pd
import numpy as np

print("=" * 70)
print("STARTING ROUTE EFFICIENCY ANALYSIS")
print("=" * 70)

# ========== STEP 1: LOAD CLEANED DATA ==========
print("\n[STEP 1] Loading cleaned data...")
df = pd.read_csv('cleaned_shipping_data.csv')
print(f"✅ Data loaded! Total records: {len(df)}")

# ========== STEP 2: CREATE ROUTES ==========
print("\n[STEP 2] Creating route definitions...")
# Route = Division → State/Province

df['Route'] = df['Division'] + ' → ' + df['State/Province']

print(f"✅ Routes created! Total unique routes: {df['Route'].nunique()}")

# ========== STEP 3: ROUTE PERFORMANCE ANALYSIS ==========
print("\n[STEP 3] Calculating route performance metrics...")

route_performance = df.groupby('Route').agg({
    'Order ID': 'count',  
    'Shipping Lead Time (Days)': ['mean', 'std', 'min', 'max'],  
    'Sales': 'sum'
}).round(2)

# Rename columns for clarity
route_performance.columns = ['Total Shipments', 'Avg Lead Time', 'Lead Time Std Dev', 
                              'Min Lead Time', 'Max Lead Time', 'Total Sales']

# Sort by average lead time (fastest first)
route_performance = route_performance.sort_values('Avg Lead Time')

print("✅ Route metrics calculated!")

# ========== STEP 4: TOP 10 MOST EFFICIENT ROUTES ==========
print("\n" + "=" * 70)
print("🏆 TOP 10 MOST EFFICIENT ROUTES (FASTEST)")
print("=" * 70)

top_10 = route_performance.head(10)
print(top_10)

# Save to CSV
top_10.to_csv('top_10_efficient_routes.csv')
print("\n✅ Saved as: top_10_efficient_routes.csv")

# ========== STEP 5: BOTTOM 10 LEAST EFFICIENT ROUTES ==========
print("\n" + "=" * 70)
print("⚠️  BOTTOM 10 LEAST EFFICIENT ROUTES (SLOWEST)")
print("=" * 70)

bottom_10 = route_performance.tail(10)
print(bottom_10)

# Save to CSV
bottom_10.to_csv('bottom_10_inefficient_routes.csv')
print("\n✅ Saved as: bottom_10_inefficient_routes.csv")

# ========== STEP 6: SHIP MODE ANALYSIS ==========
print("\n" + "=" * 70)
print("📦 SHIPPING MODE PERFORMANCE")
print("=" * 70)

ship_mode_analysis = df.groupby('Ship Mode').agg({
    'Shipping Lead Time (Days)': ['mean', 'std', 'min', 'max'],
    'Order ID': 'count',
    'Sales': 'sum'
}).round(2)

ship_mode_analysis.columns = ['Avg Lead Time', 'Std Dev', 'Min', 'Max', 'Total Orders', 'Total Sales']
ship_mode_analysis = ship_mode_analysis.sort_values('Avg Lead Time')

print(ship_mode_analysis)

# Save to CSV
ship_mode_analysis.to_csv('ship_mode_analysis.csv')
print("\n✅ Saved as: ship_mode_analysis.csv")

# ========== STEP 7: REGIONAL ANALYSIS ==========
print("\n" + "=" * 70)
print("🗺️  REGIONAL BOTTLENECK ANALYSIS")
print("=" * 70)

region_analysis = df.groupby('Region').agg({
    'Shipping Lead Time (Days)': ['mean', 'std'],
    'Order ID': 'count',
    'Sales': 'sum'
}).round(2)

region_analysis.columns = ['Avg Lead Time', 'Std Dev', 'Order Count', 'Total Sales']
region_analysis = region_analysis.sort_values('Avg Lead Time', ascending=False)

print(region_analysis)

# Save to CSV
region_analysis.to_csv('region_analysis.csv')
print("\n✅ Saved as: region_analysis.csv")

# ========== STEP 8: STATE-LEVEL ANALYSIS ==========
print("\n" + "=" * 70)
print("📍 STATE-LEVEL PERFORMANCE ANALYSIS")
print("=" * 70)

state_analysis = df.groupby('State/Province').agg({
    'Shipping Lead Time (Days)': ['mean', 'std'],
    'Order ID': 'count',
    'Sales': 'sum'
}).round(2)

state_analysis.columns = ['Avg Lead Time', 'Std Dev', 'Order Count', 'Total Sales']
state_analysis = state_analysis.sort_values('Avg Lead Time', ascending=False)

print("\nTop 10 States by Lead Time (Slowest):")
print(state_analysis.head(10))

print("\nTop 10 States by Lead Time (Fastest):")
print(state_analysis.tail(10))

# Save to CSV
state_analysis.to_csv('state_analysis.csv')
print("\n✅ Saved as: state_analysis.csv")

# ========== STEP 9: DIVISION ANALYSIS ==========
print("\n" + "=" * 70)
print("🍬 PRODUCT DIVISION PERFORMANCE")
print("=" * 70)

division_analysis = df.groupby('Division').agg({
    'Shipping Lead Time (Days)': ['mean', 'std'],
    'Order ID': 'count',
    'Sales': 'sum'
}).round(2)

division_analysis.columns = ['Avg Lead Time', 'Std Dev', 'Order Count', 'Total Sales']
division_analysis = division_analysis.sort_values('Avg Lead Time')

print(division_analysis)

# Save to CSV
division_analysis.to_csv('division_analysis.csv')
print("\n✅ Saved as: division_analysis.csv")

# ========== STEP 10: KEY INSIGHTS ==========
print("\n" + "=" * 70)
print("💡 KEY INSIGHTS & KPIs")
print("=" * 70)

total_orders = len(df)
avg_lead_time = df['Shipping Lead Time (Days)'].mean()
median_lead_time = df['Shipping Lead Time (Days)'].median()
std_lead_time = df['Shipping Lead Time (Days)'].std()

# Delayed orders (over 7 days threshold)
delayed_threshold = 7
delayed_orders = (df['Shipping Lead Time (Days)'] > delayed_threshold).sum()
delayed_pct = (delayed_orders / total_orders) * 100

print(f"\n📊 Overall Metrics:")
print(f"   • Total Orders: {total_orders}")
print(f"   • Average Lead Time: {avg_lead_time:.2f} days")
print(f"   • Median Lead Time: {median_lead_time:.2f} days")
print(f"   • Std Deviation: {std_lead_time:.2f} days")

print(f"\n⚠️  Performance at {delayed_threshold}-day Threshold:")
print(f"   • Delayed Orders: {delayed_orders}")
print(f"   • Delay Percentage: {delayed_pct:.2f}%")

print(f"\n🚚 Shipping Modes:")
for mode in df['Ship Mode'].unique():
    mode_data = df[df['Ship Mode'] == mode]
    mode_avg = mode_data['Shipping Lead Time (Days)'].mean()
    mode_count = len(mode_data)
    print(f"   • {mode}: {mode_avg:.2f} days avg ({mode_count} orders)")

print(f"\n🗺️  Regions:")
for region in df['Region'].unique():
    region_data = df[df['Region'] == region]
    region_avg = region_data['Shipping Lead Time (Days)'].mean()
    region_count = len(region_data)
    print(f"   • {region}: {region_avg:.2f} days avg ({region_count} orders)")

# ========== STEP 11: SUMMARY REPORT ==========
print("\n" + "=" * 70)
print("✅ ANALYSIS COMPLETE!")
print("=" * 70)

print("\n📁 Generated Files:")
print("   1. route_performance.csv - All routes ranked by efficiency")
print("   2. top_10_efficient_routes.csv - Fastest 10 routes")
print("   3. bottom_10_inefficient_routes.csv - Slowest 10 routes")
print("   4. ship_mode_analysis.csv - Performance by shipping method")
print("   5. region_analysis.csv - Performance by region")
print("   6. state_analysis.csv - Performance by state")
print("   7. division_analysis.csv - Performance by product division")

print("\n🎯 Next Step: Run Streamlit dashboard with this analyzed data!")
print("   Command: streamlit run app.py")

print("\n" + "=" * 70)

# Save all route performance
route_performance.to_csv('route_performance.csv')
print("\n✅ Saved as: route_performance.csv")