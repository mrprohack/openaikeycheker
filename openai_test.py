import openai

# Function to check if an API key is valid
def is_valid_api_key(api_key):
    openai.api_key = api_key
    try:
        openai.Completion.create(engine='davinci', prompt='Hello', max_tokens=10)
        return True
    except openai.error.AuthenticationError:
        return False
    except openai.error.RateLimitError:
        print(f"API Key {api_key} exceeded the rate limit. Skipping...")
        return False

# Read API keys from a text file
api_key_file = 'api_keys.txt'  # Replace with your file path
valid_api_file = 'valid_api_keys.txt'  # Replace with the desired path for the valid API keys file

with open(api_key_file, 'r') as file:
    with open(valid_api_file, 'w') as valid_file:
        for line in file:
            api_key = line.strip()
            if is_valid_api_key(api_key):
                print(f"API Key {api_key} is valid.")
                valid_file.write(api_key + '\n')

print("Valid API keys saved to 'valid_api_keys.txt'.")

