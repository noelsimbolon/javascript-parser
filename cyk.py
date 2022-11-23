# contoh CNF dari PR 9
R = {
     "S": [["A","B"],["B","C"]],
     "A": [["B","A"],["a"]],
     "B": [["C","C"],["b"]],
     "C": [["A","B"],["a"]]
    }

def CYK(string, start_symbol):
    word = string.split(" ")
    nString = len(word)
    cykTable = [[set([]) for i in range(nString)] for j in range(nString)]

    for i in range(nString):
        for j in range(nString-i):
            if i == 0:
                for left,right in R.items():
                    for term in right:
                        if (len(term) == 1 and term[0] == word[j]):
                            cykTable[j][j].add(left)
            else:
                for k in range(i):
                    for left,right in R.items():
                        for term in right:
                            if (len(term) == 2 and term[0] in cykTable[j][k+j] and term[1] in cykTable[j+k+1][i+j]):
                                cykTable[j][i+j].add(left)

    if start_symbol in cykTable[0][nString-1]:
        return True
    else: 
        return False

# testing
test_string = input("Input string: ")
if (CYK(test_string, "S")):
    print(f"'{test_string}' is in languange")
else:
    print(f"'{test_string}' not in languange")


