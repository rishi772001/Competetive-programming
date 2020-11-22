# https://leetcode.com/problems/word-search/

def search(board, word, start, index = 1):

    if index >= len(word):
        return True
    if start[0] < 0 or start[1] < 0 or start[0] >= len(board) or start[1] >= len(board[0]):
        return False


    if start[0]>=0 and start[1]+1>=0 and start[0]<len(board) and start[1]+1<len(board[0]) and board[start[0]][start[1] + 1] == word[index]:
        board[start[0]][start[1]] = "0"
        start = [start[0], start[1] + 1]

        if search(board, word, start, index + 1):
            return True
        else:
            start = [start[0], start[1] - 1]
            board[start[0]][start[1]] = word[index - 1]     # BACKTRACK

    if start[0]+1>=0 and start[1]>=0 and start[0]+1<len(board) and start[1]<len(board[0]) and board[start[0] + 1][start[1]] == word[index]:

        board[start[0]][start[1]] = "0"
        start = [start[0] + 1, start[1]]
        if search(board, word, start, index + 1):
            return True
        else:
            start = [start[0] - 1, start[1]]
            board[start[0]][start[1]] = word[index - 1]

    if start[0]>=0 and start[1]-1>=0 and start[0]<len(board) and start[1]-1<len(board[0]) and board[start[0]][start[1] - 1] == word[index]:
        board[start[0]][start[1]] = "0"
        start = [start[0], start[1] - 1]
        if search(board, word, start, index + 1):
            return True
        else:
            start = [start[0], start[1] + 1]
            board[start[0]][start[1]] = word[index - 1]


    if start[0]-1>=0 and start[1]>=0 and start[0]-1<len(board) and start[1]<len(board[0]) and board[start[0] - 1][start[1]] == word[index]:
        board[start[0]][start[1]] = "0"
        start = [start[0] - 1, start[1]]
        if search(board, word, start, index + 1):
            return True
        else:
            start = [start[0] + 1, start[1]]
            board[start[0]][start[1]] = word[index - 1]


    return False


def calc(words, main_board):
    output = list()

    for word in words:
        # board = list(main_board)
        board = []
        for i in main_board:
            temp = []
            for j in i:
                temp.append(j)
            board.append(temp)

        flag = False
        start = [0, 0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    start = [i, j]
                    if(search(board, word, start)):
                        output.append(word)
                        flag = True
                        break
            if flag:
                break
    return output



inp = [["a","a"]]
words =  ["a","a"]

print(calc(words, inp))



