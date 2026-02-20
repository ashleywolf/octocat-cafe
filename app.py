"""Octocat Café — A GitHub-themed café menu app."""

from flask import Flask, jsonify, render_template
from menu import get_menu, get_by_category

app = Flask(__name__)


@app.route("/")
def index():
    """Render the menu page."""
    drinks = get_by_category("drinks")
    snacks = get_by_category("snacks")
    return render_template("index.html", drinks=drinks, snacks=snacks)


@app.route("/api/menu")
def api_menu():
    """Return the full menu as JSON."""
    return jsonify({"menu": get_menu()})


@app.route("/api/menu/<category>")
def api_menu_category(category):
    """Return menu items for a specific category."""
    items = get_by_category(category)
    if not items:
        return jsonify({"error": f"No items found for category: {category}"}), 404
    return jsonify({"category": category, "items": items})


if __name__ == "__main__":
    app.run(debug=True)
