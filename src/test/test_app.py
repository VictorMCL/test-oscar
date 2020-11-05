from src.logic.app import *

def test_sumar():
    assert sumar(3,2) == '5' 

def test_restar():
    assert restar(3,2) == '1' 
    
def test_multiplicar():
    assert multiplicar(2,4) == '8' 

def test_dividir():
    assert dividir(10,2) == '5.0' 