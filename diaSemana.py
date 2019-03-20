array = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

a = int(input("Digite o dia da semana: "))

if a < 0 or a > 7: 
    print("Dia invalido!!")
else:
    print("O dia em questão eh: ", array[a-1])
