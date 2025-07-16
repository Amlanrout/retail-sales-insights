import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_trend(monthly_df):
    monthly_df['month'] = monthly_df['month'].astype(str)

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='month', y='revenue', data=monthly_df, label='Revenue')
    sns.lineplot(x='month', y='profit', data=monthly_df, label='Profit')
    plt.title('📈 Monthly Revenue and Profit Trend')
    plt.xlabel('Month')
    plt.ylabel('Amount (₹)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.show()

def plot_brand_revenue(df):
    brand_df = df.groupby('brand')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)

    plt.figure(figsize=(8, 5))
    sns.barplot(x='revenue', y='brand', data=brand_df, palette='Blues_d')
    plt.title('🏷️ Brand-wise Revenue')
    plt.xlabel('Revenue (₹)')
    plt.ylabel('Brand')
    plt.tight_layout()
    plt.show()

def plot_region_sales(df):
    region_df = df.groupby('region')['sales_volume'].sum().reset_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(x='sales_volume', y='region', data=region_df, palette='Greens')
    plt.title('🌍 Region-wise Sales Volume')
    plt.xlabel('Units Sold')
    plt.ylabel('Region')
    plt.tight_layout()
    plt.show()

def plot_discount_vs_profit(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='discount', y='profit', data=df, hue='brand')
    plt.title('💸 Discount vs Profit by Brand')
    plt.xlabel('Discount (₹)')
    plt.ylabel('Profit (₹)')
    plt.tight_layout()
    plt.show()
