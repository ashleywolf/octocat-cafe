# Contributing to Octocat Café ☕

Thanks for wanting to contribute! Here's how to make your PR a smooth brew.

## What We Accept

- **New menu items** — Creative, GitHub-themed food and drink items
- **Bug fixes** — If something's broken, fix it!
- **Tests** — More test coverage is always welcome
- **UI improvements** — Make the menu page look better

## What We Don't Accept

- Unrelated changes (personal links, ads, etc.)
- Changes without tests for new functionality
- PRs that break existing tests

## PR Guidelines

### Title
Use a clear, descriptive title that explains what the PR does.
- ✅ `Add Dependabot Donut to menu`
- ❌ `update stuff`

### Description
Every PR must include:
1. **What** — What does this PR change?
2. **Why** — Why is this change needed?
3. **Testing** — How did you verify it works?

### Code Requirements
- All new menu items must be added to `menu.py`
- New items need a test in `tests/test_app.py`
- Follow existing code style (PEP 8)
- Don't break existing tests

## Running Tests

```bash
pip install -r requirements.txt
pytest tests/
```

## Local Development

```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
```
