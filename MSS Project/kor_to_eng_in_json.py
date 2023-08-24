# Import modules
import json
import os

# Define a function to replace words
def replace_words(data, old_word, new_word):
    if isinstance(data, dict):
        return {key: replace_words(value, old_word, new_word) for key, value in data.items()}
    elif isinstance(data, list):
        return [replace_words(item, old_word, new_word) for item in data]
    elif isinstance(data, str):
        return data.replace(old_word, new_word)
    else:
        return data


# Define a function to replace words
def process_files(directory, old_word, new_word):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # print(data)
            # exit()

            # Replace the words in the JSON data
            data = replace_words(data, old_word, new_word)

            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4)

            print(f"Processed {filename}")


directory = "./datasets/"  # Replace with the path to  folder
old_word = "실내"  # Replace with the word you want to replace
new_word = "inside"  # Replace with the new word you want to use

process_files(directory, old_word, new_word)
