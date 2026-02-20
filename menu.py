"""Menu data for Octocat Café."""

MENU_ITEMS = [
    # --- Drinks ---
    {
        "name": "Merge Conflict Mocha",
        "emoji": "☕",
        "description": "Two flavors that somehow work together",
        "price": 6.00,
        "category": "drinks",
    },
    {
        "name": "Git Blame Brew",
        "emoji": "🫖",
        "description": "Find out who made this delicious tea",
        "price": 3.50,
        "category": "drinks",
    },
    {
        "name": "Rebase Refresher",
        "emoji": "🥤",
        "description": "Start fresh with every sip",
        "price": 4.00,
        "category": "drinks",
    },
    {
        "name": "Open Source Oat Milk",
        "emoji": "🥛",
        "description": "Free as in freedom, free as in milk",
        "price": 3.00,
        "category": "drinks",
    },
    {
        "name": "GitHub Actions Espresso Shot",
        "emoji": "⚡",
        "description": "Triggers your morning workflow",
        "price": 2.50,
        "category": "drinks",
    },
    {
        "name": "Issues IPA",
        "emoji": "🍺",
        "description": "We'll get to it eventually",
        "price": 7.00,
        "category": "drinks",
    },
    # --- Snacks ---
    {
        "name": "Copilot Crunch Cookie",
        "emoji": "🍪",
        "description": "AI-assisted baking at its finest",
        "price": 4.50,
        "category": "snacks",
    },
    {
        "name": "404 Not Found Cake",
        "emoji": "🍰",
        "description": "You'll never see it coming",
        "price": 7.50,
        "category": "snacks",
    },
    {
        "name": "Pull Request Pudding",
        "emoji": "🧁",
        "description": "Always ready for review",
        "price": 5.00,
        "category": "snacks",
    },
    {
        "name": "Dependabot Donut",
        "emoji": "🍩",
        "description": "Automatically updated daily",
        "price": 4.00,
        "category": "snacks",
    },
    {
        "name": "Forked Focaccia",
        "emoji": "🍞",
        "description": "Same bread, your own toppings",
        "price": 5.50,
        "category": "snacks",
    },
    # --- Daily Specials ---
    {
        "name": "Release Candidate Croissant",
        "emoji": "🥐",
        "description": "Almost perfect, ship it",
        "price": 6.50,
        "category": "specials",
    },
    {
        "name": "SSH Key Lime Pie",
        "emoji": "🥧",
        "description": "Access granted to flavor town",
        "price": 8.00,
        "category": "specials",
    },
    {
        "name": "README Ramen",
        "emoji": "🍜",
        "description": "Read this before consuming",
        "price": 9.50,
        "category": "specials",
    },
    {
        "name": "Webhook Waffle",
        "emoji": "🧇",
        "description": "Notifies your taste buds instantly",
        "price": 7.00,
        "category": "specials",
    },
]


def get_menu():
    """Return the full menu."""
    return MENU_ITEMS


def get_by_category(category):
    """Return menu items filtered by category."""
    return [item for item in MENU_ITEMS if item["category"] == category]


def get_item(name):
    """Return a single menu item by name."""
    for item in MENU_ITEMS:
        if item["name"].lower() == name.lower():
            return item
    return None
