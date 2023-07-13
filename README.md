# API Key Validator

A Python script to check the validity of OpenAI API keys.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Command Line Arguments](#command-line-arguments)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The API Key Validator is a Python script that allows you to check the validity of OpenAI API keys. It verifies whether the provided API keys can successfully make an API call without any authentication errors or rate limit exceedances.

## Installation

1. Clone the repository or download the script file to your local machine.
2. Install the required dependencies by running the following command:

```sh
pip install openai argparse termcolor
```

## Usage

To use the API Key Validator, follow these steps:

1. Prepare a text file (`api_keys.txt`) containing the API keys you want to validate. Each API key should be on a separate line.
2. Open a terminal and navigate to the directory where the script is located.
3. Run the following command:

```sh
python api_key_validator.py -f api_keys.txt -o valid_api_keys.txt
```
Replace `api_keys.txt` with the path to your API key file, and `valid_api_keys.txt` with the desired path to save the valid API keys (optional).
4. The script will check the validity of each API key and display the result in the terminal. Valid keys will be printed in green, while invalid keys will be printed in red.
5. If you provided an output file, the valid API keys will be saved to that file.

## Command Line Arguments

The API Key Validator accepts the following command line arguments:

- `-f` or `--api_key_file`: [Required] Specifies the path to the file containing API keys.
- `-s` or `--single_key`: [Optional] Specifies a single API key to check.
- `-o` or `--output_file`: [Optional] Specifies the path to save the valid API keys in a separate file.

You can use either the `-s` or `--single_key` option to check a single API key directly from the command line.

## Contributing

Contributions to the API Key Validator are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
