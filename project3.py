def decode(message_file):
    with open(message_file, 'r') as source:
        content = source.readlines()

    # Filter out lines that don't have the expected format
    valid_lines = [line for line in content if len(line.split()) == 2 and line.split()[0].isdigit()]

    # Extract the numeric values from each line
    numbers = [int(line.split()[0]) for line in valid_lines]

    # Calculate the total number of lines in the pyramid
    total_lines = int((8 * len(valid_lines) + 1) ** 0.5 / 2)

    # Extract the last numbers in each line of the pyramid
    last_numbers = [num for i, num in enumerate(numbers) if i % total_lines == (total_lines - 1) or i == len(numbers) - 1]

    # Extract the words corresponding to the selected last numbers
    selected_words = [line.split()[1] for line in valid_lines if int(line.split()[0]) in last_numbers]

    # Return the selected words as a string
    decoded_text = ' '.join(selected_words)

    return decoded_text

# Example usage:
message_file = 'message_file.txt'  # Replace with the actual file path
decoded_text = decode(message_file)
print(decoded_text)
