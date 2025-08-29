"""
Helpers para rodar queries no Postgres e retornar DataFrames.
"""

import os

import pandas as pd
from sqlalchemy import create_engine, text

# Configuração de conexão
DB_USER = os.getenv("POSTGRES_USER", "ecommerce")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "ecommerce")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "ecommerce")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def run_query(query: str) -> pd.DataFrame:
    """Executa uma query SQL e retorna DataFrame."""
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)
    return df


if __name__ == "__main__":
    # Exemplo: contar pedidos por status
    q = """
    SELECT order_status, COUNT(*) as total_orders
    FROM orders
    GROUP BY order_status
    ORDER BY total_orders DESC
    """
    df = run_query(q)
    print(df)
