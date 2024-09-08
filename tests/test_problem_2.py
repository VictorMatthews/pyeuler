import pytest
from src import problem_2


def test_main() -> None:
    sum_of_even_fibonacci_numbers = problem_2.main()
    assert sum_of_even_fibonacci_numbers == 4613732
