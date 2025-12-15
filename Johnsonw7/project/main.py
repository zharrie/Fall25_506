# main.py

"""
Main entry point for the Employee Training Recommendation System.
"""
#Optional is used for type hinting to indicate that a variable can either be of a specified type or be None.
from typing import Optional

# These functions load data from JSON files into dictionaries of Employee, Course, and Role objects.
from data_loader import load_employees, load_courses, load_roles

# The TrainingRecommender class includes the recommendation logic and algorithms 
#as well as methods for analyzing skill gaps and listing entities.
from recommender import TrainingRecommender

#Importing the main recommender system class
from recommender import TrainingRecommender

# Function to print employee details
def print_employee(emp) -> None:
    print(f"\nEmployee {emp.id} – {emp.name}")
    # If the employee has skills, print them sorted and joined by commas
    if emp.skills:
        print("Skills:", ", ".join(sorted(emp.skills)))
    # Else, indicate that no skills are listed
    else:
        print("Skills: (none listed)")


# Function to print role details
def print_role(role) -> None:
    # Print role ID and name
    print(f"\nRole {role.id} – {role.name}")
    # If the role has required skills, print them sorted and joined by commas
    if role.required_skills:
        print("Required skills:", ", ".join(sorted(role.required_skills)))
    # Else, indicate that no required skills are listed
    else:
        print("Required skills: (none listed)")


# Function to print course recommendations
def print_recommendations(label: str, recs) -> None:
    # Indicate which algorithm's recommendations are being printed
    print(f"\n{label} recommendations:")
    # If no recommendations, indicate that no courses were found
    if not recs:
        print("  No courses found that address the missing skills.")
        return
    # Else, print each recommended course with its details
    # idx is the rank of the recommendation
    # course is the Course object
    # score is the number of missing skills the course addresses

    # Iterate through the recommendations with an index starting from 1
    # Print the course ID, title, skills taught, and score
    # Format the skills taught as a sorted, comma-separated string
    # Print each recommendation in a readable format

    # Example output:
    #  1. C01 – De-escalation and Conflict Resolution
    #     Skills taught: communication, conflict_resolution
    #     Missing skills addressed: 2
    for idx, (course, score) in enumerate(recs, start=1):
        # Display course details and skills it teaches with commas separating them
        skills_str = ", ".join(sorted(course.skills))
        print(f"  {idx}. {course.id} – {course.title}")
        print(f"     Skills taught: {skills_str}")
        print(f"     Missing skills addressed: {score}")


# Function to choose an employee by ID
# Returns the chosen employee ID or None if cancelled
#system: TrainingRecommender - tells you to input an instance of  TrainingRecommender 
# -> symbol is part of Python’s type hinting (annotation) syntax
# So here, this means: “This function returns an Optional[str]
def choose_employee(system: TrainingRecommender) -> Optional[str]:
    # Display available employees 
    # The \n at the start creates a new line for each employee listing
    print("\nAvailable employees:")
    # Iterate through all employees and print their ID and name
    for emp in system.list_employees():
        print(f"  {emp.id}: {emp.name}")
    # Prompt user to enter an employee ID
    emp_id = input("Enter employee ID (or 'cancel' to go back): ").strip()
    # If user types 'cancel', return None
    if emp_id.lower() == "cancel":
        return None
    # If entered ID is not found, inform the user and return None
    if emp_id not in system.employees:
        print("Employee ID not found.")
        return None
    # Else, return the valid employee ID
    return emp_id

# Function to choose a role
def choose_role(system: TrainingRecommender) -> Optional[str]:
    # Display available roles
    print("\nAvailable roles:")
    # Iterate through all roles and print their ID and name
    for role in system.list_roles():
        print(f"  {role.id}: {role.name}")
    # Prompt user to enter a role ID
    role_id = input("Enter role ID (or 'cancel' to go back): ").strip()
    # If user types 'cancel', return None
    if role_id.lower() == "cancel":
        return None
    # If entered ID is not found, inform the user and return None
    if role_id not in system.roles:
        print("Role ID not found.")
        return None
    # Else, return the valid role ID
    return role_id


# This function prints the training path found in the graph in a more readable format.
def pretty_print_path(
    path_nodes,
    system: TrainingRecommender,
    role,
) -> None:
    """
    Turn a list of node IDs like
        ["skill:conflict_resolution", "course:C01", "role:R01"]
    into a readable narrative.
    """
    # If no path nodes are provided, indicate that no path was found
    if not path_nodes:
        print("  (no path found)")
        return
    print("  Path:")
    # Iterate through each node in the path
    for node in path_nodes:
        if node.startswith("skill:"):
            # Extract the skill name from the node ID:
            # Split node at the first colon and store everything after it in skill_name
            skill_name = node.split(":", 1)[1]
            # Formats the skills nicely
            print(f"    Skill needed: {skill_name}")
        
        # Else if the node represents a course
        elif node.startswith("course:"):
            # Extract the course ID from the node ID
            course_id = node.split(":", 1)[1]
            # Look up the course object using the course ID
            course = system.courses.get(course_id)
            # If the course is found, print its details
            if course:
                skills_str = ", ".join(sorted(course.skills))
                print(f"    Course {course.id}: {course.title}")
                print(f"      (teaches: {skills_str})")
            # Else, indicate that the course is unknown
            else:
                print(f"    Course {course_id}: [unknown in data]")
        # Else if the node represents the role:
        elif node.startswith("role:"):
            # Extract the role ID from the node ID
            # We already have the role object, but node still encodes its ID.
            print(f"    Target role: {role.name}")


# Main function to run the recommendation system
# This function handles user interaction and orchestrates the recommendation process.
def main():
    print("=== Employee Training Recommendation System ===")
# Try to load data files and handle missing files
    try:
        employees = load_employees()
        courses = load_courses()
        roles = load_roles()
    except FileNotFoundError as e:
        print("\nERROR:", e)
        print("Make sure your JSON data files are created as described in the README file.")
        return

    # Initialize the recommendation system with loaded data of employees, courses, and roles
    system = TrainingRecommender(employees, courses, roles)

    # Main interaction loop
    # Display menu options and handle user choices
    # The loop continues until the user chooses to exit
    # Each menu option corresponds to a specific functional area of the system
    while True:
        print("\nMain Menu:")
        print("  1. View employee profile")
        print("  2. Analyze skill gaps for a target role")
        print("  3. Get training recommendations")
        print("  4. Compare recommendation algorithms (naive vs indexed)")
        print("  5. Compare sorting algorithms (built-in vs selection sort)")
        print("  6. List all courses")
        print("  7. Show graph-based training paths for missing skills")
        print("  8. Exit")

       # User will input their choice
        choice = input("Choose an option: ").strip()
        # Handle each menu option based on user input
        if choice == "1":
            emp_id = choose_employee(system)
            if emp_id:
                emp = system.get_employee(emp_id)
                print_employee(emp)

        elif choice == "2":
            emp_id = choose_employee(system)
            if not emp_id:
                continue
            role_id = choose_role(system)
            if not role_id:
                continue

            # Get the employee and role objects based on the chosen IDs
            # emp_id and role_id were defined in the choose_employee and choose_role functions earlier 
            #role is an instance of Role class defined in models.py
            emp = system.get_employee(emp_id)
            role = system.get_role(role_id)
            print_employee(emp)
            print_role(role)

            gaps = system.analyze_gaps(emp, role)
            # If there are no gaps in skills, inform the user
            if not gaps:
                print("\nThis employee already meets all required skills for this role!")
            else:
                print("\nMissing skills for this role:")
                # Print each missing skill sorted alphabetically. gaps was defined earlier as a set of strings
                print("  " + ", ".join(sorted(gaps)))

        elif choice == "3":
            emp_id = choose_employee(system)
            # If no employee ID is chosen, skip to the next iteration of the loop
            #This allows the user to cancel the operation if needed.
            if not emp_id:
                continue
            role_id = choose_role(system)
            # If no role ID is chosen, skip to the next iteration of the loop
            # Like above, this allows the user to cancel the operation if needed.
            if not role_id:
                continue


            emp = system.get_employee(emp_id)
            role = system.get_role(role_id)
            gaps = system.analyze_gaps(emp, role)

            print_employee(emp)
            print_role(role)

            if not gaps:
                print("\nNo missing skills – no training needed for this role.")
                continue

            print("\nMissing skills:", ", ".join(sorted(gaps)))
            # try to get user input for number of top recommendations
            # If input is invalid, default to 5
            try:
                top_n = int(input("How many top course recommendations do you want? (e.g., 5): ").strip())
            except ValueError:
                top_n = 5

            results = system.recommend(gaps, top_n=top_n)
            print_recommendations("Naive", results["naive"])
            print_recommendations("Indexed", results["indexed"])

        elif choice == "4":
            emp_id = choose_employee(system)
            if not emp_id:
                continue
            role_id = choose_role(system)
            if not role_id:
                continue

            emp = system.get_employee(emp_id)
            role = system.get_role(role_id)
            gaps = system.analyze_gaps(emp, role)

            if not gaps:
                print("\nNo missing skills – algorithm comparison would be trivial.")
                continue

            results = system.compare_algorithms(gaps, repeats=200)
            print("\nAlgorithm comparison (average seconds over 200 runs):")
            print(f"  Naive:   {results['avg_naive_seconds']:.8f} s")
            print(f"  Indexed: {results['avg_indexed_seconds']:.8f} s")

        elif choice == "5":
            emp_id = choose_employee(system)
            if not emp_id:
                continue
            role_id = choose_role(system)
            if not role_id:
                continue

            emp = system.get_employee(emp_id)
            role = system.get_role(role_id)
            gaps = system.analyze_gaps(emp, role)

            if not gaps:
                print("\nNo missing skills – sorting comparison would be trivial.")
                continue

            results = system.compare_sorts(gaps, top_n=10, repeats=200)
            print("\nSorting comparison (average seconds over 200 runs):")
            print(f"  Built-in sort:   {results['avg_builtin_seconds']:.8f} s")
            print(f"  Selection sort:  {results['avg_selection_seconds']:.8f} s")

        elif choice == "6":
            print("\nAll courses:")
            for course in system.list_courses():
                print(f"  {course.id}: {course.title} (difficulty: {course.difficulty})")
                if course.skills:
                    print("     Skills taught:", ", ".join(sorted(course.skills)))
                else:
                    print("     Skills taught: (none listed)")

        elif choice == "7":
            # Graph-based training paths for missing skills
            # We chose graphs because they allow us to find paths from missing skills to courses that teach them
            # The graph structure enables efficient traversal and pathfinding algorithms to recommend training paths.
            # The paths help visualize how taking certain courses can bridge the gap between an employee's current skills and the skills required for a role.
            # This approach provides a clear and structured way to recommend training based on skill gaps.
            # It also allows for flexibility in adding new courses or skills in the future.
    
            emp_id = choose_employee(system)
            if not emp_id:
                continue
            role_id = choose_role(system)
            if not role_id:
                continue

            emp = system.get_employee(emp_id)
            role = system.get_role(role_id)
            gaps = system.analyze_gaps(emp, role)

            print_employee(emp)
            print_role(role)

            if not gaps:
                print("\nNo missing skills – no training paths needed.")
                continue

            print("\nMissing skills:", ", ".join(sorted(gaps)))
            print("\nGraph-based training paths:")
            for skill in sorted(gaps):
                print(f"\nFor missing skill: {skill}")
                path = system.get_training_path_for_skill(skill, role)
                if path is None:
                    print("\nNo training path found in the current course options. Contact your supervisor to suggest additional options!")
                else:
                    pretty_print_path(path, system, role)
        elif choice == "8":
                    print("\nGoodbye!")
                    break
        else:
            print("Invalid choice. Please choose a number from the menu.")

# Run the main function when this script is executed,
# don't run it if imported as a module.
if __name__ == "__main__":
    main()