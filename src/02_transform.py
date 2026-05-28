"""Step 2: Transform data with Polars.

This script reads raw CSV data, performs simple transformations,
and writes a cleaned dataset to data/processed.
"""

from pathlib import Path
import polars as pl

RAW_FILE = Path("data/raw/sales_raw.csv")
PROCESSED_DIR = Path("data/processed")
PROCESSED_FILE = PROCESSED_DIR / "sales_processed.csv"


def main() -> None:
    """Run the transform step."""
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw file not found: {RAW_FILE}. Run 01_ingest.py first."
        )

    # Read raw data into a Polars DataFrame
    df = pl.read_csv(RAW_FILE)

    # Add basic transformations:
    # - amount_with_tax: adds 10% tax
    # - amount_bucket: labels order size
    transformed = df.with_columns(
        [
            (pl.col("amount") * 1.10).round(2).alias("amount_with_tax"),
            pl.when(pl.col("amount") >= 150)
            .then(pl.lit("Large"))
            .otherwise(pl.lit("Standard"))
            .alias("amount_bucket"),
        ]
    )

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    transformed.write_csv(PROCESSED_FILE)

    print(f"✅ Wrote processed data to {PROCESSED_FILE}")
    print(transformed)


if __name__ == "__main__":
    main()
