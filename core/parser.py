from pathlib import Path

import pandas as pd


def load_products(file_path):
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    data = pd.read_csv(path).fillna("")
    if "product_name" not in data.columns:
        raise ValueError("Input CSV must include a product_name column.")

    return data.to_dict(orient="records")


def save_results(rows, file_path):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8-sig")
