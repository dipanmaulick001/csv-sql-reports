#actual cleaning of the dataset takes place here 
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output"

def clean_sales_csv(input_csv: Path, output_csv: Path) -> None:
    df = pd.read_csv(input_csv)

    df = df.drop_duplicates()

    df = df.replace(r"^\s*$", pd.NA, regex=True)

    df["order_id"] = pd.to_numeric(df["order_id"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df["order_id"] = df["order_id"].fillna(0).astype(int)
    df["quantity"] = df["quantity"].fillna(0).astype(int)
    df["unit_price"] = df["unit_price"].fillna(0).astype(int)

    for col in ["date", "category", "product", "city"]:
        df[col] = df[col].fillna("Unknown")

    df["total_price"] = df["quantity"] * df["unit_price"]

    OUTPUT_DIR.mkdir(exist_ok=True)

    df.to_csv(output_csv, index=False)
    

def main():
        input_csv = DATA_DIR / "raw_sales.csv"
        output_csv = OUTPUT_DIR / "cleaned_sales.csv"

        clean_sales_csv(input_csv, output_csv)
        print(f" Cleaned CSV saved to: {output_csv}")


if __name__ == "__main__":
            main()







