from bs4 import BeautifulSoup
import json

# Load JSON data
with open('output.json', 'r') as json_file:
    json_data = json.load(json_file)

# Parse HTML content
with open('Messaggio_2023-12-08.html', 'r') as html_file:
    html_content = html_file.read()
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table by name
    table = soup.find('table', {'name': 'tt'})

    # Iterate through the table rows
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])

        # Ensure there are enough cells to access
        if len(cells) > 1:
            # Extract values from cells
            order = cells[1].get_text(strip=True)

            # Find the corresponding data in JSON
            for item in json_data:
                if str(item['2']) == order:
                    quantity = str(item['10'])
                    # Ensure there are enough cells to access and it contains an input tag
                    if len(cells) > 9 and cells[9].input:
                        cells[9].input['value'] = quantity  # Update the 10th column value

# Save the modified HTML content to a new file
with open('modified_table.html', 'w') as modified_file:
    modified_file.write(str(soup))

print("HTML table has been successfully modified.")
