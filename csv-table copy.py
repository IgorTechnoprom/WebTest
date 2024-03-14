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
csv_file = 'output.csv'

# Open CSV file in write mode
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(['Modifier Suggestion', 'Search Vol.', 'CPC'])

    # Extract and write data from each modifier item
    for item in modifier_items:
        suggestion = item.find(class_='modifier-suggestion').text.strip()
        cpc_group = item.find(class_='modifier__cpcgroup')
        search_vol, cpc = '-', '-'

        # Check if search volume and CPC are available
        if cpc_group:
            search_vol_elem = cpc_group.find(class_='modifier-badge')
            if search_vol_elem:
                search_vol = search_vol_elem.text.strip()

            cpc_elems = cpc_group.find_all(class_='modifier-badge')
            if len(cpc_elems) == 2:
                cpc = cpc_elems[1].text.strip()

        # Write row to CSV file
        writer.writerow([suggestion, search_vol, cpc])

print(f'CSV file "{csv_file}" has been created successfully.')
