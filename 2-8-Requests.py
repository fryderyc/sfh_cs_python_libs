import requests

def send_get_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("GET Request successful!")
        print("Response:")
        print(response.text)
    else:
        print("GET Request failed. Status Code:", response.status_code)

def send_post_request(url, data):
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("POST Request successful!")
        print("Response:")
        print(response.text)
    else:
        print("POST Request failed. Status Code:", response.status_code)

def main():
    url = input("Enter the URL to send the request: ")

    send_get_request(url)

    data = input("Enter the data to send in the POST request (if applicable): ")
    send_post_request(url, data)

if __name__ == '__main__':
    main()