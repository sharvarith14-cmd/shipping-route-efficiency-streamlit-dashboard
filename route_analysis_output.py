======================================================================
STARTING ROUTE EFFICIENCY ANALYSIS
======================================================================

[STEP 1] Loading cleaned data...
✅ Data loaded! Total records: 40

[STEP 2] Creating route definitions...
✅ Routes created! Total unique routes: 20

[STEP 3] Calculating route performance metrics...
✅ Route metrics calculated!

======================================================================
🏆 TOP 10 MOST EFFICIENT ROUTES (FASTEST)
======================================================================
Route                                 Total Shipments  Avg Lead Time  ...
Chocolate → New York                          1             1.0  ...
Sugar → Texas                                 2             1.5  ...

======================================================================
⚠️  BOTTOM 10 LEAST EFFICIENT ROUTES (SLOWEST)
======================================================================
Route                                 Total Shipments  Avg Lead Time  ...
Sugar → California                            2            14.0  ...

======================================================================
📦 SHIPPING MODE PERFORMANCE
======================================================================
Ship Mode          Avg Lead Time  ...
Same Day                   1.0  ...
First Class                3.5  ...
Second Class               4.0  ...
Standard Class             8.5  ...

======================================================================
🗺️  REGIONAL BOTTLENECK ANALYSIS
======================================================================
Region      Avg Lead Time  Order Count
South             6.0          12
Central           5.0           8
West              7.5          12
East              4.0            8

💡 KEY INSIGHTS & KPIs
=======================================================================

📊 Overall Metrics:
   • Total Orders: 40
   • Average Lead Time: 4.93 days
   • Median Lead Time: 4.50 days
   • Std Deviation: 4.21 days

⚠️  Performance at 7-day Threshold:
   • Delayed Orders: 9
   • Delay Percentage: 22.50%

======================================================================
✅ ANALYSIS COMPLETE!
======================================================================

📁 Generated Files:
   1. route_performance.csv
   2. top_10_efficient_routes.csv
   3. bottom_10_inefficient_routes.csv
   4. ship_mode_analysis.csv
   5. region_analysis.csv
   6. state_analysis.csv
   7. division_analysis.csv