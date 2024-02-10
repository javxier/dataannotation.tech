def decode(message_file):
    with open(message_file, 'r') as source:
        content = source.readlines()

    # Filter out lines that don't have the expected format
    valid_lines = [line for line in content if len(line.split()) == 2 and line.split()[0].isdigit()]

    # Extract the numeric values from each line
    numbers = [int(line.split()[0]) for line in valid_lines]

    # Extract the last numbers in each line of the pyramid
    last_numbers = []
    current_number = 1

    for num in numbers:
        if num == current_number:
            last_numbers.append(num)
            current_number += 1

    # Extract the words corresponding to the selected last numbers
    selected_words = [line.split()[1] for line in valid_lines if int(line.split()[0]) in last_numbers]

    # Return the selected words as a string
    decoded_text = ' '.join(selected_words)

    return decoded_text

# Example usage:
message_file = 'message_file.txt'  # Replace with the actual file path
decoded_text = decode(message_file)
print(decoded_text)
