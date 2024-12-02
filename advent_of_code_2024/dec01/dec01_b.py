import numpy as np

def similarity_score(a: list, b: list) -> int:
    a = np.array(a)
    b = np.array(b)

    tot_score = 0
    for left in a:
        in_right = left == b
        num_in_right = np.sum(in_right)
        tot_score += left * num_in_right

    return tot_score


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

    left, right = read_lists_from_file(file_path)

    sim_score = similarity_score(left, right)

    print(f"Similarity score: {sim_score}")