import pytest
import math

@pytest.fixture
def numeros():
    return[1, 2, 3, 4, 5]
# Testando o dobro da soma dos elementos  
def test_dobro(numeros):  
    assert sum(x * 2 for x in numeros) == 30  # 15 * 2
