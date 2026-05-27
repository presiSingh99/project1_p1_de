"""Step 1: Ingest raw data.

This script creates a small sample dataset and saves it to data/raw.
In a real project, this step would read from an API, CSV export, or database.
"""

from pathlib import Path
import pandas as pd

# Define where files should be written
RAW_DIR = Path("data/raw")
RAW_FILE = RAW_DIR / "sales_raw.csv"


def create_sample_data() -> pd.DataFrame:
    """Create a beginner-friendly sample dataset."""
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4, 5],
            "customer": ["Alice", "Bob", "Alice", "Diana", "Evan"],
            "region": ["North", "South", "North", "East", "West"],
            "amount": [120.0, 75.5, 210.0, 50.0, 180.0],
        }
    )


def main() -> None:
    """Run the ingest step."""
    # Make sure the target folder exists
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Build sample data and save as CSV
    df = create_sample_data()
    df.to_csv(RAW_FILE, index=False)

    print(f"✅ Wrote raw data to {RAW_FILE}")
    print(df.head())


if __name__ == "__main__":
    main()
