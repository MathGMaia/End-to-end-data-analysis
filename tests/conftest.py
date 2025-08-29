import pandas as pd
import pytest


@pytest.fixture
def sample_dataframe():
    """Fixture de DataFrame de exemplo para usar nos testes."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3],
            "value": [10, 20, 30],
        }
    )
