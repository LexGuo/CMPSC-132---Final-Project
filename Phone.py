# Contains phone information

class Phone:
    # Constructor
    def __init__(self, phone_number: str, phone_type: str):
        self.__number = phone_number
        self.__type = phone_type

    # Setters

    def set_number(self, phone_number: str):
        self.__number = phone_number

    def set_type(self, phone_type: str):
        self.__type = phone_type

    # Getters

    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    # String override
    def __str__(self):
        return f"{self.__number} ({self.__type})"