from datetime import datetime
from field import Field

DATE_FORMAT = "%d.%m.%Y"


class Birthday(Field):
    def __init__(self, value: str):
        try:
            # Parsing the input date string to a datetime object
            self.value = datetime.strptime(value, DATE_FORMAT)
        except ValueError:
            # Raise an error for invalid date format
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


def __str__(self):
    # Format the datetime object as a string with the specified format
    return f"{self.value.strftime(DATE_FORMAT)}"
