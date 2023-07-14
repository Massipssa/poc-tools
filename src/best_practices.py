class Student:
    def __init__(self, first_name: str):
        self.first_name = first_name

    @property
    def get_name(self):
        return self.first_name