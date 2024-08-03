#nome = str(input("Digite seu nome: "))
#idade = int(input("Digite sua idade: "))
import math

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/(altura**2)
if imc<18.5:
    print(f"Seu IMC é {imc}.")
    print("Configura estado de MAGREZA.")
    print(f"Seu peso ideal é entre {18.5 * (altura ** 2):.2f}kgs e {24.9 * (altura ** 2):.2f}kgs")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Seu IMC é {imc}.")
    print("Configura estado de NORMAL.")
    print(f"Está dentro do seu peso ideal que é entre {18.5 *(altura**2)}kgs e {24.9 *(altura**2)}kgs")
else:
    print(f"Seu IMC é {imc}.")
    print("Configura estado de OBESIDADE.")
    print(f"Seu peso ideal é entre {18.5 * altura * altura} e {24.9 * altura * altura}")
