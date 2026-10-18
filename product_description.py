
import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"
MODEL = "gemini-3.8-flash"


def generate(product, features, tone, output):
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key:
        print("ERROR: GEMINI_API_KEY is missing from .env")
        return

    prompt = (
        f"Write a professional product description for: {product}.\n"
        f"Product features: {features}\n"
        f"Tone: {tone}\n\n"
        "Include:\n"
        "1. Product name as heading\n"
        "2. An attractive description of 80-120 words\n"
        "3. Exactly 3 short marketing slogans\n\n"
        "Use only the provided product information. "
        "Do not invent specifications, prices, or certifications."
    )

    print("Generating product description using", MODEL, "...")

    try:
        response = requests.post(
            API_URL,
            headers={
                "x-goog-api-key": api_key,
                "Content-Type": "application/json"
            },
            json={
                "contents": [
                    {
                        "parts": [
                            {"text": prompt}
                        ]
                    }
                ],
                "generationConfig": {
                    "maxOutputTokens": 4096
                }
            },
            timeout=120
        )

        if response.status_code != 200:
            print("ERROR: API request failed.")
            print("HTTP status:", response.status_code)
            print("Response:", response.text[:800])
            return

        data = response.json()
        result = data["candidates"][0]["content"]["parts"][0]["text"]

        print("\n" + result)

        output_path = Path(output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")

        print("\nSUCCESS! Product description generated.")
        print("Saved to:", output_path.resolve())

    except (requests.RequestException, KeyError, IndexError, ValueError) as error:
        print("ERROR:", error)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Assignment 9 - AI Product Description Generator CLI"
    )
    parser.add_argument("--product", required=True)
    parser.add_argument("--features", required=True)
    parser.add_argument("--tone", default="friendly")
    parser.add_argument(
        "--output",
        default="output/product_description.txt"
    )

    args = parser.parse_args()

    generate(args.product, args.features, args.tone, args.output)

