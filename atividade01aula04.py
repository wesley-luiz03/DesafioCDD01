#Solicitando um número qualquer
mes = int(input("Digite o número do mês: "))

#Comparação entre 1 e 12 para descobrir o mês
if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else: #Caso não esteja entre 1 e 12 a mensagem de erro é imprimida na tela
    print("Digite um número válido.")

