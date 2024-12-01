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

def sum_of_id_differences(sorted_left_ids, sorted_right_ids):
    sum = 0

    for left_id, right_id in zip(sorted_left_ids, sorted_right_ids):
        sum += abs(left_id - right_id)

    return sum

def main():
    lines = read_input()
    left_ids, right_ids = parse_lines(lines)

    # Sort by ID asc
    sorted_left_ids, sorted_right_ids = (sorted(left_ids), sorted(right_ids))

    sum = sum_of_id_differences(sorted_left_ids, sorted_right_ids)

    print("Sum:", sum)
    
if __name__ == "__main__":
    main()
