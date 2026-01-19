import random
import csv
from datetime import datetime, timedelta
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

#fake dataset
CATEGORIES = ["Electronics", "Grocery", "Fashion", "Books"]
CITIES = ["Kolkata", "Delhi", "Mumbai", "Bangalore"]

PRODUCTS = {
    "Electronics": ["Mouse", "Keyboard", "Headphones", "USB Cable"],
    "Grocery": ["Rice", "Tea", "Coffee", "Biscuits"],
    "Fashion": ["T-Shirt", "Jeans", "Shoes", "Jacket"],
    "Books": ["Novel", "Notebook", "Textbook", "Comics"],
}


def random_date(days_back: int = 30) -> str:
    start = datetime.now() - timedelta(days=days_back)
    dt = start + timedelta(days=random.randint(0, days_back))
    return dt.strftime("%Y-%m-%d")


def maybe_blank(value, prob: float = 0.07):
    
    return "" if random.random() < prob else value


def maybe_duplicate(existing_rows: list, prob: float = 0.06):
    if existing_rows and random.random() < prob:
        return random.choice(existing_rows)
    return None


def main():
    
    DATA_DIR.mkdir(exist_ok=True)

    output_file = DATA_DIR / "raw_sales.csv"
    rows = []
    order_id = 1000

    # gen 300 records
    for _ in range(300):
        # add duplicate row
        dup = maybe_duplicate(rows)
        if dup:
            rows.append(dup)
            continue

        category = random.choice(CATEGORIES)
        product = random.choice(PRODUCTS[category])
        city = random.choice(CITIES)

        quantity = random.randint(1, 5)
        unit_price = random.randint(100, 5000)

        # Create row and inject few missing vals
        row = {
            "order_id": maybe_blank(order_id),
            "date": maybe_blank(random_date()),
            "category": maybe_blank(category),
            "product": maybe_blank(product),
            "city": maybe_blank(city),
            "quantity": maybe_blank(quantity),
            "unit_price": maybe_blank(unit_price),
        }

        # Intent. dirty values 
        if random.random() < 0.05:
            row["unit_price"] = "NA"
        if random.random() < 0.05:
            row["quantity"] = "two"

        rows.append(row)
        order_id += 1

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f" Generated dataset: {output_file}")
    print(f"Rows generated: {len(rows)}")


if __name__ == "__main__":
    main()
