# Full Data Project Template

Este repositório é um **template para projetos de dados end-to-end**.
Inclui:
- Engenharia de dados (Postgres + Docker)
- SQL (exploração e manipulação)
- Python (ETL, limpeza e análise)
- Estatística (testes de hipóteses)
- Machine Learning (modelos preditivos)
- BI (dashboards em notebooks)

## 🚀 Como rodar

1. Subir containers:
```bash
docker compose up -d
Postgres → localhost:5432

Jupyter → http://localhost:8888

Rodar notebooks na ordem:

01_sql_exploration.ipynb

02_cleaning_analysis.ipynb

03_statistics.ipynb

04_ml_modeling.ipynb

05_bi_dashboard.ipynb

yaml
Copy code
```
---

## 📌 Próximos passos no Git
Depois de fazer tudo:
```bash
git add data/raw/README.md data/interim/README.md data/processed/README.md data/external/README.md \
       src/data/etl_postgres.py src/data/query.py \
       tests/test_data/test_etl_postgres.py \
       README.md
git commit -m "chore: add ETL/query placeholders, data docs, and tests to template"
git push origin chore/setup-fulldata-project
```
# Olist Data Science Project Template

# A Foundation for Modern Data Science 🚀

Data science projects can easily become a tangle of untitled notebooks, undocumented data, and inconsistent code. This boilerplate is your launchpad for building clean, reproducible, and production-ready projects from day one.

It's designed to handle the project engineering, so you can focus on the data science. By providing a logical structure and automating best practices, you can spend less time on setup and more time building something great.

## Guiding Principles

This isn't just a folder structure; it's a workflow designed for professional and collaborative data science.

* **Built for Reproducibility.** This template uses `uv` for dependency management with a locked `uv.lock` file. If it works on your machine, it's guaranteed to work for your teammates and in production.
* **Code Quality, Automated.** Say goodbye to style guide debates! Code is automatically formatted with `black` and linted with `ruff` using `pre-commit` hooks, ensuring all committed code is clean and consistent.
* **A Clear Data Pipeline.** The `data/` directory guides a one-way flow from immutable raw data (`raw`) to cleaned (`interim`) and feature-engineered (`processed`) datasets, creating a transparent and debuggable workflow.
* **The Right Tool for the Job.** `notebooks/` are for exploring, prototyping, and telling data stories. Once logic is ready to be reused, it's moved into `src/` as clean, reusable, and testable Python modules.

## What's Inside?

* **A Thoughtful Project Structure:** An intuitive layout to keep your project organized and scalable.
    ```
    project_name/
    ├── data/
    │   ├── external/
    │   ├── interim/
    │   ├── processed/
    │   └── raw/
    ├── models/
    ├── notebooks/
    ├── src/
    │   └── __init__.py
    ├── tests/
    │   └── __init__.py
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── .gitignore
    ├── .pre-commit-config.yaml
    ├── pyproject.toml
    └── README.md
    ```
* **Blazing-Fast Dependency Management:** Uses `uv` for incredibly fast package installation and dependency resolution, all managed through the modern `pyproject.toml` standard.
* **Automated Quality Checks:** Pre-configured `pre-commit` hooks with `black` and `ruff` ensure flawless code style and catch potential errors before they're even committed.
* **Ready-to-Go CI/CD:** Includes a GitHub Actions workflow (`ci.yml`) to automatically run your tests (`pytest`) and linter on every push and pull request.

## Get Started in Minutes

1.  **Create Your Project:**
    * Click the green **"Use this template"** button at the top of the repository page to create a copy with a clean Git history.

2.  **Clone Your New Repository:**
    ```bash
    git clone git@github.com:your-username/your-new-repository.git
    cd your-new-repository
    ```

3.  **Set Up The Environment:**
    * This command creates a virtual environment and installs all dependencies from the lock file.
    ```bash
    uv pip sync
    ```

4.  **Activate Pre-commit Hooks:**
    * This enables automatic code quality checks before each commit.
    ```bash
    pre-commit install
    ```

5.  **Start Building!**
    * Place raw data in `data/raw/`.
    * Explore and analyze in `notebooks/`.
    * Refactor reusable code into Python modules in `src/`.
    * Add unit tests for your modules in `tests/`.

## Recommended Workflow

This template encourages a sequential and organized analysis process. We recommend structuring your work in the `notebooks/` directory as follows:

1.  **`01_data_intake.ipynb`**: Load raw data, perform initial inspections (check for nulls, data types), and save a versioned, interim dataset.
2.  **`02_data_cleaning.ipynb`**: Handle missing values, correct data types, remove duplicates, and perform other cleaning tasks.
3.  **`03_exploratory_data_analysis.ipynb`**: Dive deep into the cleaned data. Create visualizations, identify correlations, and formulate hypotheses.
4.  **`04_model_baseline.ipynb`**: Build and evaluate your first simple model. This serves as the benchmark to beat.
5.  **`05_model_optimization.ipynb`**: Develop more complex models, perform hyperparameter tuning, and compare results against the baseline.

This numbered approach ensures that your analysis is a clear, reproducible story that anyone on your team can follow.

---

I built this to make doing the right thing the easy thing, even when deadlines are tight. I can't wait to see what you build!
