from collections import OrderedDict
import sys
from typing import Any

def _get_duplicates_hashable(input_list: list) -> list:
    """
    Given a list of hashable objects,
    Returns a list of the objects that appear at least twice,
    in the order that they appear for the first time in the original list.

    Parameters:
        input_list: list
            A list of hashable objects

    Returns:
        list
            A list of the objects that appear at least twice,
            ordered by their first appearance.
    """

    # To preserve the order of the elements, we can use a regular dict in Python 3.7+,
    # but we must use an OrderedDict for previous versions,
    # as dicts started being insertion ordered in 3.7.
    elements = {} if sys.version_info > (3, 6) else OrderedDict()

    for element in input_list:
        if element in elements:
            elements[element] = True
        else:
            elements[element] = False

    return [x for x in elements.keys() if elements[x]]

def _get_duplicates_unhashable(input_list: list) -> list:
    """
    Given a list of unhashable objects,
    Returns a list of the objects that appear at least twice,
    in the order that they appear for the first time in the original list.

    Parameters:
        input_list: list
            A list of unhashable objects

    Returns:
        list
            A list of the objects that appear at least twice,
            ordered by their first appearance.
    """

    return [element for idx, element in enumerate(input_list) if element in input_list[:idx]]

def get_duplicates(input_list: list) -> list:
    """
    Given a list of objects,
    Returns a list of the objects that appear at least twice,
    in the order that they appear for the first time in the original list.

    Parameters:
        input_list: list
            A list of objects

    Returns:
        list
            A list of the objects that appear at least twice,
            ordered by their first appearance.
    """

    # If the list is empty, return an empty list
    if not input_list:
        return []

    # Check if the first element in the list is hashable
    if is_hashable(input_list[0]):
        # If the first element is hashable, we assume all elements in the list are hashable
        return _get_duplicates_hashable(input_list)
    else:
        return _get_duplicates_unhashable(input_list)
    

def is_hashable(input_obj: Any) -> bool:
    """
    Determine if an input object is hashable.

    Parameters:
        input_obj: Any
            The object to check

    Returns:
        bool
            True if input_obj is hashable, False otherwise
    """

    try:
        hash(input_obj)
    except Exception:
        return False
    return True


def main():
    # Hashable input list
    input_list = ["b", "a", "c", "c", "e", "a", "c", "d", "c", "d"]
    expected_output = ["a", "c", "d"]

    actual_output = get_duplicates(input_list)

    if actual_output == expected_output:
        print("Actual output matches the expected output.")
    else:
        print("Actual output does not match the expected output.")

    print(f"Expected output: {expected_output}")
    print(f"Actual output: {actual_output}")

    # Unhashable input list
    unhashable_input_list = [{"a": "b"}, {"c": "d"}, {"a": "b"}, {"d": "e"}, {"d": "e"}]
    expected_output = [{"a": "b"}, {"d": "e"}]

    actual_output = get_duplicates(unhashable_input_list)

    if actual_output == expected_output:
        print("Actual output matches the expected output.")
    else:
        print("Actual output does not match the expected output.")

    print(f"Expected output: {expected_output}")
    print(f"Actual output: {actual_output}")

if __name__ == '__main__':
    main()