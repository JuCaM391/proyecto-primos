from primos import es_primo

def test_numero_primo():
    assert es_primo(7) == True

def test_numero_no_primo():
    assert es_primo(4) == False

def test_numero_uno_no_es_primo():
    assert es_primo(1) == False

def test_numero_dos_es_primo():
    assert es_primo(2) == True

def test_numero_negativo():
    assert es_primo(-5) == False
