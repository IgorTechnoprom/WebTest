from bs4 import BeautifulSoup
import csv

# Read HTML content from file
html_file = 'list.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract modifier items
modifier_items = soup.find_all('li', class_='modifier-item')

# CSV file name
csv_file = 'output_modifiers.csv'

# Open CSV file in write mode
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Modifier Suggestion', 'Search Vol.', 'CPC'])
    
    # Extract and write data from each modifier item
    for modifier_item in modifier_items:
        suggestion = modifier_item.find('div', class_='modifier-suggestion').text.strip()
        search_vol = modifier_item.find('div', class_='modifier-item__cpc').find_all('div', class_='modifier-badge')[0].text.strip()
        cpc = modifier_item.find('div', class_='modifier-item__cpc').find_all('div', class_='modifier-badge')[1].text.strip()
        
        # Write row to CSV file
        writer.writerow([suggestion, search_vol, cpc])

print(f'CSV file "{csv_file}" has been created successfully.')
