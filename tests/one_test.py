import pytest


class TestSimple:
    def test_passing(self):
        assert (1, 2, 3) == (1, 2, 3)

    def test_failing(self):
        assert (1, 2, 3) == (3, 2, 1)

    def test_custom_failing(self):
        pytest.fail()