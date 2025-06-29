# Project‑Management‑As‑Code (PMAC) Core

> **Lightweight, declarative, and test‑driven project blueprints — stored as JSON, validated by schema, automated by CLI.**

---

## ✨ Key Features

| Capability               | Description                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Schema‑driven**        | Strict JSON Schema (`src/pmac/schema/v0_1.json`) guarantees consistency between humans, AI, and tooling. |
| **CLI Toolkit**          | `pmac` console script provides `validate` (with `init`, `generate` coming next).                         |
| **Self‑Bootstrapping**   | GitHub Actions regenerate docs & templates on every merge. PMAC manages its own backlog.                         |
| **Quality Requirements** | Built‑in QR fields (`performance`, `security`, `logging`, `other`) for traceable non‑functional requirements.    |
| **Extensible**           | Future versions add dependency graphs, workflow hooks, and richer integrations (Jira, GitHub, Terraform, etc.).  |

---

## 📂 Repository Layout (v0.1)

```
├── src/
│   └── pmac/
│       ├── __init__.py
│       ├── cli/__main__.py
│       ├── validators.py
│       └── schema/
│           └── v0_1.json
├── tests/
│   ├── fixtures/
│   │   ├── valid/pmac_min.json
│   │   └── invalid/missing_team.json
│   └── unit/test_schema.py
├── docs/
│   └── schema_overview.md
├── .github/workflows/ci.yml
├── .gitignore
├── .env.example
├── .pre-commit-config.yaml
├── mkdocs.yml
├── pyproject.toml
├── CHANGELOG.md
├── LICENSE
└── README.md
```

> **Src‑layout:** everything importable lives under `src/`; resources (schema, templates) are included via `importlib.resources`.

---

## 🚀 Quick Start

```bash
git clone https://github.com/your-handle/pmac-core.git
cd pmac-core
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pmac validate tests/fixtures/valid/pmac_min.json
```

---

## 🛣 Roadmap

| Milestone                    | Target | Status        |
| ---------------------------- | ------ | ------------- |
| **Schema v0.1**              | Week 1 | ✅ Complete    |
| **CLI MVP**                  | Week 2 | ⏳ In Progress |
| **Self‑bootstrap CI**        | Week 3 | 🔜            |
| **Starter templates & docs** | Week 4 | 🔜            |

---

Released under the **MIT License** — see `LICENSE`.
