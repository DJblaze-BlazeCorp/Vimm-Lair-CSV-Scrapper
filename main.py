import requests
from bs4 import BeautifulSoup
import os

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to scrape data from a given URL and save it to a CSV file
def scrape_console_data(console_url, console_name, identifier):
    # Make a GET request to the URL
    response = requests.get(console_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the data
    table = soup.find('table', class_='rounded centered cellpadding1 hovertable striped')

    # If the table is found
    if table:
        # Create the console directory if it doesn't exist
        create_directory(console_name)

        # Save the data to a CSV file named after the identifier
        csv_filename = os.path.join(console_name, f'{identifier}.csv')
        with open(csv_filename, 'w') as f:
            # Iterate through table rows
            for row in table.find_all('tr'):
                # Write each row to the CSV file
                csv_row = ','.join([cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])])
                f.write(csv_row + '\n')
        print(f"Data for {console_name} scraped and saved to {csv_filename}")
    else:
        print(f"No data found for {console_name}")

# List of consoles and their URLs
consoles = {
    'Atari2600': 'https://vimm.net/vault/Atari2600/',
    'Atari5200': 'https://vimm.net/vault/Atari5200/',
    'NES': 'https://vimm.net/vault/NES/',
    'SMS': 'https://vimm.net/vault/SMS/',
    'Atari7800': 'https://vimm.net/vault/Atari7800/',
    'Genesis': 'https://vimm.net/vault/Genesis/',
    'SNES': 'https://vimm.net/vault/SNES/',
    '32X': 'https://vimm.net/vault/32X/',
    'Saturn': 'https://vimm.net/vault/Saturn/',
    'PS1': 'https://vimm.net/vault/PS1/',
    'N64': 'https://vimm.net/vault/N64/',
    'Dreamcast': 'https://vimm.net/vault/Dreamcast/',
    'PS2': 'https://vimm.net/vault/PS2/',
    'GameCube': 'https://vimm.net/vault/GameCube/',
    'Xbox': 'https://vimm.net/vault/Xbox/',
    'Xbox360': 'https://vimm.net/vault/Xbox360/',
    'PS3': 'https://vimm.net/vault/PS3/',
    'Wii': 'https://vimm.net/vault/Wii/',
    'WiiWare': 'https://vimm.net/vault/WiiWare/',
    'GB': 'https://vimm.net/vault/GB/',
    'Lynx': 'https://vimm.net/vault/Lynx/',
    'GG': 'https://vimm.net/vault/GG/',
    'VB': 'https://vimm.net/vault/VB/',
    'GBC': 'https://vimm.net/vault/GBC/',
    'GBA': 'https://vimm.net/vault/GBA/',
    'DS': 'https://vimm.net/vault/DS/',
    'PSP': 'https://vimm.net/vault/PSP/'
}

# List of alphabet letters and numbers
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0'

# Prompt the user to select a console
print("Select a console to scrape:")
for i, console in enumerate(consoles.keys(), 1):
    print(f"{i}. {console}")

# Get user input for console selection
selected_console_index = int(input("Enter the number corresponding to the console: ")) - 1
selected_console_name = list(consoles.keys())[selected_console_index]
selected_console_url = consoles[selected_console_name]

# Scrape data for alphabet letters
for letter in letters:
    # Construct the URL for the current letter
    letter_url = f"{selected_console_url}{letter}"
    # Scrape data for the selected console and letter
    scrape_console_data(letter_url, selected_console_name, letter)

# Scrape data for numbers
for number in numbers:
    # Construct the URL for the current number
    number_url = f"https://vimm.net/vault/?p=list&system={selected_console_name}&section=number"
    # Scrape data for the selected console and number
    scrape_console_data(number_url, selected_console_name, number)
