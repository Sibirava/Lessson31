import pytest


def setup_module():
    print("setup module level")


def teardown_module():
    print("teardown module level")


def bfhsdjfbds():
    print("setup function level")


def teardown_function(function):
    print("teardown function level")


def test_passing():
    print("running test_passing")

    assert (1, 2, 3) == (1, 2, 3)


def test_failing():
    print("running test_failing", end=' ')
    assert (1, 2, 3) == (3, 2, 1)


def test_custom_failing():
    print("running test_custom_failing", end=' ')
    pytest.fail()