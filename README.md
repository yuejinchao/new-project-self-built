# Alibaba AI Listing System

Alibaba AI Listing System is a runnable MVP for generating Alibaba International product listing content from a CSV file. It creates SEO-friendly titles, B2B product descriptions, keyword suggestions, and saves the results to `output/results.csv`.

## Features

- Batch process products from `data/input.csv`
- Generate 5 Alibaba-style English SEO titles for each product
- Generate B2B product descriptions with features, materials, applications, and buyer benefits
- Extract simple keyword suggestions from generated text
- Save all generated content to CSV

## Project Structure

```text
.
├── app.py
├── config.json
├── requirements.txt
├── core/
│   ├── __init__.py
│   ├── generator.py
│   ├── parser.py
│   └── seo.py
├── data/
│   └── input.csv
├── output/
│   └── .gitkeep
└── prompts/
    ├── desc_prompt.txt
    └── title_prompt.txt
```

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:

```bash
set OPENAI_API_KEY=your_api_key_here
```

On macOS or Linux:

```bash
export OPENAI_API_KEY=your_api_key_here
```

3. Run the generator:

```bash
python app.py
```

The generated listing content will be saved to `output/results.csv`.

## Input Format

Edit `data/input.csv` and add one product per row:

```csv
product_name,category,material,application
woven label,garment accessories,polyester,clothing brand label
hang tag,garment accessories,paper,clothing packaging
```

Only `product_name` is required. Other columns are optional and help improve output quality.
