from collections import Counter

def read_input():
    with open("day01-input.txt") as f:
        return f.readlines()

def parse_lines(lines):
    left_ids = []
    right_ids = []

    for line in lines:
        left_id, right_id = line.split()
        left_ids.append(int(left_id))
        right_ids.append(int(right_id))

    return left_ids, right_ids

def calculate_similary_score(left_ids, right_ids):
    similarity_score = 0

    right_ids_count = Counter(right_ids)

    for left_id in left_ids:
        num_of_occurrences_in_right_ids = right_ids_count.get(left_id, 0)

        similarity_score += left_id * num_of_occurrences_in_right_ids

    return similarity_score

def main():
    lines = read_input()
    left_ids, right_ids = parse_lines(lines)

    similarity_score = calculate_similary_score(left_ids, right_ids)

    print("Similarity score:", similarity_score)
    
if __name__ == "__main__":
    main()

