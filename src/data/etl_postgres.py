"""
ETL script para carregar CSVs no Postgres.
Este arquivo serve como placeholder para projetos futuros.
"""

import os

import pandas as pd
from sqlalchemy import create_engine

# Configuração de conexão
DB_USER = os.getenv("POSTGRES_USER", "ecommerce")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "ecommerce")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "ecommerce")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def load_csv_to_postgres(csv_path: str, table_name: str, if_exists: str = "replace"):
    """Carrega um CSV para uma tabela no Postgres."""
    engine = create_engine(DATABASE_URL)
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    print(f"✅ CSV {csv_path} carregado na tabela {table_name} ({len(df)} linhas).")


if __name__ == "__main__":
    # Exemplo: carregar o dataset de clientes
    load_csv_to_postgres("data/raw/olist_customers_dataset.csv", "customers")
