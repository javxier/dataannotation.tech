def decode(message_file):
    with open(message_file, 'r') as source:
        content = source.readlines()

    # Filter out lines that don't have the expected format
    valid_lines = [line for line in content if len(line.split()) == 2 and line.split()[0].isdigit()]

    # Extract the numeric values from each line
    numbers = [int(line.split()[0]) for line in valid_lines]

    # Create a dictionary to store the words associated with each number
    words_dict = {num: line.split()[1] for num, line in zip(numbers, valid_lines)}

    # Find the maximum value in the numbers list
    max_number = max(numbers)

    # Initialize an empty list to store the selected words
    selected_words = []

    # Iterate through the rows of the pyramid
    for row in range(1, max_number + 1):
        # Calculate the starting index for the current row
        start_index = sum(range(row)) + 1

        # Find the last number in the current row
        last_number = start_index + row - 1

        # Add the word associated with the last number to the selected_words list
        selected_words.append(words_dict.get(last_number, ''))

    # Return the selected words as a string
    decoded_text = ' '.join(selected_words)

    return decoded_text

# Example usage:
message_file = 'message_file.txt'  # Replace with the actual file path
decoded_text = decode(message_file)
print(decoded_text)
