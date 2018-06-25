import itertools


def lettersCombinations(digits):

    buttons = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]

    }

    digits = list(digits)
    letters = []
    results = []

    if len(digits) == 0:
        return []
    elif len(digits) == 1:
        return buttons[int(digits[0])]
    else:
        for x in digits:
            letters.append(buttons[int(x)])

        for i in itertools.product(*letters):
            results.append(''.join(i))

        return results
