import os
print(f"Running {__file__}...")
print(f"__name__ is {__name__}")
# Import the os module to allow for the definition of the path to the HSK level files
# Define the path to the directory containing the HSK level files
hsk_dir = os.path.dirname(__file__)

def profile(text):
    # Count the total number of characters in the text file
    total_chars = len(text)

    # Initialize variables for the character counts in each HSK level file
    hsk_counts = [0] * 6

    # Loop through each character in the text file
    for char in text:
        # Loop through each HSK level file
        for i in range(1, 7):
            # Define the path to the HSK level file
            hsk_path = os.path.join(hsk_dir, f"hsk{i}.txt")
            # Read the HSK level file contents
            with open(hsk_path, "r", encoding="utf-8") as hsk_file:
                hsk_text = hsk_file.read()
            # If the character is found in the HSK level file, increment the count
            if char in hsk_text:
                hsk_counts[i-1] += 1
                break  # Break out of the inner loop once the character is found in one file

    # Compute the average HSK level for the characters in the text file
    total_hsk_score = sum(hsk_counts)
    if total_hsk_score > 0:
        avg_hsk_level = sum([(i+1)*count for i, count in enumerate(hsk_counts)]) / total_hsk_score
    else:
        avg_hsk_level = 0

    return total_chars, hsk_counts, avg_hsk_level
