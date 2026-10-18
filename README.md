# Assignment 9: Product Description Generator (CLI)

**Group:** Cronus

**Members:** K M Arafat Islam, Rubina Akther, Mahamud Galib Bin, Zarin Anjum Prova

A Python CLI application that uses the Pollinations AI chat-completions API to generate an accurate product description and three marketing slogans from product information provided by the user.

## Model

The script requests the Pollinations AI `openai` model alias. The actual model routed by the service may vary. Check the API response/provider dashboard if you need the exact model identifier for reporting.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
notepad .env
```

Put your valid Pollinations API key in `.env` and never commit that file.

## Run

```powershell
python product_description.py --product "NordicGo Travel Backpack" --features "water-resistant fabric, padded shoulder straps, laptop compartment, 20-liter capacity" --tone friendly --output output/backpack_description.txt
```

The result appears in the terminal and is saved to a text file.

## Files

- `product_description.py`: Python CLI program
- `requirements.txt`: dependencies
- `.env.example`: API key placeholder (no secrets)
- `.gitignore`: prevents accidental commits of secrets and virtual environments

## Screenshots for Moodle

1. CLI command and generated product description with three slogans.
2. Saved `.txt` output opened in Notepad.

Only claim successful generation after running the script and verifying its output. This example is text-based and does not analyze a product photograph.
