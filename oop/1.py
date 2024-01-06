"""Object-oriented Programming basics."""

class Person:
    """Person class."""
    def __init__(self, first_name, last_name, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_first_name(self):
        """Method returns first name of a person."""
        return self.first_name
    
    def get_full_name(self):
        """Method returns full name of a person."""
        return f"{self.first_name} {self.last_name}"
    
    def get_age(self):
        """Method returns age of a person."""
        return self.age


person = Person("Rayhon", "Jalolova", 16)
print(person.get_age())