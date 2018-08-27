"""
Python library, used to validate UK postodes via simple, pure-pythonic algorithms.
"""

# CONSTANTS TO CHECK
OUTWARD_MIN_LENGTH = 2
OUTWARD_MAX_LENGTH = 4
OUTWARD_ALPHA_POS = (0, 1)

INWARD_MIN_LENGTH = 3
INWARD_MAX_LENGTH = 3
INWARD_ALPHA_POS = (1, 3)
INWARD_NUM_POS = (0, 1)


class PostCodeValidationError(Exception):
    """
    Exception, raised if conditions are not met.
    """
    pass


def validate(postcode: str):
    """
    Single interface for postcode validation.
    Performs parts extraction and calls appropriate
    function for each part.

    :param str postcode: postcode to validate.
    :return: True if code is validates, else `PostCodeValidationError` is raised.
    """
    try:
        outward, inward = postcode.split(' ')
    except ValueError:
        raise PostCodeValidationError(
            "Cannot extract parts. Postcode must be string type and have single space between parts.")
    _validate_outward(outward)
    _validate_inward(inward)
    return True


def _validate_outward(outward: str):
    """
    Combines together validation function to perform check for outward postcode part.

    :param str outward: outward part of the postcode.
    """
    _check_is_alphanum(outward)
    _check_length(outward, OUTWARD_MIN_LENGTH, OUTWARD_MAX_LENGTH)
    _check_is_alpha(outward, OUTWARD_ALPHA_POS)


def _validate_inward(inward: str):
    """
    Combines together validation function to perform check for inward postcode part.
    :param str inward: outward part of the postcode.
    :return:
    """
    _check_is_alphanum(inward)
    _check_length(inward, INWARD_MIN_LENGTH, INWARD_MAX_LENGTH)
    _check_is_alpha(inward, INWARD_ALPHA_POS)
    _check_is_num(inward, INWARD_NUM_POS)


def _check_is_alphanum(to_check: str):
    """
    Checks if passed parameter is alphanumeric.

    :param str to_check: postcode or part to check.
    :raises: `PostCodeValidationError` if check is False.
    """
    if not to_check.isalnum():
        raise PostCodeValidationError(f'Part {to_check} includes non-alphanumeric values.')


def _check_length(to_check: str, _min: int, _max: int):
    """
    Checks if passed parameter length is within allowed range.

    :param str to_check: postcode or part to check.
    :param int _min: minimal length that postcode part can have.
    :param int _max: maximum length that postcode part can have.
    :raises: `PostCodeValidationError` if check is False.
    """
    length = len(to_check)
    if length < _min or length > _max:
        raise PostCodeValidationError(
            f'Postcode part {to_check} cannot be more than {_max} or less than {_min}')


def _check_is_num(to_check: str, pos: tuple):
    """
    Checks if passed parameter is numeric value at given position.

    :param str to_check: postcode or part to check.
    :param tuple pos: tuple that represents slice of postcode to check.
    :raises: `PostCodeValidationError` if check is False.
    """
    if not to_check[pos[0]:pos[1]].isnumeric():
        raise PostCodeValidationError(
            f'Postcode part {to_check} at position {pos} must be numeric.')


def _check_is_alpha(to_check: str, pos: tuple):
    """
    Checks if passed parameter is alphabetic value at given position.

    :param str to_check: postcode or part to check.
    :param tuple pos: tuple that represents slice of postcode to check.
    :raises: `PostCodeValidationError` if check is False.
    """
    if not to_check[pos[0]:pos[1]].isalpha():
        raise PostCodeValidationError(
            f'Postcode part {to_check} at position {pos} must be an alphabetic character.')
