#data_loader.py

import json #For json files
import os #For file path operations
from typing import Dict # For type annotations
from models import Employee, Course, Role # Importing our key data models

# Indicating where our data files are located
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


# This function loads a JSON file from the data directory.
def _load_json(filename: str):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find {filename} in data directory: {DATA_DIR}. "
            f"Please create the file. See README for details"
        )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


#This function loads employees from a JSON file and returns a dictionary of Employee objects keyed by their IDs.
def load_employees() -> Dict[str, Employee]:
    #Loading json file
    raw = _load_json("employees.json")
    #Initialize empty dictionary for employees
    employees: Dict[str, Employee] = {}
    #For every item in the raw data, create Employee object and add to dictionary (repeat for other data)
    for item in raw:
        emp = Employee.from_dict(item)
        employees[emp.id] = emp
    return employees


#This function loads courses from a JSON file and returns a dictionary of Course objects keyed by their IDs.
def load_courses() -> Dict[str, Course]:
    raw = _load_json("courses.json")
    courses: Dict[str, Course] = {}
    for item in raw:
        course = Course.from_dict(item)
        courses[course.id] = course
    return courses


#This function loads roles from a JSON file and returns a dictionary of Role objects keyed by their IDs.
def load_roles() -> Dict[str, Role]:
    raw = _load_json("roles.json")
    roles: Dict[str, Role] = {}
    for item in raw:
        role = Role.from_dict(item)
        roles[role.id] = role
    return roles
