import pytest


@pytest.fixture
def order():
    return []


@pytest.fixture
def inner(order):
    order.append("inner")


@pytest.fixture
def outer(order, inner):
    order.append("outer")

def test_order(order, outer):
    assert order == ["inner", "outer"]

class TestOne:
    @pytest.fixture
    def inner(self, order):
        order.append("one")

    def test_order(self, order, outer):
        assert order == ["one", "outer"]


class TestTwo:
    @pytest.fixture
    def inner(self, order):
        order.append("two")

    def test_order(self, order, outer):
        assert order == ["two", "outer"]