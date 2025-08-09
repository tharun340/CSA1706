# --- Data Definitions ---

# subject_code: subject_name
subjects = {
    "cs101": "Computer Science",
    "ma102": "Mathematics",
    "ph103": "Physics"
}

# teacher_name: list of subject_codes
teachers = {
    "Dr. Smith": ["cs101"],
    "Prof. Lee": ["ma102"],
    "Dr. Jones": ["ph103"]
}

# student_name: list of subject_codes
students = {
    "John Doe": ["cs101"],
    "Jane Smith": ["ma102"],
    "Alice Walker": ["cs101"],
    "Bob Johnson": ["ph103"],
    "Susan Clark": ["ma102"]
}

# --- Functions ---

def subjects_of_student(student_name):
    if student_name not in students:
        print(f"{student_name} not found.")
        return
    print(f"\nSubjects taken by {student_name}:")
    for code in students[student_name]:
        subject_name = subjects.get(code, "Unknown Subject")
        print(f" - {subject_name} ({code})")

def students_of_teacher(teacher_name):
    if teacher_name not in teachers:
        print(f"{teacher_name} not found.")
        return
    print(f"\nStudents taught by {teacher_name}:")
    teacher_subjects = teachers[teacher_name]
    for student, subject_codes in students.items():
        for code in subject_codes:
            if code in teacher_subjects:
                subject_name = subjects.get(code, "Unknown Subject")
                print(f" - {student} in {subject_name} ({code})")

def teacher_of_student(student_name):
    if student_name not in students:
        print(f"{student_name} not found.")
        return
    print(f"\nTeachers of {student_name}:")
    for code in students[student_name]:
        subject_name = subjects.get(code, "Unknown Subject")
        found = False
        for teacher, subject_codes in teachers.items():
            if code in subject_codes:
                print(f" - {teacher} teaches {subject_name} ({code})")
                found = True
        if not found:
            print(f" - No teacher found for {subject_name} ({code})")

def subject_info(code):
    subject_name = subjects.get(code)
    if subject_name:
        print(f"\nSubject Code: {code}, Name: {subject_name}")
    else:
        print(f"\nSubject code '{code}' not found.")

# --- Example Usage ---

if __name__ == "__main__":
    subjects_of_student("Alice Walker")
    students_of_teacher("Prof. Lee")
    teacher_of_student("John Doe")
    subject_info("cs101")
