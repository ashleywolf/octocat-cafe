# ☕ Octocat Café

[![GitHub Pages](https://img.shields.io/badge/demo-live-brightgreen?logo=github)](https://ashleywolf.github.io/octocat-cafe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Copilot](https://img.shields.io/badge/Made%20with-Copilot-blue?logo=githubcopilot)](https://github.com/features/copilot)

A GitHub-themed café menu app — where every commit comes with a cup of coffee. Built with Python/Flask and deployed on GitHub Pages.

> `git clone deliciousness && npm run brew`

## 🌐 Live Demo

**[ashleywolf.github.io/octocat-cafe](https://ashleywolf.github.io/octocat-cafe/)**

![Octocat Café Screenshot](https://via.placeholder.com/800x400/0d1117/58a6ff?text=☕+Octocat+Café+—+Menu+Preview)

## 📋 Menu Preview

### ☀️ Daily Specials
| Item | Price |
|------|-------|
| 🥐 **Release Candidate Croissant** — Almost perfect, ship it | $6.50 |
| 🥧 **SSH Key Lime Pie** — Access granted to flavor town | $8.00 |
| 🍜 **README Ramen** — Read this before consuming | $9.50 |
| 🧇 **Webhook Waffle** — Notifies your taste buds instantly | $7.00 |

### 🥤 Drinks
| Item | Price |
|------|-------|
| ☕ **Merge Conflict Mocha** — Two flavors that somehow work together | $6.00 |
| 🫖 **Git Blame Brew** — Find out who made this delicious tea | $3.50 |
| 🥤 **Rebase Refresher** — Start fresh with every sip | $4.00 |
| 🥛 **Open Source Oat Milk** — Free as in freedom, free as in milk | $3.00 |
| ⚡ **GitHub Actions Espresso Shot** — Triggers your morning workflow | $2.50 |
| 🍺 **Issues IPA** — We'll get to it eventually | $7.00 |

### 🍪 Snacks
| Item | Price |
|------|-------|
| 🍪 **Copilot Crunch Cookie** — AI-assisted baking at its finest | $4.50 |
| 🍰 **404 Not Found Cake** — You'll never see it coming | $7.50 |
| 🧁 **Pull Request Pudding** — Always ready for review | $5.00 |
| 🍩 **Dependabot Donut** — Automatically updated daily | $4.00 |
| 🍞 **Forked Focaccia** — Same bread, your own toppings | $5.50 |

## 🚀 Getting Started

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` to see the menu.

## 🔌 API

```bash
# Full menu
curl http://localhost:5000/api/menu

# By category
curl http://localhost:5000/api/menu/drinks
curl http://localhost:5000/api/menu/specials
```

## 🧪 Tests

```bash
pytest tests/ -q
```

## 🤝 Contributing

Got an idea for a new menu item? We'd love it!
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to make your PR a smooth brew.

## 📄 License

MIT
