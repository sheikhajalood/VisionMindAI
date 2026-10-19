
from pathlib import Path
import pandas as pd

# Locate the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Find the product summary created by sales_analytics.py
SUMMARY_FILE = (
    PROJECT_DIR / "data" / "processed" / "product_summary.csv"
)


def generate_insights():
    # Check whether the sales report exists
    if not SUMMARY_FILE.exists():
        raise FileNotFoundError(
            "Product summary not found. "
            "Run sales_analytics.py first."
        )

    # Read the product summary
    df = pd.read_csv(SUMMARY_FILE, index_col="product")

    # Find the product with the highest revenue
    top_product = df["revenue"].idxmax()
    top_revenue = df.loc[top_product, "revenue"]
    top_units = df.loc[top_product, "units_sold"]

    # Print business insights
    print("\n===== VISIONMIND AI BUSINESS INSIGHTS =====")

    print(
        f"\n1. Highest-revenue product: {top_product}"
    )
    print(f"   Revenue: Rs. {top_revenue:,.2f}")
    print(f"   Units sold: {int(top_units)}")

    print("\n2. Business suggestion:")
    print(
        f"   Review the stock levels of {top_product} "
        "before making replenishment decisions."
    )

    print(
        "\nNote: This suggestion is based on sales data only. "
        "Actual stock and demand should be checked."
    )


if __name__ == "__main__":
    generate_insights()
