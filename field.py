class Field:
    """Represents a generic field with a value."""

    def __init__(self, value):
        """Initialize the Field with a value."""
        self.value = value

    def __str__(self):
        """Return the string representation of the value."""
        return str(self.value)
