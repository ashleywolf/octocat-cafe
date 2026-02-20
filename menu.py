"""Menu data for Octocat Café."""

MENU_ITEMS = [
    {
        "name": "Copilot Crunch Cookie",
        "emoji": "🍪",
        "description": "AI-assisted baking at its finest",
        "price": 4.50,
        "category": "snacks",
    },
    {
        "name": "Merge Conflict Mocha",
        "emoji": "☕",
        "description": "Two flavors that somehow work together",
        "price": 6.00,
        "category": "drinks",
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


# Added in PR: Add Dependabot Donut
MENU_ITEMS.append({
    "name": "Dependabot Donut",
    "emoji": "🍩",
    "description": "Automatically keeps your hunger updated",
    "price": 4.00,
    "category": "snacks",
})
