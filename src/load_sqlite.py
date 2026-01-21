import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"


def load_into_sqlite(clean_csv: Path, db_path: Path) -> None:
    # read cleaned csv
    df = pd.read_csv(clean_csv)

    # connect/create sqlite db
    conn = sqlite3.connect(db_path)

    # write dataframe to sqlite table
    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.close()


def main():
    clean_csv = OUTPUT_DIR / "cleaned_sales.csv"
    db_path = OUTPUT_DIR / "sales.db"

    load_into_sqlite(clean_csv, db_path)
    print(f" SQLite DB created at: {db_path}")


if __name__ == "__main__":
    main()
