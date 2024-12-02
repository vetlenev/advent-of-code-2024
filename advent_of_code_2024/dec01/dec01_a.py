def total_distance_deviation(a: list, b: list) -> int:
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    total_diff = 0
    for i in range(len(a)):
        total_diff += abs(a_sorted[i] - b_sorted[i])

    return total_diff

def read_lists_from_file(file_path: str) -> tuple:
    a = []
    b = []
    with open(file_path) as in_file:
        for line in in_file:
            ab_split = line.split()
            a.append(int(ab_split[0]))
            b.append(int(ab_split[1]))
        
    return a, b


if __name__ == "__main__":
    from pathlib import Path

    root = Path(__file__).parent.parent.parent
    file_path = root / "advent_of_code_2024" / "data" / "dec01.txt"

    a, b = read_lists_from_file(file_path)
        
    tot_diff = total_distance_deviation(a, b)

    print(f"Total distance deviation: {tot_diff}")