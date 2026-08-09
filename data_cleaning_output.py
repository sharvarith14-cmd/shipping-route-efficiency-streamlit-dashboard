============================================================
STARTING DATA CLEANING PROCESS
============================================================

[STEP 1] Loading data...
✅ Data loaded successfully!
   Total rows: 40
   Total columns: 18

[STEP 2] Inspecting data...
First 5 rows:
   Row ID  Order ID    Order Date   Ship Date  ...

[STEP 3] Checking missing values...
✅ No missing values!

[STEP 4] Standardizing date formats...
✅ Dates converted successfully!

[STEP 5] Calculating shipping lead time...
✅ Lead time calculated!

Lead time statistics:
   count    40.000000
   mean      4.925000
   std       4.207895
   min       1.000000
   max      14.000000

[STEP 6] Validating records...
✅ No negative lead times found!
✅ No duplicates found!

============================================================
CLEANING COMPLETED!
============================================================

📊 Final Dataset:
   Rows: 40
   Columns: 19
   Average Lead Time: 4.93 days
   Min Lead Time: 1 days
   Max Lead Time: 14 days

[STEP 8] Saving cleaned data...
✅ Cleaned data saved as: cleaned_shipping_data.csv

============================================================
READY FOR ANALYSIS!
============================================================