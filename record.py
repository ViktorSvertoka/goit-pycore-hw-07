from phone import Phone
from name import Name
from birthday import Birthday


class Record:
    # Represents a contact record containing a name and a list of phone numbers.

    def __init__(self, name):
        # Initialize the Record with a name and an empty list of phones.
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):
        # Concatenate contact name and phones.
        contact_info = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

        # Add birthday if available
        if self.birthday:
            contact_info += f", birthday: {self.birthday}"

        return contact_info

    def add_phone(self, number: str):
        # Add a phone number to the record.
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        # Remove a phone number from the record.
        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number: str, new_number: str):
        # Edit a phone number in the record.
        found = False  # Flag to indicate if the old phone number was found
        # Iterate through the list of phones
        for i, phone in enumerate(self.phones):
            if (
                phone.value == old_number
            ):  # Check if the current phone number matches the old number
                # Replace the old phone number with the new one
                self.phones[i] = Phone(new_number)
                found = True
                break  # Exit the loop once the phone number is updated
        # If the old phone number was not found, raise a KeyError
        if not found:
            raise KeyError(
                "The specified number does not exist or the contact has no phone numbers."
            )

    def find_phone(self, number):
        # Find a phone number in the record.
        for phone in self.phones:
            if phone.value == number:
                return phone

    def add_birthday(self, date):
        self.birthday = Birthday(date)
