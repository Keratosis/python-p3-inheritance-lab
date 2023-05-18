#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Default knowledge"]

    def teach(self, information=None):
        if information is None:
            print("No information provided. Teaching cannot be performed.")
            return None
        self.knowledge.append(information)
        return information




T = Teacher("braxton","shaffie")
T.teach()
print(T.first_name,T.last_name)
print(T.knowledge)