from os import system
if system("clear") != 0: system("cls")

#Peticiones a APIs

#Sin dependencias y modo complicado (forma nativa de Python)

import urllib.request
import json


api_posts = 'https://jsonplaceholder.typicode.com/todos/1'

try:
    response = urllib.request.urlopen(api_posts) #abre la url
    data = response.read() #recoge los datos
    json_data = json.loads(data.decode('utf-8')) #convertimos a json
    print(json_data)
    response.close() #cerramos la conexion
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")


# Con dependencias (requests)
import requests

print("\nGET:")

response = requests.get(api_posts)
print(response.json())


print("\POST:")

try:
    api_posts = 'https://jsonplaceholder.typicode.com/posts'
    input = {
        "title": "jmc",
        "body": "bar",
        "userId": 2
    }

    response = requests.post(api_posts, json=input)
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

    print("\PUT:")

try:
    api_posts = 'https://jsonplaceholder.typicode.com/posts/3'
    input = {
        "title": "jmc",
        "body": "bar",
        "userId": 3
    } 

    response = requests.put(api_posts, json=input)
    print(response.status_code)

except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")



#LLamada a la api de gemini

GEMINI_API_KEY="AIzaSyBCkwMLtjQWi1ZXvwJ2kWq1PCOUpp3l7zw"

def call_gemini_api(GEMINI_API_KEY, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    contents = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    response = requests.post(url, json=contents, headers=headers)
    return response.json()


prompt = "Who are you?"

output = call_gemini_api(GEMINI_API_KEY, prompt)

#print(json.dumps(output, indent=2))

texto = output["candidates"][0]["content"]["parts"][0]["text"]
print("\n" + texto)