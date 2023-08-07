#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = []

    def learn(self, lesson_learned):
        self.knowledge.append(lesson_learned)