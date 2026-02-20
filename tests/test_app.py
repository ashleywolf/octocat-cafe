"""Tests for Octocat Café."""

import pytest
from app import app
from menu import get_menu, get_by_category, get_item


@pytest.fixture
def client():
    """Create a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index_page(client):
    """Test that the menu page loads."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Octocat" in response.data


def test_api_menu(client):
    """Test the JSON menu endpoint."""
    response = client.get("/api/menu")
    assert response.status_code == 200
    data = response.get_json()
    assert "menu" in data
    assert len(data["menu"]) > 0


def test_api_menu_category(client):
    """Test filtering by category."""
    response = client.get("/api/menu/drinks")
    assert response.status_code == 200
    data = response.get_json()
    assert data["category"] == "drinks"
    assert all(item["category"] == "drinks" for item in data["items"])


def test_api_menu_invalid_category(client):
    """Test 404 for invalid category."""
    response = client.get("/api/menu/nonexistent")
    assert response.status_code == 404


def test_get_menu():
    """Test get_menu returns all items."""
    menu = get_menu()
    assert len(menu) == 15
    names = [item["name"] for item in menu]
    assert "Copilot Crunch Cookie" in names
    assert "SSH Key Lime Pie" in names


def test_get_item():
    """Test finding a specific item."""
    item = get_item("Merge Conflict Mocha")
    assert item is not None
    assert item["price"] == 6.00


def test_get_item_not_found():
    """Test that missing items return None."""
    assert get_item("Nonexistent Item") is None
