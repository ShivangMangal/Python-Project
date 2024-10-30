class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade):
        student = Student(student_id, name, age, grade)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def display_students(self):
        if not self.students:
            print("No students added yet.")
        else:
            print("List of Students:")
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")

    def search_student(self, name):
        found = False
        for student in self.students:
            if student.name == name:
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
                found = True

        if not found:
            print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student with ID {student_id} deleted successfully!")
                return
        print("Student not found.")

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            sms.add_student(student_id, name, age, grade)
        elif choice == '2':
            sms.display_students()
        elif choice == '3':
            name = input("Enter Student Name to search: ")
            sms.search_student(name)
        elif choice == '4':
            student_id = int(input("Enter Student ID to delete: "))
            sms.delete_student(student_id)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
