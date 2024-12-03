import re

def read_input():
    with open("day03-input.txt") as f:
        return f.read()

def get_sum(memory):
    sum = 0

    muls = re.findall(r"mul\((\d{1,3},\d{1,3})\)", memory)

    for mul in muls:
        a, b = mul.split(",")
        sum += int(a) * int(b)

    return sum

def main():
    memory = read_input()

    sum = get_sum(memory)

    print("Sum of multiplications:", sum)
    
if __name__ == "__main__":
    main()
