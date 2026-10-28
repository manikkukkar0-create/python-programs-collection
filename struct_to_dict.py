"""
Structure to Dictionary Conversion
Author: Manik Kukkar
University: JECRC University, Jaipur
Description: Demonstrates converting custom class objects and dataclasses to Python dictionaries.
"""

from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Course:
    course_code: str
    course_name: str
    credits: int

@dataclass
class Student:
    name: str
    roll_no: str
    semester: int
    cgpa: float
    courses: List[Course]

def convert_student_to_dict(student: Student) -> dict:
    """Convert dataclass structure to a nested Python dictionary."""
    return asdict(student)

class LegacyStudent:
    """Traditional Python class demonstrating custom dictionary serialization."""
    def __init__(self, name: str, roll_no: str, branch: str):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "branch": self.branch
        }

def main():
    print("=== Structure to Dictionary Conversion (Manik Kukkar) ===")
    student = Student(
        name="Manik Kukkar",
        roll_no="23BCSE010",
        semester=3,
        cgpa=8.0,
        courses=[
            Course("CS201", "Data Structures & Algorithms", 4),
            Course("CS202", "Web Development", 3),
            Course("CS203", "Python Programming", 3)
        ]
    )

    student_dict = convert_student_to_dict(student)
    print("Converted Dataclass to Dict:")
    import json
    print(json.dumps(student_dict, indent=2))

    legacy = LegacyStudent("Manik Kukkar", "23BCSE010", "Computer Science and Engineering")
    print("\nConverted Legacy Class to Dict:")
    print(legacy.to_dict())

if __name__ == "__main__":
    main()
