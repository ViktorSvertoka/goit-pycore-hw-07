from field import Field


class Name(Field):
    """Represents a field for storing a name, inheriting from the Field class."""

    def __init__(self, name):
        """Initialize the Name field with a name."""
        self.value = name
