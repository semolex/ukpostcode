#### Python library, used to validate UK postcodes via simple, pure-pythonic algorithms.

#### Installation

`cd` into source directory and run:

`python setup.py install`

#### Usage example:


```python 
>>> from ukpostcode import validate
>>> validate("EC1A 1BB")  # valid
True
>>> validate("W1A 0AX")  # valid
True
>>> validate("1234 AAA")  # invalid
Traceback (most recent call last):
...
ukpostcode.main.PostCodeValidationError: Postcode part 1234 at position (0, 1) must be an alphabetic character
```
