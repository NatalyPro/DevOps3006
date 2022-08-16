import requests

response = requests.get("http://localhost:5001", data="aaa")
expected = "hello and welcome to the world of games"
print(response.text)
actual = response.text
assert expected == actual