import sys

def lexer(input_str):
    # This is where we do lexical analysis. Lexical analysis in simple words = tokenizing. 
    #   we turn the given characters into meaningful chunks of data so that we can use them in parsing
    pass

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
