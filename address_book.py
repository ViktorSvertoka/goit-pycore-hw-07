from datetime import datetime, timedelta
from collections import UserDict
from constants import DATE_FORMAT


def is_weekend_day(day: int) -> bool:
    return day >= 5


class AddressBook(UserDict):
    # A simple address book implementation.
    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    def add_record(self, record):
        # Add a record to the address book.
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name: str):
        # Find a record by name.
        try:
            return self.data[name]
        except KeyError:
            raise KeyError(f"Record with name '{name}' not found.")

    def delete(self, name):
        # Delete a record by name.
        del self.data[name]

    def get_upcoming_birthdays(self):
        today_date = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday_date = record.birthday.value.replace(
                    year=today_date.year
                ).date()
                days_until_birthday = (birthday_date - today_date).days

                if 0 <= days_until_birthday <= 7:
                    if is_weekend_day(birthday_date.weekday()):
                        days_to_add = 2 if birthday_date.weekday() == 5 else 1
                        congratulation_date = birthday_date + timedelta(
                            days=days_to_add
                        )
                    else:
                        congratulation_date = birthday_date

                    upcoming_birthdays.append(
                        {
                            "name": name,
                            "congratulation_date": congratulation_date.strftime(
                                DATE_FORMAT
                            ),
                        }
                    )
                elif (
                    days_until_birthday < 0
                ):  # If birthday has already passed this year, calculate for next year
                    next_birthday_date = record.birthday.value.replace(
                        year=today_date.year + 1
                    ).date()
                    days_until_next_birthday = (next_birthday_date - today_date).days

                    if 0 <= days_until_next_birthday <= 7 and is_weekend_day(
                        next_birthday_date.weekday()
                    ):
                        days_to_add = 2 if next_birthday_date.weekday() == 5 else 1
                        congratulation_date = next_birthday_date + timedelta(
                            days=days_to_add
                        )
                        upcoming_birthdays.append(
                            {
                                "name": name,
                                "congratulation_date": congratulation_date.strftime(
                                    DATE_FORMAT
                                ),
                            }
                        )

        return upcoming_birthdays
