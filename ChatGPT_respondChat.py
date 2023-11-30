import re

# Define the input and output file names
input_file_name = "respond2.txt"
output_file_name = "respondChatGPT.html"

# Open the input file for reading using UTF-8 encoding
with open(input_file_name, "r", encoding="utf-8") as input_file:
    # Read the contents of the input file
    file_contents = input_file.read()

# Use regular expressions to find all occurrences of "User" and "ChatGPT"
pattern = r"User(.*?)ChatGPT"
matches = re.findall(pattern, file_contents, re.DOTALL)

# If matches are found, get the text from the last match
if matches:
    last_match = matches[-1]
    extracted_text = last_match.strip()

    # Remove double spaces, newline characters, and consecutive paragraph breaks
    cleaned_text = re.sub(r'  +', ' ', extracted_text)  # Remove double spaces
    cleaned_text = re.sub(r'\n', ' ', cleaned_text)     # Remove newline characters
    cleaned_text = re.sub(r'\n\n+', '\n\n', cleaned_text)  # Remove consecutive paragraph breaks

    # Insert paragraph breaks before "User" and "ChatGPT"
    cleaned_text = re.sub(r'User', '\n\nUser', cleaned_text)
    cleaned_text = re.sub(r'ChatGPT', '\n\nChatGPT', cleaned_text)

    # Create an HTML document with the cleaned text
    html_content = f"<html><body>{cleaned_text}</body></html>"

    # Open the output file for writing using UTF-8 encoding
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        output_file.write(html_content)
    print(f"Extracted, cleaned, and formatted text saved to {output_file_name}")

    # Count the total number of "User" occurrences
    user_count = len(re.findall("User", file_contents))
    print(f"Total number of 'User' occurrences: {user_count}")
else:
    print("No matches found.")
