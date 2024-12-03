import numpy as np

def read_reports(file_path: str) -> tuple:
    reports = []
    with open(file_path) as file:
        for line in file.readlines():
            reports.append(line.split())
        
    return reports


def safe_reports(reports: list, problem_dampener: bool = False) -> tuple:
    num_safe = 0
    unsafe_reports = []
 
    for report in reports:
        report = np.array(report).astype(int)
        levels_diff = np.diff(report)

        is_safe = safe_criterias(levels_diff)

        if is_safe:
            num_safe += 1
        elif len(report) <= 2:
            # Removing one will always yield safe report
            num_safe += 1
        elif problem_dampener:
            num_safe += process_unsafe_reports([report], already_removed=False)

    return num_safe, unsafe_reports


def process_unsafe_reports(reports: list, already_removed: bool) -> int:
    for report in reports:
        levels_diff = np.diff(report)
        is_safe = safe_criterias(levels_diff)

        if is_safe:
            return 1
        
        elif already_removed:
            # If we have already removed one level, we can't remove another, skip to next report
            continue

        # There are three scenarios where we can remove one level to make the report safe

        new_reports = []
        for idx_to_remove in range(len(report)):
            new_report = np.delete(report, idx_to_remove)
            new_reports.append(new_report)
        return process_unsafe_reports(new_reports, already_removed=True)

    # All other scenarios can  be skipped - swapping any two levels will not satifsy safety criterias
    return 0


def safe_criterias(levels_diff: np.array) -> bool:
    all_increase = all(levels_diff > 0)
    all_decrease = all(levels_diff < 0)
    monotonic = all_increase or all_decrease

    at_least_one = all(abs(levels_diff) >= 1)
    at_most_three = all(abs(levels_diff) <= 3)

    return monotonic and at_least_one and at_most_three


if __name__ == "__main__":
    from pathlib import Path

    root = Path(__file__).parent.parent
    file_path = root / "advent_of_code_2024" / "data" / "dec02.txt"

    reports = read_reports(file_path)

    num_safe, unsafe_reports = safe_reports(reports, problem_dampener=True)

    print(f"Number of safe reports: {num_safe}")