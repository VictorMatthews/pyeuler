import pytest
from src import problem_3


def test_main() -> None:
    solution = problem_3.main()
    assert solution == 0
