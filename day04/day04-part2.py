import re

def read_input():
    with open("day04-input.txt") as f:
        return f.readlines()

def get_xmas_count(word_search):
    xmas_count = 0

    for line_idx in range(len(word_search) - 2):
        for letter_idx in range(len(word_search[0]) - 2):
            diagonal = (
                word_search[line_idx][letter_idx] + 
                word_search[line_idx + 1][letter_idx + 1] + 
                word_search[line_idx + 2][letter_idx + 2]
            )

            backwards_diagonal = (
                word_search[line_idx + 2][letter_idx] + 
                word_search[line_idx + 1][letter_idx + 1] + 
                word_search[line_idx][letter_idx + 2]
            )

            if diagonal in ["MAS", "SAM"] and backwards_diagonal in ("MAS", "SAM"):
                xmas_count += 1

    return xmas_count

def main():
    word_search = read_input()

    xmas_count = get_xmas_count(word_search)

    print("XMAS count:", xmas_count)
    
if __name__ == "__main__":
    main()
