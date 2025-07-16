import sys
import os

# ✅ Step 1: Add the 'scripts' folder to the Python path
scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.append(scripts_dir)

# ✅ Step 2: Now import directly from the script (without scripts.)
from data_cleaning import load_and_clean_data

from kpi_analysis import calculate_kpis
from visualization import (
    plot_monthly_trend,
    plot_brand_revenue,
    plot_region_sales,
    plot_discount_vs_profit
)


# ✅ Step 3: Use the function
file_path = 'data/fmcg_sales_mock.csv'
df_cleaned = load_and_clean_data(file_path)

# ✅ Step 4: Display output
print("\n📊 Preview of cleaned data:")
print(df_cleaned.head())

print("\n📈 Summary statistics:")
print(df_cleaned.describe())

# ✅ Step 5: Run KPI Analysis
results = calculate_kpis(df_cleaned)

# ✅ Step 6: Print KPI Tables
print("\n🏷️ Brand-wise Performance:")
print(results['brand_perf'])

print("\n🌍 Region-wise Performance:")
print(results['region_perf'])

print("\n📆 Monthly Revenue & Profit Trend:")
print(results['monthly_trend'].head())

# ✅ Step 7: Visualize KPIs
plot_monthly_trend(results['monthly_trend'])
plot_brand_revenue(df_cleaned)
plot_region_sales(df_cleaned)
plot_discount_vs_profit(df_cleaned)


