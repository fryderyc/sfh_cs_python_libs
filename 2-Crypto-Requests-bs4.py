import requests
from bs4 import BeautifulSoup
from cryptography.fernet import Fernet

def scrape_and_encrypt(url, key):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Scraping and encrypting email addresses from a website
    emails = soup.select('a[href^=mailto]')
    #print(emails)
    # https://blog.hubspot.com/website/html-mailto
    encrypted_emails = []

    for email in emails:
        encrypted_email = encrypt_message(email['href'][7:], key)
        encrypted_emails.append(encrypted_email)

    print("Encrypted Emails:")
    for email in encrypted_emails:
        print(email)

def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as file:
        file.write(key)

def load_key():
    with open("encryption.key", "rb") as file:
        key = file.read()
    return key

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message.decode()

def main():
    generate_key() # Run this line only once to generate the encryption key
    
    key = load_key()

    url = input("Enter the URL of the website to scrape: ")
    scrape_and_encrypt(url, key)

if __name__ == '__main__':
    main()