from unittest.mock import patch
from primos import es_primo

def test_mock_es_primo():
    with patch('primos.es_primo', return_value=True) as mock_func:
        resultado = mock_func(4)
        assert resultado == True
        mock_func.assert_called_once_with(4)
