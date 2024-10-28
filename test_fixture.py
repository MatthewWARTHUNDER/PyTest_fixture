import pytest

#Definindo uma fixture chamada 'lista_simples'
@pytest.fixture
def lista_simples():
    return[1, 2, 3, 4, 5]

# Usando a fixture 'lista_simples1' em um teste
def test_soma(lista_simples):
    assert sum(lista_simples) == 15


# Testando o menor elemento da lista  
def test_menor_elemento(lista_simples):  
    assert min(lista_simples) == 1  

# Testando o maior elemento da lista  
def test_maior_elemento(lista_simples):  
    assert max(lista_simples) == 5  

# Testando o comprimento da lista  
def test_comprimento(lista_simples):  
    assert len(lista_simples) == 5  

# Testando se a lista contém o número 3  
def test_contem_tres(lista_simples):  
    assert 3 in lista_simples  
