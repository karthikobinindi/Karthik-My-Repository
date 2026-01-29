import pytest
from app import divide

def test_environment(env):
    assert env in ["dev", "prod"]


@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert False


@pytest.mark.xfail(reason="Known issue: division by zero raises error")
def test_divide_by_zero():
    divide(10, 0)
