import pytest
from main import fill_all_regions

def test_exemplo_1():
    entrada = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0],
    ]
    esperado = [
        [2, 2, 1, 3, 3],
        [2, 1, 1, 3, 3],
        [2, 2, 1, 1, 1],
        [1, 1, 4, 4, 4],
    ]
    resultado = fill_all_regions(entrada, 0, 0)
    assert resultado == esperado

def test_exemplo_2():
    entrada = [
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
    ]
    esperado = [
        [3, 1, 2, 2, 1],
        [3, 1, 2, 2, 1],
        [3, 1, 1, 1, 1],
        [3, 3, 3, 1, 4],
    ]
    resultado = fill_all_regions(entrada, 0, 2)
    assert resultado == esperado

def test_sem_area_navegavel():
    entrada = [
        [1, 1],
        [1, 1],
    ]
    esperado = [
        [1, 1],
        [1, 1],
    ]
    resultado = fill_all_regions(entrada, 0, 0)
    assert resultado == esperado

def test_inicio_em_area_colorida():
    entrada = [
        [2, 0],
        [1, 1],
    ]
    esperado = [
        [2, 2],
        [1, 1],
    ]
    resultado = fill_all_regions(entrada, 0, 0)
    assert resultado == esperado

def test_inicio_em_obstaculo():
    entrada = [
        [1, 0],
        [0, 0],
    ]
    esperado = [
        [1, 2],
        [2, 2],
    ]
    resultado = fill_all_regions(entrada, 0, 0)
    assert resultado == esperado