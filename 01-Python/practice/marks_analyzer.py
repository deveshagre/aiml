"""Starter exercise: student marks analyzer.

Complete the TODOs. Run with: python marks_analyzer.py
"""

def validate_marks(marks):
    """Return only numeric marks in the range 0 to 100."""
    # TODO: validate values and return a cleaned list
    raise NotImplementedError


def summarize(marks):
    """Return a dictionary with count, average, minimum and maximum."""
    # TODO: handle an empty list safely
    raise NotImplementedError


if __name__ == "__main__":
    raw_marks = [78, 92, 65, 81, 100]
    clean = validate_marks(raw_marks)
    print(summarize(clean))
