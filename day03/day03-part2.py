import re

def read_input():
    with open("day03-input.txt") as f:
        return f.read()

def get_sum(memory):
    sum = 0
    is_on = True

    matches = re.finditer(r"(don't\(\)|do\(\)|mul\((\d{1,3},\d{1,3})\))", memory)

    for match in matches:
        instruction = match.group(0)

        if instruction == "don't()":
            is_on = False
        elif instruction == "do()":
            is_on = True
        elif "mul(" in instruction:
            if is_on:
                nums = instruction[4:-1]
                a, b = map(int, nums.split(","))
                sum += a * b

    return sum

def main():
    memory = read_input()

    sum = get_sum(memory)

    print("Sum of multiplications:", sum)
    
if __name__ == "__main__":
    main()
