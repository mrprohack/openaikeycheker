import openai
import argparse
from termcolor import colored

# Function to check if an API key is valid
def is_valid_api_key(api_key):
    openai.api_key = api_key
    try:
        openai.Completion.create(engine='davinci', prompt='Hello', max_tokens=10)
        return True
    except openai.error.AuthenticationError:
        return False
    except openai.error.RateLimitError:
        #print(f"API Key {api_key} exceeded the rate limit. Skipping...")
        return False

# Read API keys from a text file
def read_api_keys_from_file(filename):
    with open(filename, 'r') as file:
        api_keys = file.read().splitlines()
    return api_keys

# Parse command line arguments
parser = argparse.ArgumentParser(description='Check the validity of API keys')
parser.add_argument('-s', '--single_key', help='API key to check')
parser.add_argument('-f', '--api_key_file', help='Path to the file containing API keys')
parser.add_argument('-o', '--output_file', help='Path to save the valid API keys')
args = parser.parse_args()

single_key = args.single_key
api_key_file = args.api_key_file
output_file = args.output_file

# Check a single API key if provided
if single_key:
    if is_valid_api_key(single_key):
        print(colored(f"API Key {single_key} is valid.", 'green'))
    else:
        print(colored(f"API Key {single_key} is invalid.", 'red'))

# Check API keys from a file if provided
if api_key_file:
    # Read API keys from the file
    api_keys = read_api_keys_from_file(api_key_file)

    # List to store valid API keys
    valid_api_keys = []
    valid_count = 0

    # Iterate over API keys and check validity
    for api_key in api_keys:
        if is_valid_api_key(api_key):
            valid_api_keys.append(api_key)
            print(colored(f"API Key {api_key} is valid.", 'green'))
            valid_count += 1
        else:
            print(colored(f"API Key {api_key} is invalid.", 'red'))

    # Save valid API keys to a file if output_file is provided
    if output_file:
        with open(output_file, 'w') as file:
            file.write('\n'.join(valid_api_keys))
        print(colored(f"Valid API keys saved to '{output_file}' and Number of valid API keys: {valid_count}.", 'blue'))

# Print help menu if no arguments are provided
if not (single_key or api_key_file):
    parser.print_help()

