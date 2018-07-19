from how_to_handle_kwargs import existingFunction
from how_to_handle_kwargs import no_op


def test_lists():
    x = [1, 3]
    result = existingFunction(x)
    assert x == x

def test_dicts():
    pass