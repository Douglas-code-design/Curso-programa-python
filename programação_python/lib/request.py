import requests

# cep = input("Digite seu cep")



# response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")


# data = response.json()



# print(data)
# print(f"você mora na{data["logradouro"]}, que fica no bairro{data["bairro"]}.")

response = requests.get("https://fakestoreapi.com/products/1")

data = response.json()

print(data["price"])
print(data["title"])




