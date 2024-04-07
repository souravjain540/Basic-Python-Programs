import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get("Paste a Domain here")
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as empty list
all_h1_tags = []

# Set all_h1_tags to all h1 tags of the soup
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

print(all_h1_tags)

# give you all h1 tags 