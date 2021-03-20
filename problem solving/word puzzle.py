def recur(n, grid, word, i, j, k, prev=""):
    if k >= len(word):
        return 1
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0
    if (grid[i][j] != word[k]):
        return 0

    if k == 0:
        return (recur(n, grid, word, i - 1, j, k + 1, "top") +
                recur(n, grid, word, i, j - 1, k + 1, "left") +
                recur(n, grid, word, i + 1, j, k + 1, "bottom") +
                recur(n, grid, word, i, j + 1, k + 1, "right") +

                recur(n, grid, word, i - 1, j - 1, k + 1, "topleft") +
                recur(n, grid, word, i - 1, j + 1, k + 1, "topright") +
                recur(n, grid, word, i + 1, j - 1, k + 1, "bottomleft") +
                recur(n, grid, word, i + 1, j + 1, k + 1, "bottomright")
                )
    else:
        if prev == "top":
            return recur(n, grid, word, i - 1, j, k + 1, prev)
        if prev == "left":
            return recur(n, grid, word, i, j - 1, k + 1, prev)
        if prev == "bottom":
            return recur(n, grid, word, i + 1, j, k + 1, prev)
        if prev == "right":
            return recur(n, grid, word, i, j + 1, k + 1, prev)
        if prev == "topleft":
            return recur(n, grid, word, i - 1, j - 1, k + 1, prev)
        if prev == "topright":
            return recur(n, grid, word, i - 1, j + 1, k + 1, prev)
        if prev == "bottomleft":
            return recur(n, grid, word, i + 1, j - 1, k + 1, prev)
        if prev == "bottomright":
            return recur(n, grid, word, i + 1, j + 1, k + 1, prev)


def countOccurrence(n, grid, word):  # n is the number of rows/columns in the grid, grid contains all the characters.
    # word is the given input string whose number of occurrences has to be found.
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == word[0]:
                temp = recur(n, grid, word, i, j, 0)
                count += temp
    return count


def main():
    n = int(input())
    grid = []
    for i in range(n):
        x = input()
        grid.append(x)
    word = input()
    print(countOccurrence(n, grid, word))


main()
