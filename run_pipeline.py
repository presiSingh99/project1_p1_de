"""Run the full local ETL pipeline.

This script orchestrates each pipeline stage in the correct order:
1. Ingest raw data
2. Transform raw data
3. Load processed data into DuckDB
4. Query the DuckDB database

Run it from the project root with:
    python run_pipeline.py
"""

from pathlib import Path
import subprocess
import sys

# Each tuple contains a friendly stage name and the script that should run.
# Keeping the steps in a list makes the pipeline order easy to read and update.
PIPELINE_STAGES = [
    ("Ingest raw data", Path("src/01_ingest.py")),
    ("Transform data", Path("src/02_transform.py")),
    ("Load data into DuckDB", Path("src/03_load_duckdb.py")),
    ("Query DuckDB database", Path("src/04_query.py")),
]


def run_stage(stage_number: int, total_stages: int, stage_name: str, script_path: Path) -> None:
    """Run one pipeline script and stop if it fails."""
    print(f"\n▶️  Stage {stage_number}/{total_stages}: {stage_name}", flush=True)
    print(f"   Running: python {script_path}", flush=True)

    # Use the same Python interpreter that launched this orchestrator.
    # check=True tells Python to raise an error if the script exits with failure.
    subprocess.run([sys.executable, str(script_path)], check=True)

    print(f"✅ Finished stage {stage_number}/{total_stages}: {stage_name}", flush=True)


def main() -> None:
    """Run all pipeline stages in order."""
    total_stages = len(PIPELINE_STAGES)

    print("🚀 Starting local ETL pipeline", flush=True)

    for stage_number, (stage_name, script_path) in enumerate(PIPELINE_STAGES, start=1):
        try:
            run_stage(stage_number, total_stages, stage_name, script_path)
        except subprocess.CalledProcessError as error:
            # If a stage fails, stop the pipeline immediately so later steps do not
            # run with missing or incomplete data.
            print(f"\n❌ Pipeline stopped: {stage_name} failed.", flush=True)
            print(f"   Exit code: {error.returncode}", flush=True)
            raise SystemExit(error.returncode) from error

    print("\n🎉 Pipeline completed successfully", flush=True)


if __name__ == "__main__":
    main()
