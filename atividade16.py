# Crie um programa que receba o peso e a altura de uma pessoa e calcule o Índice de Massa Corporal (IMC). O programa deve classificar o IMC da pessoa de acordo com a tabela a seguir:
# Abaixo do peso: IMC < 18.5
# Peso normal: 18.5 ≤ IMC < 25
# Sobrepeso: 25 ≤ IMC < 30
# Obesidade: IMC ≥ 30
peso = int(input(" Insira o Peso do Indivíduo "))
altura = int(input(" Insira a Altura do Indivíduo "))

imc = peso / (altura * 2)

if (imc < 18.5):
    print(" O Indivíduo está abaixo do peso ")

elif (18.5<= imc <25):
    print(" O Indivíduo está com Peso Normal ")

elif (25 <= imc < 30):
    print(" O Indivíduo está com Sobrepeso ")

elif (imc >= 30):
    print(" O Indivíduo está Obeso ")



