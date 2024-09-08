import os
import sys
from typing import Union, Tuple
from file_data import src_code, test_code


def get_problem_number() -> Union[any, None]:
    """Get problem number from arguments"""
    # sys.argv[0] is the file name python is running
    # The argument we expect after the file name is
    # the number for the problem we are creating
    try:
        return sys.argv[1]
    except IndexError as e:
        return None


def get_files_to_create(problem_number: int) -> Tuple[str]:
    """Get the file names to create and return in a Tuple
    the first value is the src code file, the second value
    is the test code file"""
    src_file = f"problem_{problem_number}.py"
    test_file = f"test_{src_file}"
    cwd = os.getcwd()
    src_file = f"{cwd}{os.sep}src{os.sep}{src_file}"
    test_file = f"{cwd}{os.sep}tests{os.sep}{test_file}"
    return (src_file, test_file)


def validate_problem_number(problem_number: any) -> int:
    """Validate the problem number to scaffold"""
    try:
        problem_number = int(problem_number)
        files_to_create = get_files_to_create(problem_number)
        if os.path.isfile(files_to_create[0]):
            raise Exception("Source file already exists for entered problem number")
        if os.path.isfile(files_to_create[1]):
            raise Exception("Test file already exists for entered problem number")
    except ValueError as e:
        raise Exception("Argument entered is not a number")
    return problem_number


def create_files(problem_number: int) -> None:
    files_to_create = get_files_to_create(problem_number)
    with open(files_to_create[0], "w") as src_file:
        src_file.write(src_code.replace("NEW_PROBLEM_NUMBER", str(problem_number)))
    with open(files_to_create[1], "w") as test_file:
        test_file.write(test_code.replace("NEW_PROBLEM_NUMBER", str(problem_number)))


def scaffold() -> None:
    """Handle scaffolding of problem files"""
    problem_number = get_problem_number()
    if problem_number == None:
        raise Exception("No argument entered for the problem number")
    problem_number = validate_problem_number(problem_number)
    create_files(problem_number)


if __name__ == "__main__":
    try:
        scaffold()
    except Exception as e:
        print(type(e))
        print("Error trying to add problem files")
        print(str(e))
