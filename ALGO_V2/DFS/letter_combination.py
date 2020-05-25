# https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description?_from=ladder&&fromId=1

KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


# example: digits: 234
def letter_combinations(digits):
    if not digits:
        return []
    results = []
    dfs(digits, 0, "", results)
    return results


def dfs(digits, index, string, results):
    if index >= len(digits):
        results.append(string)
        return
    print(digits[index], results)
    for letter in KEYBOARD[digits[index]]:
        print(letter, string)
        dfs(digits, index+1, string+letter, results)

r = letter_combinations("345")
print(r)