import pytest


@pytest.fixture()
def coll():
    return [1, 2, 3, 4]


@pytest.fixture(autouse=True)
def setup_coll(coll):
    coll[0] = 'a'

def test_first_example(coll):
    assert coll == ['a', 2, 3, 4]


def test_second_example(coll):
    assert coll[0] == 'a'
