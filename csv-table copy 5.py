import csv
from bs4 import BeautifulSoup

# Extract keywords dynamically from the HTML file
keywords = []
with open('list.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    modifier_items = soup.find_all(class_='modifier-item')

    for item in modifier_items:
        keyword = item.find(class_='modifier-suggestion').text.strip()
        keywords.append(keyword)

# Read existing data from CSV file
existing_data = {}
with open('output.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        existing_data[row['Keyword']] = {
            'Modifiers': row['Modifiers'],
            'Search Vol': row['Search Vol'],
            'CPC': row['CPC']
        }

# Parse HTML file and extract information
with open('list.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    modifier_items = soup.find_all(class_='modifier-item')

    for item in modifier_items:
        keyword = item.find(class_='modifier-suggestion').text.strip()
        search_vol_elem = item.find(class_='modifier-badge badge-easy')
        cpc_elem = item.find(class_='modifier-badge badge-medium')
        search_vol = '-' if search_vol_elem is None else search_vol_elem.text.strip()
        cpc = '-' if cpc_elem is None else cpc_elem.text.strip()

        # Compare data and update CSV if necessary
        if keyword in existing_data:
            if (existing_data[keyword]['Modifiers'] or
                    search_vol != existing_data[keyword]['Search Vol'] or
                    cpc != existing_data[keyword]['CPC']):
                # Update CSV data
                existing_data[keyword]['Search Vol'] = search_vol
                existing_data[keyword]['CPC'] = cpc
        else:
            # Add new keyword to existing data
            existing_data[keyword] = {
                'Modifier': row['Modifiers'],
                'Search Vol': search_vol,
                'CPC': cpc
            }

# Write updated data to CSV file
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Keyword', 'Modifiers', 'Search Vol', 'CPC'])
    for keyword, data in existing_data.items():
        writer.writerow([keyword, data['Modifiers'], data['Search Vol'], data['CPC']])

print(f'CSV file "{csv_file}" has been created successfully.')
