import sys

def lexer(input_str):
    # This is where we do lexical analysis. Lexical analysis in simple words = tokenizing. 
    #   we turn the given characters into meaningful chunks of data so that we can use them in parsing

def parse(tokens):
    # Here we take the tokenized data check for the JSON grammar.
    #   if it is in correct order/grammar we're good to go

if __name__ == "__main__":
    input_str = input()  # Read the input JSON string from standard input.
    tokens = lexer(input_str)
    is_valid = parse(tokens)

    # I will come back here
