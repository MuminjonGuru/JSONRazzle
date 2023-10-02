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
            while i < len(input_str) and input_str[i] != '"':
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
    # Here we will write the code to parse the toksenized data and check for the JSON grammar.
    # If the grammar is correct, we will return True, else False.

    stack = []
    last_token = None

    for token in tokens:
        if token in ['{', '[']:
            stack.append(token)
        elif token == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

            # make sure there's either another object, an array, or it's the end
            if last_token not in ['}', ']', '"', True, False, None] and (type(last_token) != int):
                return False
            
        elif token == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()

            if last_token not in ['}', ']', '"', True, False, None] and (type(last_token) != int):
                return False 
        
        elif token == ':':
            # check if there is a key before a colon
            if last_token == '"' or type(last_token) != str:
                return False
            
        elif token == ',':
            # check there is a value before a comma
            if last_token in ['{', '[', ':', ',']:
                return False
            
        # start checking for keys or values (strings)
        elif type(token) == str:
            # check for correct placement
            if last_token not in ['{', ':', ',']:
                return False
            
        # validate digits
        elif type(token) == str:
            if last_token not in [':', ',']:
                return False
    
        elif token in [True, False, None]:
            if last_token not in [':', ',']:
                return False
            
        last_token = token

    # if it balanced, it should be empty
    return not stack


if __name__ == "__main__":
    input_str = input()  # Read the input JSON string from standard input.
    tokens = lexer(input_str)
    is_valid = parse(tokens)

    if is_valid:
        print("Valid JSON")
        sys.exit(0)
    else:
        print("Invalid JSON")
        sys.exit(1)
