src_code = """\"\"\"
ENTER PROBLEM INFO HERE
\"\"\"

def main() -> int:
    return 0
    

if __name__ == "__main__":
    print("Starting Problem NEW_PROBLEM_NUMBER")
    solution = main()
    print(f"The solution to problem NEW_PROBLEM_NUMBER is {solution}")
    
"""

test_code = """import pytest
from src import problem_NEW_PROBLEM_NUMBER


def test_main() -> None:
    solution = problem_NEW_PROBLEM_NUMBER.main()
    assert solution == 0

"""
