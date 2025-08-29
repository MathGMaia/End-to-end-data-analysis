# tests/test_src/test_utils.py

from src.utils.math_ops import add_numbers


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_sample_dataframe_fixture(sample_dataframe):
    # Verifica se a fixture retorna um dataframe válido
    assert "id" in sample_dataframe.columns
    assert "value" in sample_dataframe.columns
    assert len(sample_dataframe) == 3
    assert sample_dataframe["value"].sum() == 60
