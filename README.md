


# 📊 E-commerce Analysis: An End-to-End Data Project

[![CI](https://github.com/MathGMaia/Ecommerce-data-analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/MathGMaia/Ecommerce-data-analysis/actions)

## **Work in Progress... 🛠️🧑‍💻**

This project implements a complete data pipeline to analyze the Olist e-commerce dataset (available on Kaggle), demonstrating the full data lifecycle from engineering to predictive analysis and business intelligence.

---

## Project ideia

This is not just a data analysis project, but a demonstration of a complete and actionable data system. I believe that high-quality analysis is only possible on top of a robust and reproducible data engineering foundation. The goal is to build a system that reliably and scalably answers business questions from the ground up.

---

## Tech Stack

| Category | Tools |
| :--- | :--- |
| **Languages** | Python (Pandas, Scikit-learn, SQLAlchemy), SQL |
| **Database** | PostgreSQL (with migration plan to GCP) |
| **Engineering & Automation** | Git/GitHub, Docker, GitHub Actions (CI), uv, pre-commit |
| **BI & Visualization** | Power BI, Matplotlib, Seaborn |

---

## Pipeline Architecture (ELT)

Instead of analyzing CSV files directly, this project implements an ELT (Extract, Load, Transform) data pipeline to ensure data quality and governance.

1. **Extract & Load (EL):** The raw data from Olist CSV files is extracted and loaded into a PostgreSQL database under a `raw_olist` schema. This layer acts as a faithful copy of the source, ensuring auditability and reproducibility.
2. **Transform (T):** After loading, the data is transformed using SQL and Python. In this step, it is cleaned, normalized, and modeled to reflect business logic. The result is stored in an `analytics` schema, which serves as the single source of truth for all analyses.

---

## Project updates coming soon 🧑‍💻✅
