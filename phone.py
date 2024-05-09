from field import Field


class Phone(Field):
    """Represents a field for storing a phone number, inheriting from the Field class."""

    def __init__(self, number):
        """Initialize the Phone field with a phone number."""
        self.value = self.validate_number(number)

    def validate_number(self, number):
        """Validate the phone number."""

        if len(number) != 10:
            raise ValueError("The phone number must contain 10 digits")

        if not number.isdigit():
            raise ValueError("The phone number must contain only numbers")

        return number
