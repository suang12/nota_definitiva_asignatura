# Programa para realizar los operadores, usando las  diferentes formulas

print("---------------------------------------")
print("---------VALOR NOTA DEFINITIVA---------")
print("---------------------------------------")
# input
nc = int(input("Digite el valor de nc: "))
cp = int(input("Digite el valor de cp: "))
na = int(input("Digite el valor na: "))
au = int(input("Digite el valor au: "))
bi = int(input("Digite el valor bi: "))
# processing
nd = (0.3*nc) + (0.3*cp) + (0.1*na) + (0.1*au) + (0.2*bi)
# output
print("------------------------")
print("-------RESULTADOS-------")
print("------------------------")

print("resultados NOTA DEFINITIVA " + str(nd))
