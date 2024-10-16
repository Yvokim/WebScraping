import csv

from selenium import webdriver  # takes automatic control of the browser,basically becoming like a user
from selenium.webdriver.chrome.service import Service  # starts and stops the webdriver and managing the browser session
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # manages updates and downloads for your chrome driver,,

# ensuring it is always up to date

# Initialize the Chrome WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
'''ChromeDriverManager().install():

Downloads the correct version of ChromeDriver and returns the path where it’s saved on your system.
Service(...):

The Service class is initialized with the path returned by ChromeDriverManager().install(). This manages starting and 
stopping ChromeDriver. webdriver.Chrome(...):

Finally, this creates a Chrome instance (i.e., a browser window), with Selenium managing ChromeDriver in the 
background through the service parameter.


'''

try:
    # Open the Quotes to Scrape page
    driver.get('http://quotes.toscrape.com/')

    # Find all quote elements
    quotes = driver.find_elements(By.CLASS_NAME, 'quote')

    # Open a csv file for writing
    with open('quotes.csv', mode='w', newline='', encoding='utf-8') as csv_file:

        # Create a CSV writer object
        writer = csv.writer(csv_file)

        # write the header row
        writer.writerow(['Quote', 'Author', 'Tags'])

        # Iterate through each quote and write to the csv file

        # Iterate through each quote and print the text
        for quote in quotes:
         # Get the quote text
            quote_text = quote.find_element(By.CLASS_NAME, 'text').text
            # Get the author
            author = quote.find_element(By.CLASS_NAME, 'author').text
            # Get the tags (if any)
            tags = quote.find_elements(By.CLASS_NAME, 'tag')
            tag_list = [tag.text for tag in tags]

        # Join the tags into single string separated by commas

            tags_string = ','.join(tag_list)
        # write the quote data to the csv file

            writer.writerow([quote_text, author, tags_string])

        # Print the quote and author
        print(f'Quote: {quote_text}')
        print(f'Author: {author}')
        print(f'Tags: {", ".join(tag_list)}')
        print('-' * 60)  # Separator line

finally:
    # Close the browser after use
    driver.quit()
