#Variável de contador
contador = 0

#Estrutura de repetição até 10
for num in range (1, 11,1):
    num = int(input(f"Digite o {num}º número: "))
    #Cálculo para adicionar o valor com o valor de num
    contador = contador + num

print(contador)