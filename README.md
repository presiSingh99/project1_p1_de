# Local ETL Pipeline (Pandas + Polars + DuckDB)

This project is a beginner-friendly local ETL pipeline:

1. **Ingest** sample data with Pandas
2. **Transform** data with Polars
3. **Load** data into DuckDB
4. **Query** data from DuckDB

## Project structure

- `data/raw` - raw CSV output from ingest step
- `data/processed` - cleaned CSV output from transform step
- `db` - DuckDB database file
- `src` - pipeline scripts

## Local setup and run instructions

### 1) Create a virtual environment

```bash
python -m venv .venv
```

### 2) Activate the virtual environment

- **macOS/Linux**
  ```bash
  source .venv/bin/activate
  ```

- **Windows (PowerShell)**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```

- **Windows (Command Prompt)**
  ```cmd
  .venv\Scripts\activate.bat
  ```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run files in order

```bash
python src/01_ingest.py
python src/02_transform.py
python src/03_load_duckdb.py
python src/04_query.py
```

## Note about Codex environment

If `duckdb` is not installed (or cannot be installed due to environment/network restrictions), the script `src/04_query.py` may fail with `ModuleNotFoundError: No module named 'duckdb'`.
