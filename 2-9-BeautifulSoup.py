import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Scraping all the headlines from a news website
    headlines = soup.find_all('h2')

    print("Headlines:")
    for headline in headlines:
        print(headline.text.strip())

def main():
    url = input("Enter the URL of the website to scrape: ")
    scrape_website(url)

if __name__ == '__main__':
    main()