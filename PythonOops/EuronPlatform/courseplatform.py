from exception import InvalidEmailError, CourseAssignmentError, SubmissionError
from logging import logger

class User:
    # Class Variable to keep tabs on global user sign-ups
    total_users_count = 0

    def __init__(self, name: str, email: str, user_id: str):
        if not self.validate_email(email):
            logger.error(f"Failed to create user. Invalid Email format: {email}")
            raise InvalidEmailError(f"Email format '{email}' is invalid.")
            
        self.name = name
        self.email = email
        self.user_id = user_id
        
        # Increment tracking variable on every successful instantiation
        User.total_users_count += 1
        logger.debug(f"User {self.name} created. Total global registered users: {User.total_users_count}")

    # Instance Method
    def get_details(self) -> str:
        return f"ID: {self.user_id} | Name: {self.name} | Email: {self.email}"

    # Static Method
    @staticmethod
    def validate_email(email: str) -> bool:
        """Simple syntax verification for user profile construction safely."""
        return "@" in email and "." in email

    # Class Method
    @classmethod
    def get_total_users(cls) -> int:
        """Returns the complete registry metrics."""
        return cls.total_users_count


class Student(User):
    def __init__(self, name: str, email: str, user_id: str):
        # Call base constructor
        super().__init__(name, email, user_id)
        self.course_name = "Not Assigned"
        self.completed_assignments = []

    # Instance Method
    def assign_course(self, course: str):
        if not course or len(course.strip()) == 0:
            raise CourseAssignmentError("Course title cannot be empty.")
        self.course_name = course
        logger.info(f"Course '{course}' successfully assigned to Student: {self.name}")

    # Instance Method
    def submit_assignment(self, assignment_title: str):
        if self.course_name == "Not Assigned":
            raise SubmissionError(f"Cannot submit assignment. Student {self.name} is not enrolled in a course.")
        if not assignment_title:
            raise SubmissionError("Assignment title cannot be empty.")
            
        self.completed_assignments.append(assignment_title)
        logger.info(f"Assignment '{assignment_title}' submitted by Student: {self.name}")

    # Overridden Instance Method
    def get_details(self) -> str:
        base_details = super().get_details()
        assignments_str = ", ".join(self.completed_assignments) if self.completed_assignments else "None"
        return f"[Student] {base_details} | Course: {self.course_name} | Submissions: [{assignments_str}]"


class Mentor(User):
    def __init__(self, name: str, email: str, user_id: str, expertise: str):
        super().__init__(name, email, user_id)
        self.expertise = expertise
        self.assigned_students_count = 0

    # Instance Method
    def update_student_allocation(self, count: int):
        if count < 0:
            raise ValueError("Student allocation counts cannot drop below zero boundaries.")
        self.assigned_students_count = count
        logger.info(f"Mentor {self.name}'s batch updated to {self.assigned_students_count} students.")

    # Overridden Instance Method
    def get_details(self) -> str:
        base_details = super().get_details()
        return f"[Mentor] {base_details} | Expertise: {self.expertise} | Supervised Candidates: {self.assigned_students_count}"