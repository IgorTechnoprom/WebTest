from bs4 import BeautifulSoup
import re

# Open the HTML file for reading
with open('proizvod.html', 'r', encoding='utf-8') as html_file:
    # Read the content of the HTML file
    html_content = html_file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove extra spaces between elements
    for element in soup.find_all(string=lambda text: isinstance(text, str)):
        # Replace multiple spaces with a single space
        element.replace_with(re.sub(r'\s+', ' ', element.strip()))

    # Save the cleaned HTML content to a new file
    with open('proizvod-ociscen.html', 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(str(soup))

print("HTML file has been cleaned and saved successfully.")
