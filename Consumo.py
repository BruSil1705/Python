#Faça um algoritmo que calcule o combustível gasto em 
#uma viagem de 2000 Km, com autonomia de 10 Km/l
autonomia = int(input("Autonomia do veículo Km/l:"))
distancia = int(input("Distância da viagem Km:"))
gasto = distancia/autonomia
print("Seu consumo foi de ", gasto, " litros.")