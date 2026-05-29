codex/create-local-data-pipeline-project-zmizrj
"""Step 4: Query the DuckDB sales table.

This script connects to the local DuckDB database and runs three
beginner-friendly analytics queries against the sales table.

"""Step 4: Query the DuckDB table.

This script runs simple analytics queries and prints the results.
main
"""

from pathlib import Path
import duckdb

DB_FILE = Path("db/analytics.duckdb")


def main() -> None:
codex/create-local-data-pipeline-project-zmizrj
    """Run three example sales queries and print the results."""

    """Run query examples."""
main
    if not DB_FILE.exists():
        raise FileNotFoundError(
            f"Database file not found: {DB_FILE}. Run 03_load_duckdb.py first."
        )

codex/create-local-data-pipeline-project-zmizrj
    # Connect to the DuckDB database created by 03_load_duckdb.py.
    conn = duckdb.connect(str(DB_FILE))

    # Query 1: Total sales by region.
    # SUM(amount) adds all sales amounts in each region.
    # GROUP BY region creates one result row per region.
    total_sales_by_region_sql = """
        SELECT region, ROUND(SUM(amount), 2) AS total_amount
        FROM sales
        GROUP BY region
        ORDER BY total_amount DESC
    """
    total_sales_by_region = conn.execute(total_sales_by_region_sql).fetchdf()

    # Query 2: Average order amount by customer.
    # AVG(amount) calculates the typical order size for each customer.
    # GROUP BY customer creates one result row per customer.
    average_order_by_customer_sql = """
        SELECT customer, ROUND(AVG(amount), 2) AS average_amount
        FROM sales
        GROUP BY customer
        ORDER BY average_amount DESC
    """
    average_order_by_customer = conn.execute(average_order_by_customer_sql).fetchdf()
    
    
    # Query 3: Top 3 largest sales amounts.
        # ORDER BY amount DESC sorts largest sales first.
        # LIMIT 3 keeps only the first three rows after sorting.
    	    top_3_sales_sql = """
   	        SELECT order_id, customer, region, amount, amount_with_tax
   	        FROM sales
   	        ORDER BY amount DESC
   	        LIMIT 3
      	    """
    	    top_3_sales = conn.execute(top_3_sales_sql).fetchdf()
    	
    	    conn.close()
    	
    	    print("\n✅ Total sales by region")
    	    print(total_sales_by_region)
    	
    	    print("\n✅ Average order amount by customer")
    	    print(average_order_by_customer)
    	
    	    print("\n✅ Top 3 largest sales amounts")
    	    print(top_3_sales)
    	
    	
    	if __name__ == "__main__":
    	    main()