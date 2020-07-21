class Choice:

    def __init__(self, string_representation: str, value):
        self.string_representation = string_representation
        self.value = value

    def __str__(self):
        return self.string_representation

    def __repr__(self):
        return f"Choice: {self.__str__()}"
