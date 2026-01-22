import requests

url = "https://api.restful-api.dev/objects"

responses = requests.get(url)
print(responses.status_code)
print(responses.json())

posturl="https://api.restful-api.dev/objects"

body1={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
r1=requests.post(posturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())

puturl="https://api.restful-api.dev/objects/ff8081819782e69e019be40f81e72ecf"
body1={
   "name": "Apple ",
   "data": {
      "year": 2018,
      "price": 1849,
      "CPU model": "Intel Core i5",
      "Hard disk size": "1 TB"
   }
}
r1=requests.put(puturl,json=body1);
print("post status code",r1.status_code)
print(r1.json())
