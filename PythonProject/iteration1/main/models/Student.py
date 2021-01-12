from typing import Any


class Student:

    def __init__(self, id, number, name, surname):
        self.id = id
        self.number = number
        self.name = name
        self.surname = surname
        self.setSmartFullName()
        self.setFullName()
        self.attancePercent = 0

    def __str__(self) -> str:
        string = """Student with number {number} , name {name} , surname {surname}""".format(number=self.number,
                                                                                             name=self.name,
                                                                                             surname=self.surname)
        return string

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSurname(self, surname):
        self.surname = id

    def getSurname(self):
        return self.surname

    def getAttancePercent(self):
        return self.attancePercent

    def setAttendancePercent(self, attancePercent):
        self.attancePercent = attancePercent


    def setSmartFullName(self):
        x = self.name.split(" ")[0]
        fullName = """{name}{surname}""".format(name=x,
                                                surname=self.surname.split(" ")[len(self.surname.split(" ")) - 1])
        self.smartFullName = fullName.lower()


    def setFullName(self):
        x = self.name.replace(" ", "")
        fullName = """{name}{surname}""".format(name=x,
                                                surname=self.surname)
        self.fullName = fullName.lower()

