import os
import random

def test_pytest1_test1():
    pass


def test_pytest1_test2():
    assert False


def test_even_failed():
    assert int(os.environ.get("PARAM", 0)) % 2 != 0


def test_odd_failed():
    assert int(os.environ.get("PARAM", 0)) % 2 == 0


def test_random():
    assert random.randint(1, 10) >= 5
