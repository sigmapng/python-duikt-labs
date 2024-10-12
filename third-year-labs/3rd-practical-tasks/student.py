class Student:

    def __init__(self, name, date_of_birth, group):
        self._name = name
        self._date_of_birth = date_of_birth
        self._group = group

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, value):
        self._group = value
