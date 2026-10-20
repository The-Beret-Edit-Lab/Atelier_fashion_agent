import json

# Atelier Capsule Wardrobe Inventory
CATALOG = [
    {
        "id": "ATL-01",
        "name": "Structured Double-Breasted Wool Trench",
        "category": "outerwear",
        "color": "camel",
        "price": 340.00,
        "stock": 4,
        "vibes": ["parisian", "minimalist", "capsule staple"],
    },
    {
        "id": "ATL-02",
        "name": "Heavyweight Mulberry Silk Slip Skirt",
        "category": "bottoms",
        "color": "champagne cream",
        "price": 180.00,
        "stock": 6,
        "vibes": ["minimalist", "tactile luxury", "evening"],
    },
    {
        "id": "ATL-03",
        "name": "Chunky Ribbed Cashmere Turtleneck",
        "category": "knitwear",
        "color": "charcoal heather",
        "price": 240.00,
        "stock": 0,  # Out of stock to test agent recovery
        "vibes": ["cozy", "scandi", "winter layering"],
    },
    {
        "id": "ATL-04",
        "name": "Fine-Gauge Merino Mockneck Knit",
        "category": "knitwear",
        "color": "ivory ecru",
        "price": 150.00,
        "stock": 5,
        "vibes": ["parisian", "understated", "layering foundation"],
    },
    {
        "id": "ATL-05",
        "name": "Sculptural Wool Felt Beret",
        "category": "accessories",
        "color": "noir black",
        "price": 75.00,
        "stock": 3,
        "vibes": ["parisian", "heritage", "signature accent"],
    },
]

def search_catalog(aesthetic_query: str, max_budget: float = 1000.0) -> str:
    """Discovers garments by aesthetic keywords, material, or color palette.

    Args:
        aesthetic_query: Style terms, fabrics, or colors to search.
        max_budget: Upper price limit for items.
    """
    print(f"\n⚡ [TOOL CALLED] search_catalog(aesthetic_query='{aesthetic_query}')")
    tokens = aesthetic_query.lower().split()
    results = [
        item for item in CATALOG
        if any(t in f"{item['name']} {item['color']} {' '.join(item['vibes'])}".lower() for t in tokens)
        and item["price"] <= max_budget
    ]
    print(f"📦 [TOOL RETURN] Found {len(results)} items")
    return json.dumps(results)

def check_stock(item_id: str) -> str:
    """Verifies stock availability for a specific garment ID.

    Args:
        item_id: Unique SKU identifier (e.g. 'ATL-01').
    """
    print(f"\n⚡ [TOOL CALLED] check_stock(item_id='{item_id}')")
    for item in CATALOG:
        if item["id"] == item_id:
            return json.dumps({"id": item_id, "in_stock": item["stock"] > 0, "units": item["stock"]})
    return json.dumps({"error": "Item not found"})