lista = [input("Insira o sexo: "), input("\n Insira o sexo:"), input("\n Insira o sexo:")]

masculino = 0
feminino = 0

for a in lista:
    if a == 'M' or a == 'm':
        masculino = masculino + 1
    elif a == 'F' or a == 'f':
        feminino = feminino + 1

print("Masculino: ", masculino)
print("\nFeminino: ",feminino)
