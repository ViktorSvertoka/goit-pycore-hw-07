from collections import UserDict


class AddressBook(UserDict):
    """A simple address book implementation."""

    def add_record(self, record):
        """Add a record to the address book."""
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """Find a record by name."""
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' not found.")
        return record

    def delete(self, name):
        """Delete a record by name."""
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]
