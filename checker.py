from automata.fa.dfa import DFA

# evaluasi VARIABEL dengan FA
check_variable = DFA(
    states={'q0','q1','q2'}
    input_symbols={'`','1','2','3','4','5','6','7','8','9','0','-','=',
                   'q','w','e','r','t','y','u','i','o','p','[',']',"\\",
                   'a','s','d','f','g','h','j','k','l',';',"'",
                   'z','x','c','v','b','n','m',',','.','/',
                   '~','!','@','#','$','%','^','&','*','(',')','_','+',
                   'Q','W','E','R','T','Y','U','I','O','P','{','}','|',
                   'A','S','D','F','G','H','J','K','L',':','"',
                   'Z','X','C','V','B','N','M','<','>','?',' '}
    transitions={
        'q0':  {'`': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2', '0': 'q2', '-': 'q2', '=': 'q2',
                'q': 'q1', 'w': 'q1', 'e': 'q1', 'r': 'q1', 't': 'q1', 'y': 'q1', 'u': 'q1', 'i': 'q1', 'o': 'q1', 'p': 'q1', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q1', 's': 'q1', 'd': 'q1', 'f': 'q1', 'g': 'q1', 'h': 'q1', 'j': 'q1', 'k': 'q1', 'l': 'q1', ';': 'q2', "'": 'q2',
                'z': 'q1', 'x': 'q1', 'c': 'q1', 'v': 'q1', 'b': 'q1', 'n': 'q1', 'm': 'q1', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q1', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q2', ')': 'q2', '_': 'q1', '+': 'q2',
                'Q': 'q1', 'W': 'q1', 'E': 'q1', 'R': 'q1', 'T': 'q1', 'Y': 'q1', 'U': 'q1', 'I': 'q1', 'O': 'q1', 'P': 'q1', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q1', 'S': 'q1', 'D': 'q1', 'F': 'q1', 'G': 'q1', 'H': 'q1', 'J': 'q1', 'K': 'q1', 'L': 'q1', ':': 'q2', '"': 'q2',
                'Z': 'q1', 'X': 'q1', 'C': 'q1', 'V': 'q1', 'B': 'q1', 'N': 'q1', 'M': 'q1', '<': 'q2', '>': 'q2', '?': 'q2', ' ': 'q2'},
        'q1':  {'`': 'q2', '1': 'q1', '2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1', '7': 'q1', '8': 'q1', '9': 'q1', '0': 'q1', '-': 'q2', '=': 'q2',
                'q': 'q1', 'w': 'q1', 'e': 'q1', 'r': 'q1', 't': 'q1', 'y': 'q1', 'u': 'q1', 'i': 'q1', 'o': 'q1', 'p': 'q1', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q1', 's': 'q1', 'd': 'q1', 'f': 'q1', 'g': 'q1', 'h': 'q1', 'j': 'q1', 'k': 'q1', 'l': 'q1', ';': 'q2', "'": 'q2',
                'z': 'q1', 'x': 'q1', 'c': 'q1', 'v': 'q1', 'b': 'q1', 'n': 'q1', 'm': 'q1', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q1', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q2', ')': 'q2', '_': 'q1', '+': 'q2',
                'Q': 'q1', 'W': 'q1', 'E': 'q1', 'R': 'q1', 'T': 'q1', 'Y': 'q1', 'U': 'q1', 'I': 'q1', 'O': 'q1', 'P': 'q1', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q1', 'S': 'q1', 'D': 'q1', 'F': 'q1', 'G': 'q1', 'H': 'q1', 'J': 'q1', 'K': 'q1', 'L': 'q1', ':': 'q2', '"': 'q2',
                'Z': 'q1', 'X': 'q1', 'C': 'q1', 'V': 'q1', 'B': 'q1', 'N': 'q1', 'M': 'q1', '<': 'q2', '>': 'q2', '?': 'q2' , ' ': 'q2'},
        'q2':  {'`': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2', '0': 'q2', '-': 'q2', '=': 'q2',
                'q': 'q2', 'w': 'q2', 'e': 'q2', 'r': 'q2', 't': 'q2', 'y': 'q2', 'u': 'q2', 'i': 'q2', 'o': 'q2', 'p': 'q2', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q2', 's': 'q2', 'd': 'q2', 'f': 'q2', 'g': 'q2', 'h': 'q2', 'j': 'q2', 'k': 'q2', 'l': 'q2', ';': 'q2', "'": 'q2',
                'z': 'q2', 'x': 'q2', 'c': 'q2', 'v': 'q2', 'b': 'q2', 'n': 'q2', 'm': 'q2', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q2', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q2', ')': 'q2', '_': 'q2', '+': 'q2',
                'Q': 'q2', 'W': 'q2', 'E': 'q2', 'R': 'q2', 'T': 'q2', 'Y': 'q2', 'U': 'q2', 'I': 'q2', 'O': 'q2', 'P': 'q2', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q2', 'S': 'q2', 'D': 'q2', 'F': 'q2', 'G': 'q2', 'H': 'q2', 'J': 'q2', 'K': 'q2', 'L': 'q2', ':': 'q2', '"': 'q2' ,
                'Z': 'q2', 'X': 'q2', 'C': 'q2', 'V': 'q2', 'B': 'q2', 'N': 'q2', 'M': 'q2', '<': 'q2', '>': 'q2', '?': 'q2', ' ': 'q2'}
    }
    initial_state = 'q0'
    final_states = {'q1'}
)

# evaluasi EKSPRESI atau OPERASI dengan FA
check_expression = DFA(
    states={'q0','q1','q2','q3'}
    input_symbols={'`','1','2','3','4','5','6','7','8','9','0','-','=',
                   'q','w','e','r','t','y','u','i','o','p','[',']',"\\",
                   'a','s','d','f','g','h','j','k','l',';',"'",
                   'z','x','c','v','b','n','m',',','.','/',
                   '~','!','@','#','$','%','^','&','*','(',')','_','+',
                   'Q','W','E','R','T','Y','U','I','O','P','{','}','|',
                   'A','S','D','F','G','H','J','K','L',':','"',
                   'Z','X','C','V','B','N','M','<','>','?',' '}
    transitions={
        'q0':  {'`': 'q2', '1': 'q1', '2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1', '7': 'q1', '8': 'q1', '9': 'q1', '0': 'q1', '-': 'q1', '=': 'q2',
                'q': 'q1', 'w': 'q1', 'e': 'q1', 'r': 'q1', 't': 'q1', 'y': 'q1', 'u': 'q1', 'i': 'q1', 'o': 'q1', 'p': 'q1', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q1', 's': 'q1', 'd': 'q1', 'f': 'q1', 'g': 'q1', 'h': 'q1', 'j': 'q1', 'k': 'q1', 'l': 'q1', ';': 'q2', "'": 'q2',
                'z': 'q1', 'x': 'q1', 'c': 'q1', 'v': 'q1', 'b': 'q1', 'n': 'q1', 'm': 'q1', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q1', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q1', ')': 'q1', '_': 'q1', '+': 'q2',
                'Q': 'q1', 'W': 'q1', 'E': 'q1', 'R': 'q1', 'T': 'q1', 'Y': 'q1', 'U': 'q1', 'I': 'q1', 'O': 'q1', 'P': 'q1', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q1', 'S': 'q1', 'D': 'q1', 'F': 'q1', 'G': 'q1', 'H': 'q1', 'J': 'q1', 'K': 'q1', 'L': 'q1', ':': 'q2', '"': 'q2',
                'Z': 'q1', 'X': 'q1', 'C': 'q1', 'V': 'q1', 'B': 'q1', 'N': 'q1', 'M': 'q1', '<': 'q2', '>': 'q2', '?': 'q2', ' ': 'q2'},
        'q1':  {'`': 'q2', '1': 'q1', '2': 'q1', '3': 'q1', '4': 'q1', '5': 'q1', '6': 'q1', '7': 'q1', '8': 'q1', '9': 'q1', '0': 'q1', '-': 'q2', '=': 'q2',
                'q': 'q1', 'w': 'q1', 'e': 'q1', 'r': 'q1', 't': 'q1', 'y': 'q1', 'u': 'q1', 'i': 'q1', 'o': 'q1', 'p': 'q1', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q1', 's': 'q1', 'd': 'q1', 'f': 'q1', 'g': 'q1', 'h': 'q1', 'j': 'q1', 'k': 'q1', 'l': 'q1', ';': 'q2', "'": 'q2',
                'z': 'q1', 'x': 'q1', 'c': 'q1', 'v': 'q1', 'b': 'q1', 'n': 'q1', 'm': 'q1', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q1', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q1', ')': 'q1', '_': 'q1', '+': 'q2',
                'Q': 'q1', 'W': 'q1', 'E': 'q1', 'R': 'q1', 'T': 'q1', 'Y': 'q1', 'U': 'q1', 'I': 'q1', 'O': 'q1', 'P': 'q1', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q1', 'S': 'q1', 'D': 'q1', 'F': 'q1', 'G': 'q1', 'H': 'q1', 'J': 'q1', 'K': 'q1', 'L': 'q1', ':': 'q2', '"': 'q2',
                'Z': 'q1', 'X': 'q1', 'C': 'q1', 'V': 'q1', 'B': 'q1', 'N': 'q1', 'M': 'q1', '<': 'q2', '>': 'q2', '?': 'q2', ' ': 'q2'},
        'q2':  {'`': 'q2', '1': 'q2', '2': 'q2', '3': 'q2', '4': 'q2', '5': 'q2', '6': 'q2', '7': 'q2', '8': 'q2', '9': 'q2', '0': 'q2', '-': 'q2', '=': 'q2',
                'q': 'q2', 'w': 'q2', 'e': 'q2', 'r': 'q2', 't': 'q2', 'y': 'q2', 'u': 'q2', 'i': 'q2', 'o': 'q2', 'p': 'q2', '[': 'q2', ']': 'q2', "\\": 'q2',
                'a': 'q2', 's': 'q2', 'd': 'q2', 'f': 'q2', 'g': 'q2', 'h': 'q2', 'j': 'q2', 'k': 'q2', 'l': 'q2', ';': 'q2', "'": 'q2',
                'z': 'q2', 'x': 'q2', 'c': 'q2', 'v': 'q2', 'b': 'q2', 'n': 'q2', 'm': 'q2', ',': 'q2', '.': 'q2', '/': 'q2',
                '~': 'q2', '!': 'q2', '@': 'q2', '#': 'q2', '$': 'q2', '%': 'q2', '^': 'q2', '&': 'q2', '*': 'q2', '(': 'q2', ')': 'q2', '_': 'q2', '+': 'q2',
                'Q': 'q2', 'W': 'q2', 'E': 'q2', 'R': 'q2', 'T': 'q2', 'Y': 'q2', 'U': 'q2', 'I': 'q2', 'O': 'q2', 'P': 'q2', '{': 'q2', '}': 'q2', '|': 'q2',
                'A': 'q2', 'S': 'q2', 'D': 'q2', 'F': 'q2', 'G': 'q2', 'H': 'q2', 'J': 'q2', 'K': 'q2', 'L': 'q2', ':': 'q2', '"': 'q2' ,
                'Z': 'q2', 'X': 'q2', 'C': 'q2', 'V': 'q2', 'B': 'q2', 'N': 'q2', 'M': 'q2', '<': 'q2', '>': 'q2', '?': 'q2', ' ': 'q2'}
    }
    initial_state = 'q0'
    final_states = {'q2'}
)




