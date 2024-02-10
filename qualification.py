def decode(message_file):
    with open(message_file, 'r') as source:
        content = source.readlines()

    # For validity take out lines that don't follow expected format
    valid_lines = [line for line in content if len(line.split()) == 2 and line.split()[0].isdigit()]

    # Find numeric values from each line
    numbers = [int(line.split()[0]) for line in valid_lines]

    # Make a dictionary to store the words associated with each number
    words_dict = {num: line.split()[1] for num, line in zip(numbers, valid_lines)}

    # Find the maximum value in list of numbers
    max_number = max(numbers)

    # Create empty list for storing selected words
    selected_words = []

    # Iterate through each row of the pyramid
    for row in range(1, max_number + 1):
        # Beginning index
        start_index = sum(range(row)) + 1

        # Last number in the current row
        last_number = start_index + row - 1

        # Words associated with last number of row, appended here to list 'selected_words'
        selected_words.append(words_dict.get(last_number, ''))

    # Return selected words as a string, cleaning excess whitespaces
    decoded_text = ' '.join(selected_words).strip()

    return decoded_text

# main test
message_file = 'message_file.txt'
decoded_text = decode(message_file)
print(decoded_text)