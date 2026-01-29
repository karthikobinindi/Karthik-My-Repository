import pytest
from app import multiply

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 5, 25),
    (10, 0, 0),
    (-1, 8, -8)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.slow
@pytest.mark.parametrize("a,b,expected", [
    (100, 200, 20000),
    (300, 400, 120000)
])
def test_large_multiplications(a, b, expected):
    assert multiply(a, b) == expected
