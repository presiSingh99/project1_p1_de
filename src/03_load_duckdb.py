"""Step 3: Load transformed data into DuckDB.

This script creates a DuckDB database file and loads processed CSV
into a table named sales.
"""

from pathlib import Path
import duckdb

PROCESSED_FILE = Path("data/processed/sales_processed.csv")
DB_DIR = Path("db")
DB_FILE = DB_DIR / "analytics.duckdb"


def main() -> None:
    """Run the load step."""
    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(
            f"Processed file not found: {PROCESSED_FILE}. Run 02_transform.py first."
        )

    DB_DIR.mkdir(parents=True, exist_ok=True)

    # Connect to DuckDB (it creates the file if it does not exist)
    conn = duckdb.connect(str(DB_FILE))

    # Recreate the sales table from processed CSV for repeatable runs
    conn.execute("DROP TABLE IF EXISTS sales")
    conn.execute(
        f"""
        CREATE TABLE sales AS
        SELECT *
        FROM read_csv_auto('{PROCESSED_FILE.as_posix()}', HEADER=TRUE)
        """
    )

    row_count = conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
    conn.close()

    print(f"✅ Loaded {row_count} rows into DuckDB table: sales")
    print(f"✅ Database file: {DB_FILE}")


if __name__ == "__main__":
    main()
