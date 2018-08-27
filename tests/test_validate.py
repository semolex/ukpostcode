from unittest import TestCase

from ukpostcode import validate
from ukpostcode import PostCodeValidationError

VALID_CODES = (
    "EC1A 1BB", "W1A 0AX", "M1 1AE", "B33 8TH", "DN55 1PT", "SW1W 0NY", "PO16 7GZ", "CO4 3SQ",
    "B24 9QG", "RM4 1XH", "GU26 6LN", "DL16 6RU", "AA9A 9AA", "A9A 9AA", "A9 9AA", "AA9 9AA",
    "AA99 9AA", "TKCA 1ZZ", "E20 3EL"
)


INVALID_CODES = (
    "! !",
    "AAFDF 1AE",
    "W1A 0AX2",
    "TRE-123",
    "1ER UIT",
    "T2W U12",
    "AAAA 122",
    "1234 AAA",
    "1U26 6LN",
    "GU26 6",
    "GU2634 6LN"
)


class TestValidate(TestCase):
    def test_validate_success(self):
        for postcode in VALID_CODES:
            self.assertTrue(validate(postcode))

    def test_validate_fail(self):
        for postcode in INVALID_CODES:
            with self.assertRaises(PostCodeValidationError):
                validate(postcode)
