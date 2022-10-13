import requests
url = "https://api.adviceslip.com/advice"
r = requests.get(url)
response = r.json()
advice = response['slip']['advice']
print(advice)