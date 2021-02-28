'''
@Author: rishi
'''

text = "supreme court is the highest judicial court"
letters = "su"

ans = 0

i = 0
while i < len(text):
    if text[i] in letters:
        temp = text[i]
        while temp in letters:
            if i + 1 < len(text):
                i += 1
                temp += text[i]
            else:
                # calculate
                paste = 1
                backspace = len(letters) - (letters.index(temp) + len(temp))
                if i == len(text) - 1 and letters.index(temp):
                    mouse = (len(temp) * 2) + letters.index(temp) - 1
                elif letters.index(temp):
                    mouse = (len(temp) * 2) + letters.index(temp)
                else:
                    mouse = 0

                print(temp, paste, backspace, mouse)
                ans += paste + backspace + mouse

                i += 1
                break
        else:
            temp = temp[:-1]
            # calculate
            paste = 1
            backspace = len(letters) - (letters.index(temp) + len(temp))
            if i == len(text) - 1 and letters.index(temp):
                mouse = (len(temp) * 2) + letters.index(temp) - 1
            elif letters.index(temp):
                mouse = (len(temp) * 2) + letters.index(temp)
            else:
                mouse = 0

            print(temp, paste, backspace, mouse)
            ans += paste + backspace + mouse
    else:
        i += 1

print(ans)
