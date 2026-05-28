"""Step 4: Query the DuckDB table.

This script runs simple analytics queries and prints the results.
"""

from pathlib import Path
import duckdb

DB_FILE = Path("db/analytics.duckdb")


def main() -> None:
    """Run query examples."""
    if not DB_FILE.exists():
        raise FileNotFoundError(
            f"Database file not found: {DB_FILE}. Run 03_load_duckdb.py first."
        )

    conn = duckdb.connect(str(DB_FILE))

    # Query 1: total sales by region
    query_region = """
    SELECT region, ROUND(SUM(amount), 2) AS total_amount
    FROM sales
    GROUP BY region
    ORDER BY total_amount DESC
    """
    region_result = conn.execute(query_region).fetchdf()

    # Query 2: average order amount by customer
    query_customer = """
    SELECT customer, ROUND(AVG(amount), 2) AS avg_amount
    FROM sales
    GROUP BY customer
    ORDER BY avg_amount DESC
    """
    customer_result = conn.execute(query_customer).fetchdf()

 codex/create-local-data-pipeline-project-72fhv4

codex/create-local-data-pipeline-project-h19xpk
 main
    # Query 3: top 3 largest sales amounts from the sales table
    # SQL logic:
    # 1) Select columns that exist in the sales dataset.
    # 2) Sort rows by amount in descending order (largest sales first).
    # 3) Keep only the first 3 rows using LIMIT.
    query_top_sales = """
 codex/create-local-data-pipeline-project-72fhv4
SELECT order_id, customer, region, amount, amount_with_tax
FROM sales
ORDER BY amount DESC
LIMIT 3
"""
    top_sales_result = conn.execute(query_top_sales).fetchdf()


    SELECT order_id, customer, region, amount, amount_with_tax
    FROM sales
    ORDER BY amount DESC
    LIMIT 3
    """
    top_sales_result = conn.execute(query_top_sales).fetchdf()

    # Query 3: top 3 highest paid employees from the employees table
    # SQL logic:
    # 1) Select employee name and salary columns.
    # 2) Sort rows by salary in descending order (highest salaries first).
    # 3) Keep only the first 3 rows using LIMIT.
    query_top_employees = """
    SELECT employee_name, salary
    FROM employees
    ORDER BY salary DESC
    LIMIT 3
    """
    top_employees_result = conn.execute(query_top_employees).fetchdf()
main

main
    conn.close()

    print("\n✅ Total sales by region")
    print(region_result)

    print("\n✅ Average order amount by customer")
    print(customer_result)

codex/create-local-data-pipeline-project-72fhv4
    print("\n✅ Top 3 largest sales amounts")
    print(top_sales_result)


codex/create-local-data-pipeline-project-h19xpk
    print("\n✅ Top 3 largest sales amounts")
    print(top_sales_result)

    print("\n✅ Top 3 highest paid employees")
    print(top_employees_result)
main
main
if __name__ == "__main__":
    main()
