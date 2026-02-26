# Contains a physical address

class Address:
    # Constructor
    COUNTRY = "USA" # We only serve the US
    def __init__(self, street: str, city: str, state: str, zip_code: int):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    # Setters
    def set_street(self, street: str):
        self.__street = street

    def set_city(self, city: str):
        self.__city = city

    def set_state(self, state: str):
        self.__state = state

    def set_zip(self, zip_code: str):
        self.__zip = zip_code

    # Getters
    def get_street(self):
        return self.__street

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip

    # String overload
    def __str__(self):
        return f"{self.__street}, {self.__city}, {self.__state} {self.__zip}"