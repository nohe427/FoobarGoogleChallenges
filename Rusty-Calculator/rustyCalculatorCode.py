def answer(string):
    finalString = ""
    multi = 0
    add = 0
    while len(string) > 0:
        if len(string) > 2:
            fNum = string[0]
            op = string[1]
            if op == "*":
                multi = multi + 1
                finalString = finalString + fNum
            elif op == "+":
                add = add + 1
                word = ""
                i = 0
                while multi > i:
                    word = word + "*"
                    i = i +1
                finalString = finalString + fNum + str(word)
                multi = 0
            string = string[2:]
        elif len(string) == 2:
            op = string[0]
            fNum = string[1]
            if op == "*":
                multi = multi + 1
                finalString = finalString + fNum
            elif op == "+":
                add = add + 1
                while multi > i:
                    word = word + "*"
                    i = i +1
                finalString = finalString + fNum + str(word)
                multi = 0
            string = string[1:]
        elif len(string) == 1:
            fNum = string[0]
            finalString = finalString + fNum
            i=0
            word = ""
            while multi > i:
                word = word + "*"
                i = i +1
            finalString = finalString + str(word)
            i=0
            word = ""
            while add > i:
                word = word + "+"
                i = i +1
            string = ""
    finalString = finalString + str(word)
    return finalString
