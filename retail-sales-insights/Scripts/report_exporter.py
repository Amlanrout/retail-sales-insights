import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def export_kpis_to_excel(results, output_path='reports/kpi_report.xlsx'):
    with pd.ExcelWriter(output_path) as writer:
        results['brand_perf'].to_excel(writer, sheet_name='Brand Performance')
        results['region_perf'].to_excel(writer, sheet_name='Region Performance')
        results['monthly_trend'].to_excel(writer, sheet_name='Monthly Trend')
    print(f"✅ KPI tables exported to: {output_path}")

def save_chart(fig, filename):
    output_file = os.path.join('reports', filename)
    fig.savefig(output_file, bbox_inches='tight')
    print(f"🖼️ Chart saved as: {output_file}")

def export_charts(df, results):
    sns.set(style="whitegrid")

    # 1. Monthly Revenue & Profit
    fig1 = plt.figure(figsize=(10, 5))
    monthly = results['monthly_trend']
    monthly['month'] = monthly['month'].astype(str)
    sns.lineplot(x='month', y='revenue', data=monthly, label='Revenue')
    sns.lineplot(x='month', y='profit', data=monthly, label='Profit')
    plt.title('Monthly Revenue and Profit Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_chart(fig1, 'monthly_trend.png')
    plt.close(fig1)

    # 2. Brand-wise Revenue
    fig2 = plt.figure(figsize=(8, 5))
    brand_df = df.groupby('brand')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
    sns.barplot(x='revenue', y='brand', data=brand_df, palette='Blues_d')
    plt.title('Brand-wise Revenue')
    plt.tight_layout()
    save_chart(fig2, 'brand_revenue.png')
    plt.close(fig2)

    # 3. Region-wise Sales Volume
    fig3 = plt.figure(figsize=(8, 5))
    region_df = df.groupby('region')['sales_volume'].sum().reset_index()
    sns.barplot(x='sales_volume', y='region', data=region_df, palette='Greens')
    plt.title('Region-wise Sales Volume')
    plt.tight_layout()
    save_chart(fig3, 'region_sales.png')
    plt.close(fig3)

    # 4. Discount vs Profit
    fig4 = plt.figure(figsize=(8, 5))
    sns.scatterplot(x='discount', y='profit', data=df, hue='brand')
    plt.title('Discount vs Profit by Brand')
    plt.tight_layout()
    save_chart(fig4, 'discount_vs_profit.png')
    plt.close(fig4)
