from dataclasses import dataclass, field
from typing import List, Set, Dict


@dataclass
# @dataclass is something that automatically adds special methods to the class, 
#like __init__() and __repr__(), based on the class attributes.
# It is used here to simplify the creation of data classes for Employee, Course, and Role.
# Here for Employee, it defines the attributes id, name, and skills.
# skills is initialized as an empty set by default using field(default_factory=set).
# This is useful for ensuring that each instance of Employee has its own set of skills
class Employee:
    id: str
    name: str
    skills: Set[str] = field(default_factory=set) #default_factory=set creates a new set for each instance

    @classmethod
    #classmethod is a method that is bound to the class and not the instance of the class
    # Here, it is used to create an Employee instance from a dictionary.
    # It processes the skills to ensure they are stored as a set of lowercase strings.
    # This is useful for consistent skill representation.
    # It helps in avoiding duplicates and makes skill comparisons easier.
    # The from_dict method is a common pattern for creating instances from data structures like dictionaries.
    def from_dict(cls, data: Dict) -> "Employee":
        # Skills are tranformed from a list to a set to ensure uniqueness and allow set operations
        skills = set(skill.strip().lower() for skill in data.get("skills", []))
        return cls(
            id=str(data.get("id")),
            name=str(data.get("name")),
            skills=skills,
        )

@dataclass
class Course:
    id: str
    title: str
    skills: Set[str] = field(default_factory=set)
    difficulty: str = "unspecified"

    @classmethod
    def from_dict(cls, data: Dict) -> "Course":
        skills = set(skill.strip().lower() for skill in data.get("skills", []))
        return cls(
            id=str(data.get("id")),
            title=str(data.get("title")),
            skills=skills,
            difficulty=str(data.get("difficulty", "unspecified")),
        )


@dataclass
class Role:
    id: str
    name: str
    required_skills: Set[str] = field(default_factory=set)

    @classmethod
    def from_dict(cls, data: Dict) -> "Role":
        required_skills = set(skill.strip().lower() for skill in data.get("required_skills", []))
        return cls(
            id=str(data.get("id")),
            name=str(data.get("name")),
            required_skills=required_skills,
        )
