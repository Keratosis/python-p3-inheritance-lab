#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",]

    def teach(self):
        if self.knowledge:
            return self.knowledge[0]
        else:
            print("No information provided. Teaching cannot be performed.")



T = Teacher("braxton","shaffie")
T.teach()
print(T.first_name,T.last_name)
print(T.knowledge[3])