lista = [int(input("Numero 1: ")), int(input("\nNumero 2: ")), int(input("\nNumero 3: "))]
maior = 0


for a in range(len(lista)):

    if maior < lista[a]:
        maior = lista[a]
print("Maior numero eh: ", maior)
