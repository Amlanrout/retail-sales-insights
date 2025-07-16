import pandas as pd

def calculate_kpis(df):
    print("\n📈 Calculating KPIs...")

    # Total KPIs
    total_revenue = df['revenue'].sum()
    total_profit = df['profit'].sum()
    total_volume = df['sales_volume'].sum()

    print(f"\n💰 Total Revenue: ₹{total_revenue:,.2f}")
    print(f"📦 Total Sales Volume: {total_volume:,} units")
    print(f"🏦 Total Profit: ₹{total_profit:,.2f}")

    # Brand-wise performance
    brand_perf = df.groupby('brand').agg({
        'revenue': 'sum',
        'profit': 'sum',
        'sales_volume': 'sum'
    }).sort_values(by='revenue', ascending=False)

    # Region-wise performance
    region_perf = df.groupby('region').agg({
        'revenue': 'sum',
        'profit': 'sum',
        'sales_volume': 'sum'
    }).sort_values(by='revenue', ascending=False)

    # Monthly revenue and profit trend
    df['month'] = df['date'].dt.to_period('M')
    monthly_trend = df.groupby('month').agg({
        'revenue': 'sum',
        'profit': 'sum'
    }).reset_index()

    return {
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'total_volume': total_volume,
        'brand_perf': brand_perf,
        'region_perf': region_perf,
        'monthly_trend': monthly_trend
    }
