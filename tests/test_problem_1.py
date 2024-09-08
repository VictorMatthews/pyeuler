import pytest
from src import problem_1


def test_sum_multiples_of_three_or_five() -> None:
    sum = problem_1.sum_multiples_of_three_or_five(10)
    assert sum == 23


def test_main() -> None:
    sum = problem_1.main()
    assert sum == 233168
