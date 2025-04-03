horaentrada1 = int(input("Qual a hora da 1º entrada? "))
minentrada1 = int(input("Qual os minutos da 1º entrada? "))
horaentrada2 = int(input("Qual a hora da 2º entrada? "))
minentrada2 = int(input("Qual os minutos da 2º entrada? "))

horaentrada1 = 0
horaentrada2 = 0
minentrada1 = 0
minentrada2 = 0

if horaentrada1 > 12:
    horaentrada1 = horaentrada1 - 60
if horaentrada2 > 12:
    horaentrada2 = horaentrada2 - 60

horasaida = horaentrada1 + horaentrada2

if minentrada1 >= 60:
    horaentrada1 = horaentrada1 + 1
    minentrada1 = minentrada1 - 60
if minentrada2 >= 60:
    horaentrada2 = horaentrada2 + 1
    minentrada2 = minentrada2 - 60

minsaida = minentrada1 + minentrada2

print(horasaida, minsaida)