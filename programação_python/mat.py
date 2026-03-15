import matplotlib.pyplot as plt


x = [1 ,2 ,3, 4, 5]
y = [2, 4, 3, 7, 6]

plt.plot(x, y)
plt.title("Meu Primeiro garfico com python")
plt.xlabel("isso é X")
plt.ylabel("isso é Y")



produtos= ["A", "B", "C","D"]
vendas = [10, 27, 7, 18]

plt.bar(produtos, vendas)
plt.title("vendas por produto")
plt.xlabel("produtos")
plt.ylabel("vendas")
plt.show