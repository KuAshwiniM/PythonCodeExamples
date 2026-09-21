from courseplatform import User, Student, Mentor
from exception import LearningPlatformError
from logging import logger

def run_platform_demo():
    logger.info("--- Initializing Super30 Platform System Workspace ---")
    
    # Track multiple objects locally
    students_registry = []
    mentors_registry = []

    # 1. Register Users inside error checking frameworks
    try:
        # Creating Students
        s1 = Student("Anand Kumar", "anand@super30.org", "STU101")
        s2 = Student("Ramanujan S.", "ramanujan@math.edu", "STU102")
        students_registry.extend([s1, s2])
        
        # Creating a Mentor
        m1 = Mentor("Prof. Mukherjee", "mukherjee@super30.org", "MNT201", "Advanced Mathematics & Calculus")
        mentors_registry.append(m1)
        
    except LearningPlatformError as e:
        logger.error(f"Initialization Registry Interrupted: {e}")

    # 2. Operations & Exception Handling Showcase
    print("\n--- Platform Operations Execution ---")
    try:
        # Triggering operational pipelines
        s1.assign_course("Data Structures & Algorithms")
        s1.submit_assignment("Binary Trees Assignment 1")
        s1.submit_assignment("Graph Theory Hackathon")
        
        s2.assign_course("Quantum Electrodynamics")
        # Trying to update Mentor Allocation details
        m1.update_student_allocation(15)
        
        # Intentionally triggering a tracked framework exception (Enrolling in empty course)
        print("\n* Attempting Invalid Operation (Empty Course Assignment):")
        s2.assign_course("")
        
    except LearningPlatformError as e:
        logger.warning(f"Handled expected workspace rule exception: {e}")

    try:
        # Intentionally triggering a static method runtime exception (Invalid Email configuration)
        print("\n* Attempting Invalid User Registration:")
        faulty_student = Student("Wrong Email Guy", "bad_email_format", "STU404")
    except LearningPlatformError as e:
        logger.warning(f"Handled expected validation layout exception: {e}")

    # 3. Reading and Aggregating Platform Metadata Logs
    print("\n--- Displaying Platform Profiles ---")
    for student in students_registry:
        print(student.get_details())
        
    for mentor in mentors_registry:
        print(mentor.get_details())

    # 4. Accessing Static and Class Methods directly
    print("\n--- Platform Global Analytics Counters ---")
    # Fetching counter value directly via Class Method
    total_active_profiles = User.get_total_users()
    print(f"Total instantiated profile instances registered (Class Method Check): {total_active_profiles}")
    
    # Validating standalone structures with Static Method without mapping instances
    email_check = User.validate_email("test@platform.com")
    print(f"Is 'test@platform.com' valid format structural layout? (Static Method Check): {email_check}")

    logger.info("--- Super30 Platform Demonstration Pipeline Closed Safely ---")

if __name__ == "__main__":
    run_platform_demo()