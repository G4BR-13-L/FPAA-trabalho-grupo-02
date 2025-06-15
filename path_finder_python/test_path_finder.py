import pytest
from main import a_estrela, Pos
from mazegen import mazegen

def test_caminho_simples():
    labirinto = [['S', '0', 'E']]
    caminho = a_estrela(labirinto)
    assert caminho is not None
    assert caminho[0] == Pos(0, 0)
    assert caminho[-1] == Pos(0, 2)

def test_sem_caminho():
    labirinto = [['S', '1', 'E']]
    caminho = a_estrela(labirinto)
    assert caminho is None

def test_inicio_igual_fim():
    labirinto1 = [['E']]
    caminho = a_estrela(labirinto1)
    assert caminho is None

    labirinto2 = [['S']]
    caminho = a_estrela(labirinto2)
    assert caminho is None

def test_labirinto_vazio():
    labirinto = []
    caminho = a_estrela(labirinto)
    assert caminho is None

def test_labirinto_gerado():
    labirinto = mazegen()
    caminho = a_estrela(labirinto)
    assert caminho is not None