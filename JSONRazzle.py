import sys

def lexer(input_str):
    # This is where we do lexical analysis. Lexical analysis in simple words = tokenizing. 
    #   we turn the given characters into meaningful chunks of data so that we can use them in parsing
    tokens = []
    i = 0

    while i < len(input_str):
        char = input_str[i]

        if char == '{':
            tokens.append('{')
            i += 1
        elif char == '}':
            tokens.append('}')
            i += 1
        elif char == '[':
            tokens.append('[')
            i += 1
        elif char == ']':
            tokens.append(']')
            i += 1
        elif char == '"':
            start = i
            i += 1
            while i < len(input_str) and input_str[i] != '"';
                i += 1
            tokens.append(input_str[start:i+1])
            i += 1
        elif char.isdigit():
            start = i
            while i < len(input_str) and input_str[i].isdigit():
                i += 1
            tokens.append(int(input_str[start:i]))
        elif input_str[i:i+4] == 'true': # need to check 4 characters here
            tokens.append(True)
            i += 4
        elif input_str[i:i+5] == 'false': # need to check 5 characters here
            tokens.append(False)
            i += 5
        elif input_str[i:i+4] == 'null': # you get the idea
            tokens.append(None)
            i += 4
        elif char in [':', ',']:
            tokens.append(char)
            i += 1
        else:
            i += 1 # just skip spaces
    
    return tokens

def parse(tokens):
    # Here we will write the code to parse the tokenized data and check for the JSON grammar.
    # If the grammar is correct, we will return True, else False.
    if tokens:
        # Here we take the tokenized data check for the JSON grammar.
        #   if it is in correct order/grammar we're good to go
        return True
    else:
        return False

if __name__ == "__main__":
    input_str = input()  # Read the input JSON string from standard input.
    tokens = lexer(input_str)
    is_valid = parse(tokens)

    # I will come back here
