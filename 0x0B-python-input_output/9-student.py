#!/usr/bin/python3
"""This is a class defination of Student."""


class Student:
    """This is the definition of the class."""

    def __init__(self, first_name, last_name, age):
        """
        The intialization of the class Student


        Args:
            first_name: first_name of student
            last_name: last_name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This code retrieves a dictionary representation of a Student."""

        return(vars(self))
