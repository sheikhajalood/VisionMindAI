
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Input dataset and output folder
DATA_FILE = PROJECT_DIR / "data" / "raw" / "sales.csv"
OUTPUT_DIR = PROJECT_DIR / "data" / "processed"


def analyze_sales():
    # Check if the sales dataset exists
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Sales dataset not found: {DATA_FILE}"
        )

    # Read the CSV file
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])

    # Calculate revenue for every product entry
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Overall sales metrics
    total_revenue = df["revenue"].sum()
    total_units = df["quantity"].sum()

    # Product-wise performance
    product_summary = (
        df.groupby("product")
        .agg(
            units_sold=("quantity", "sum"),
            revenue=("revenue", "sum")
        )
        .sort_values("revenue", ascending=False)
    )

    # Revenue earned each day
    daily_revenue = df.groupby("date")["revenue"].sum()

    # Print the report
    print("\n===== VISIONMIND AI SALES REPORT =====")
    print(f"Total revenue: Rs. {total_revenue:,.2f}")
    print(f"Total units sold: {total_units}")

    print("\nProduct-wise sales:")
    print(product_summary.to_string())

    print("\nDaily revenue:")
    print(daily_revenue.to_string())

    print(
        "\nHighest-revenue product:",
        product_summary["revenue"].idxmax()
    )

    # Create output folder
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Save results as CSV files
    product_summary.to_csv(
        OUTPUT_DIR / "product_summary.csv"
    )
    daily_revenue.to_csv(
        OUTPUT_DIR / "daily_revenue.csv"
    )

    # Create and save a daily revenue chart
    daily_revenue.plot(
        kind="line",
        marker="o",
        title="Daily Retail Revenue"
    )
    plt.xlabel("Date")
    plt.ylabel("Revenue (Rs.)")
    plt.xticks(rotation=30)
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "daily_revenue.png")
    plt.close()

    print(f"\nReports saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    analyze_sales()
