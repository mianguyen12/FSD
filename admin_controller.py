from models.student import Student
from models.subject import Subject
from models.database import Database

class AdminController:
    def __init__(self):
        self.db = Database()
        self.students = self.db.load_students()

    def show_all(self):
        return [
            f"{s.name} :: {s.id} --> Email: {s.email}"
            for s in self.students
        ] or ["< Nothing to Display >"]

    def group_by_grade(self):
        grade_groups = {}

        for student in self.students:
            for sub in student.subjects:
                entry = f"{student.name} :: {student.id} --> GRADE: {sub.grade} - MARK: {sub.mark:.2f}"
                grade_groups.setdefault(sub.grade, []).append(entry)

        return grade_groups or {"< Nothing to Display >": []}

    def partition_pass_fail(self):
        passed = []
        failed = []
        for s in self.students:
            avg = s.get_average()
            grade = self._grade_from_mark(avg)
            entry = f"{s.name} :: {s.id} --> GRADE: {grade} - MARK: {avg:.2f}"
            if s.is_pass():
                passed.append(entry)
            else:
                failed.append(entry)
        if not passed and not failed:
            return None, None
        return passed, failed
    
    def remove_by_id(self, student_id):
        before = len(self.students)
        self.students = [s for s in self.students if s.id != student_id]
        self.db.save_students(self.students)
        return len(self.students) < before

    def clear_all(self):
        self.students = []
        self.db.clear()
        return True

    def _grade_from_mark(self, mark):
        if mark >= 85:
            return "HD"
        elif mark >= 75:
            return "D"
        elif mark >= 65:
            return "C"
        elif mark >= 50:
            return "P"
        else:
            return "F"

# Ensures this module is treated as a package
__all__ = ['AdminController']
