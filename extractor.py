import re
# Hello, this is a comment
# Read the original file contents
with open("hsk6.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

# Extract only the Chinese characters
chinese_text = re.sub("[^\u4e00-\u9fff]+", "", original_text)

# Write the extracted Chinese characters back to the file
with open("hsk6.txt", "w", encoding="utf-8") as file:
    file.write(chinese_text)
