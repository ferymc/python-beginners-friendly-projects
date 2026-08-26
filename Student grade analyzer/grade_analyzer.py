from typing import Dict, Tuple


def analyze_students(
    grade: Dict[str, Dict[str, float]],
) -> Tuple[str, str, Dict[str, float]]:

    if not grade:
        raise ValueError("Data cannot be empty!")

    for name, lessons in grade.items():

        if not lessons:
            raise ValueError(f"no grade found for student {name}")

        if any(not isinstance(value, (int, float)) for value in lessons.values()):
            raise ValueError(f"invalid grade detected for student {name}")

    average = {}

    for student, lessons in grade.items():
        average[student] = sum(lessons.values()) / len(lessons)

    best_student = max(average, key=average.get)
    worst_student = min(average, key=average.get)

    return best_student, worst_student, average


if __name__ == "__main__":

    students = {
        "ali": {"math": 18, "physics": 14},
        "sara": {"math": 20, "physics": 19},
        "zahra": {"math": 15, "physics": 12},
        "mahdi": {"math": 11, "physics": 10},
        "fery": {"math": 19, "physics": 20},
    }
    best, worst, grade_list = analyze_students(students)

    print(f"Best student is: {best}")
    print(f"Worst student is: {worst}")
    print(f"Grade list: {grade_list}")
