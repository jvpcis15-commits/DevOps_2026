print("Versão 2 do sistema!")
from datetime import datetime

agora = datetime.now()
print("Data e hora atual:", agora)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    if opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = somar(num1, num2)
            elif opcao == "2":
                resultado = subtrair(num1, num2)
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
            elif opcao == "4":
                resultado = dividir(num1, num2)

            print(f"Resultado: {resultado}")

        except ValueError:
            print("Erro: digite apenas números válidos!")

    else:
        print("Opção inválida!")
