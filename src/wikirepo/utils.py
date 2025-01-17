"""
Utilities
---------

Utility functions for general operations.

Contents
    _make_var_list,
    _return_given_type,
    try_float,
    round_if_int,
    gen_list_of_lists,
    check_str_similarity,
    check_str_args
"""

from difflib import SequenceMatcher


def _make_var_list(var):
    """
    Allows for a one line check for if a variable is a list.
    """
    var_was_str = False
    if isinstance(var, str):
        var_was_str = True
        var = [var]

    return var, var_was_str


def _return_given_type(var, var_was_str):
    """
    Allows for a one line return or list or string variables.
    """
    if var_was_str:
        # Check if there's only one element
        if len(var) == 1:
            return var[0]

        else:
            return var

    else:
        return var


def try_float(string):
    """Checks if a string is a float."""
    try:
        return float(string)

    except:
        return string


def round_if_int(val):
    """Rounds off the decimal of a value if it is an integer float."""
    if isinstance(val, float) and val.is_integer():
        val = int(val)

    return val


def gen_list_of_lists(original_list, new_structure):
    """Generates a list of lists with a given structure from a given list."""
    assert len(original_list) == sum(
        new_structure
    ), "The number of elements in the original list and desired structure don't match"

    return [
        [original_list[i + sum(new_structure[:j])] for i in range(new_structure[j])]
        for j in range(len(new_structure))
    ]


def check_str_similarity(str_1, str_2):
    """Checks the similarity of two strings."""
    return SequenceMatcher(None, str_1, str_2).ratio()


def check_str_args(arguments, valid_args):
    """
    Checks whether a str argument is valid, and makes suggestions if not.
    """
    if isinstance(arguments, str):
        if arguments in valid_args:
            return arguments

        suggestions = []
        for v in valid_args:
            similarity_score = round(check_str_similarity(str_1=arguments, str_2=v), 2)
            arg_and_score = (v, similarity_score)
            suggestions.append(arg_and_score)

        ordered_suggestions = sorted(suggestions, key=lambda x: x[1], reverse=True)

        print(f"'{arguments}' is not a valid argument for the given function.")
        print(f"The closest valid options to '{arguments}' are:")
        for item in ordered_suggestions[:5]:
            print(item)

        raise ValueError("An invalid string has been passed.")

    elif isinstance(arguments, list):
        # Check arguments, and remove them if they're invalid
        for a in arguments:
            check_str_args(arguments=a, valid_args=valid_args)

        return arguments
