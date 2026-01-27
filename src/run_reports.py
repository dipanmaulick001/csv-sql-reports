import sqlite3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output"
REPORTS_DIR = OUTPUT_DIR / "reports"
SQL_FILE = ROOT / "sql" / "reports.sql"


def parse_sql_file(sql_path: Path) -> dict[str, str]:
    """
    Parses sql/reports.sql into named queries using:
    -- name: query_name
    <SQL query...>;
    """
    text = sql_path.read_text(encoding="utf-8")

    blocks = text.split("-- name:")
    queries = {}

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        name = lines[0].strip()
        query = "\n".join(lines[1:]).strip()

        # ensure it ends with semicolon
        if not query.endswith(";"):
            query += ";"

        queries[name] = query

    return queries


def main():
    db_path = OUTPUT_DIR / "sales.db"
    REPORTS_DIR.mkdir(exist_ok=True)

    queries = parse_sql_file(SQL_FILE)

    conn = sqlite3.connect(db_path)

    for name, query in queries.items():
        df = pd.read_sql_query(query, conn)
        out_file = REPORTS_DIR / f"{name}.csv"
        df.to_csv(out_file, index=False)
        print(f"Report generated: {out_file}")

    conn.close()


if __name__ == "__main__":
    main()
