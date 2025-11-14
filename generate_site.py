from pathlib import Path
import json

# Load product data
with open("data/products.json", "r") as f:
    products = json.load(f)

# Load the HTML template
template = Path("templates/index_template.html").read_text()

# Generate product cards
cards = ""
for p in products:
    cards += f"""
    <div class="product-card">
        <img src="{p['image']}" alt="{p['name']}">
        <h3>{p['name']}</h3>
        <p>{p['price']}</p>
    </div>
    """

# Insert cards into template
html = template.replace("{{ products }}", cards)

# Build output folder
Path("site/static").mkdir(parents=True, exist_ok=True)

(Path("site") / "index.html").write_text(html)

# Copy static files
for asset in Path("static").glob("*"):
    (Path("site/static") / asset.name).write_bytes(asset.read_bytes())

print("✅ Site built! Open site/index.html to preview.")
