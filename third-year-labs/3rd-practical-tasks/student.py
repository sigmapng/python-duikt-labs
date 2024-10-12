class Student:

    def __init__(self, name, date_of_birth, group):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__group = group

    @property
    def name(self):
        return self.__name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def group(self):
        return self.__group
