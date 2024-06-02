import requests

for i in range(1000):
    response = requests.get('https://www.google.com')
    html_content = response.text