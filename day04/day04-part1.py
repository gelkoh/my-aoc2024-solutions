import re

def read_input():
    with open("day04-input.txt") as f:
        return f.readlines()

def get_xmas_count(word_search):
    xmas_count = 0

    for line in word_search:
        matches = re.findall("(?=XMAS)|(?=SAMX)", line)
        xmas_count += len(matches)

    transposed = ["".join(line) for line in zip(*word_search)]

    for line in transposed:
        matches = re.findall("(?=XMAS)|(?=SAMX)", line)
        xmas_count += len(matches)

    for line_idx in range(len(word_search) - 3):
        for letter_idx in range(len(word_search[0]) - 3):
            diagonal = (
                word_search[line_idx][letter_idx] + 
                word_search[line_idx + 1][letter_idx + 1] + 
                word_search[line_idx + 2][letter_idx + 2] + 
                word_search[line_idx + 3][letter_idx + 3]
            )

            if diagonal in ["XMAS", "SAMX"]:
                xmas_count += 1

        for letter_idx in range(3, len(word_search[0])):  # Start from 3 for backward diagonal
            backwards_diagonal = (
                word_search[line_idx][letter_idx] + 
                word_search[line_idx + 1][letter_idx - 1] + 
                word_search[line_idx + 2][letter_idx - 2] + 
                word_search[line_idx + 3][letter_idx - 3]
            )
            if backwards_diagonal in ["XMAS", "SAMX"]:
                xmas_count += 1

    return xmas_count

def main():
    word_search = read_input()

    xmas_count = get_xmas_count(word_search)

    print("XMAS count:", xmas_count)
    
if __name__ == "__main__":
    main()
