import requests


url = "https://api.github.com"
response = requests.get(url)

print(response) # imprime un obj de estado "<Response [200]>"
print(response.headers) #imprime todos los headers en modo de diccionario
print(response.status_code) #imprime codigo del estado de la peticion "200"

"""podemos acceder los datos de la respuesta conocidos 
    como el cuerpo o la carga "Payload" 

    hay 3 manera de acceder a ellos
    content = respuesta en bytes (b)
    text = respuesta en String
    json = respuesta en diccionario de python
# """
print(response.content)
print(response.text)
print(response.json()["current_user_url"])


"""filtro de query-params"""

url = "https://api.github.com/search/repositories"

"""
se envian de forma de diccionario y {"1":"python"} hace referencia a los query params

q = query (esto permite hacer la consulta)
Python = (sobre que palabra se hara consulta)

"""
response = requests.get(url, params={"q":"python"})
# print(response.status_code)
print(response.json())
data = response.json()
print(data.keys())

