import json
import os
from pathlib import Path

from dotenv import load_dotenv

from core.generator import ListingGenerator
from core.parser import load_products, save_results
from core.seo import extract_keywords


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
INPUT_PATH = ROOT / "data" / "input.csv"
OUTPUT_PATH = ROOT / "output" / "results.csv"


def load_config():
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def run():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set OPENAI_API_KEY before running the app.")

    config = load_config()
    generator = ListingGenerator(api_key=api_key, config=config, root=ROOT)
    products = load_products(INPUT_PATH)

    results = []
    for product in products:
        title_output = generator.generate_titles(product)
        description = generator.generate_description(product)
        keywords = extract_keywords(f"{title_output}\n{description}")

        results.append(
            {
                "product_name": product.get("product_name", ""),
                "category": product.get("category", ""),
                "titles": title_output,
                "description": description,
                "keywords": ", ".join(keywords),
            }
        )

    save_results(results, OUTPUT_PATH)
    print(f"Done. Results saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    run()
