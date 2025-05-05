import random
from typing import List
from models.subject import Subject

class Student:
    def __init__(self, name, email, password, student_id=None, subjects=None):
        self.id = student_id or f"{random.randint(1, 999999):06d}"
        self.name = name
        self.email = email
        self.password = password
        self.subjects: List[Subject] = subjects or []

    def enrol_subject(self):
        if len(self.subjects) >= 4:
            return False, "Cannot enrol in more than 4 subjects."
        subject = Subject()  # mark & id are random
        self.subjects.append(subject)
        return True, f"Subject {subject.id} enrolled with mark {subject.mark} and grade {subject.grade}"

    def remove_subject(self, subject_id):
        before = len(self.subjects)
        self.subjects = [s for s in self.subjects if s.id != subject_id]
        return len(self.subjects) < before, "Subject removed." if len(self.subjects) < before else "Subject not found."

    def change_password(self, new_password):
        self.password = new_password

    def get_average(self):
        if not self.subjects:
            return 0
        return sum(s.mark for s in self.subjects) / len(self.subjects)

    def is_pass(self):
        return self.get_average() >= 50

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "subjects": [s.to_dict() for s in self.subjects]
        }

    @staticmethod
    def from_dict(data):
        subjects = [Subject.from_dict(s) for s in data.get("subjects", [])]
        return Student(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            student_id=data["id"],
            subjects=subjects
        )
def get_grade(self):
    avg = self.get_average()
    if avg >= 85:
        return "HD"
    elif avg >= 75:
        return "D"
    elif avg >= 65:
        return "C"
    elif avg >= 50:
        return "P"
    else:
        return "F"