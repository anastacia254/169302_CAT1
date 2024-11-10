class Student:
    def __init__(this, name, student_id):
        this.name = name
        this.student_id = student_id
        this.assignments = {}

    def add_assignment(this, assignment_name, grade):
        """Add an assignment and grade to the student's record."""
        this.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {this.name}.")

    def display_grades(this):
        """Display all assignments and grades."""
        print(f"Grades for {this.name}:")
        if this.assignments:
            for assignment, grade in this.assignments.items():
                print(f"{assignment}: {grade}")
        else:
            print("No assignments recorded.")


class Instructor:
    def __init__(this, name, course_name):
        this.name = name
        this.course_name = course_name
        this.students = []

    def add_student(this, student):
        """Add a student to the course."""
        if student not in this.students:
            this.students.append(student)
            print(f"Added student {student.name} (ID: {student.student_id}) to {this.course_name}.")
        else:
            print(f"{student.name} is already enrolled in the course.")

    def assign_grade(this, student_id, assignment_name, grade):
        """Assign a grade to a specific student."""
        student = next((s for s in this.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found.")

    def display_all_students_grades(this):
        """Display all students and their grades."""
        print(f"Grades for all students in {this.course_name}:")
        if this.students:
            for student in this.students:
                student.display_grades()
        else:
            print("No students enrolled.")


# Interactive code for instructor to add students and assign grades

# Create an instructor
instructor = Instructor("Dr.Muya", "Computer Science 3101")

while True:
    print("\nCourse Management System")
    print("1. Add a student")
    print("2. Assign a grade to a student")
    print("3. Display all students and their grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        student = Student(student_name, student_id)
        instructor.add_student(student)

    elif choice == "2":
        student_id = input("Enter student ID to assign a grade: ")
        assignment_name = input("Enter assignment name: ")
        grade = input("Enter grade: ")
        try:
            grade = float(grade)
            instructor.assign_grade(student_id, assignment_name, grade)
        except ValueError:
            print("Invalid grade. Please enter a numeric value.")

    elif choice == "3":
        instructor.display_all_students_grades()

    elif choice == "4":
        print("Exiting the course management system.")
        break

    else:
        print("Invalid choice, please try again.")
