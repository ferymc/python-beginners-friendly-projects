from typing import Dict, Tuple


def analyze_students(
    grade: Dict[str, Dict[str, float]],
) -> Tuple[str, str, Dict[str, float]]:

    if not grade:
        raise ValueError("Data cannot be empty!")

    for name, lesson in grade.values():
        if not lesson:
            raise ValueError(f"no grade found for student {name}")
        
