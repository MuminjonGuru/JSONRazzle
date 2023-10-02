# JSONRazzle - JSON Validator

A basic JSON validator built using Python to demonstrate lexical and syntactic analysis. While it may not cover the entire JSON specification comprehensively, it provides insights into the process of parsing and validation.

## Features

- Basic tokenization of JSON strings into meaningful chunks.
- Validation of basic JSON structures including objects, arrays, key-value pairs, strings, numbers, booleans, and null.
- File-based validation.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/MuminjonGuru/JSONRazzle.git
   cd JSONRazzle
   ```

2. Run the validator on a JSON file:
   ```bash
   python main.py test.json
   ```

   Replace `test.json` with the path to your JSON file.

3. See the validation results on the console.

## Structure

- `lexer`: Function to tokenize the JSON content.
- `parse`: Function to parse the tokenized data and validate it based on the JSON grammar.
- `validate_json_file`: Function to read a `.json` file and validate its content.

## Limitations

- This is a basic demonstration and might not cover all edge cases of the JSON specification.
- Nested structures and arrays with multiple and varied types of items are handled simplistically. For comprehensive validation, a more advanced approach or library would be necessary.

## Contributing

Feel free to submit issues or pull requests to improve the validator or extend its features.

## License

This project is licensed under the Apache License.
