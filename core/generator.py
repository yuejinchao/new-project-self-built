from pathlib import Path

from openai import OpenAI


class ListingGenerator:
    def __init__(self, api_key, config, root):
        self.client = OpenAI(api_key=api_key)
        self.config = config
        self.root = Path(root)

    def generate_titles(self, product):
        prompt = self._render_prompt("title_prompt.txt", product)
        return self._complete(prompt)

    def generate_description(self, product):
        prompt = self._render_prompt("desc_prompt.txt", product)
        return self._complete(prompt)

    def _render_prompt(self, filename, product):
        template_path = self.root / "prompts" / filename
        template = template_path.read_text(encoding="utf-8")
        values = {
            "product_name": product.get("product_name", ""),
            "category": product.get("category", ""),
            "material": product.get("material", ""),
            "application": product.get("application", ""),
            "style": self.config.get("style", "Alibaba International B2B SEO optimized"),
            "language": self.config.get("language", "en"),
        }
        return template.format(**values)

    def _complete(self, prompt):
        response = self.client.chat.completions.create(
            model=self.config.get("model", "gpt-4.1-mini"),
            temperature=float(self.config.get("temperature", 0.7)),
            messages=[
                {
                    "role": "system",
                    "content": "You are an Alibaba International B2B SEO and listing optimization expert.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content.strip()
