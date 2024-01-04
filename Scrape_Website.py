import requests
from bs4 import BeautifulSoup

url = 'https://example.com'  # Replace with the URL of the website you want to scrape

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Use the BeautifulSoup functions to extract the data you need from the HTML
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    heading_text = heading.get_text()
    link = heading.find('a')  # Find the first <a> tag within the heading, if it exists
    if link:
        heading_link = link['href']
        print(f"=== {heading_text} ===")
        print(f"Link: {heading_link}")
    else:
        print(f"=== {heading_text} ===")

    next_element = heading.find_next()  # Get the next element after the heading
    while next_element.name.startswith(('h', 'p', 'ul', 'ol', 'img')):  # Select specific tags
        # Print the text of the element based on its tag
        if next_element.name.startswith('h'):
            print(f"=== {next_element.get_text()} ===")
        elif next_element.name == 'p':
            print(next_element.get_text())
        elif next_element.name in ['ul', 'ol']:
            for li in next_element.find_all('li'):
                print(f"- {li.get_text()}")
        elif next_element.name == 'img':
            print(f"Image: {next_element['src']}")
        next_element = next_element.find_next()  # Move to the next element

    print('\n')  # Add a newline for better readability