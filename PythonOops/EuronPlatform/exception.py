class LearningPlatformError(Exception):
    """Base Exception rule for the Super30 platform errors."""
    pass

class InvalidEmailError(LearningPlatformError):
    """Raised when an invalid email layout is provided."""
    pass

class CourseAssignmentError(LearningPlatformError):
    """Raised when course updates conflict or encounter operational issues."""
    pass

class SubmissionError(LearningPlatformError):
    """Raised when an assignment submission criteria isn't met."""
    pass