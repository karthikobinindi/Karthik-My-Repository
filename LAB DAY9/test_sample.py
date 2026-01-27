from math_utils import add
import pytest

@pytest.mark.smoke
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2
