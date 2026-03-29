from datetime import datetime

print("Versão final do sistema!")

def data_hora():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Operações
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

# Histórico
historico = []
ultima_operacao = None

def salvar_operacao(op):
    global ultima_operacao
    historico.append(op)
    ultima_operacao = op

def mostrar_historico():
    print("\n=== HISTÓRICO ===")
    if not historico:
        print("Nenhuma operação realizada.")
    else:
        for item in historico:
            print(item)

def mostrar_ultima():
    print("\nÚltima operação:", ultima_operacao)

# Menu
def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Ver histórico")
    print("6 - Última operação")
    print("0 - Sair")

# Programa principal
while True:
    print(f"\nData e hora: {data_hora()}")
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Encerrando...")
        break

    elif opcao == "5":
        mostrar_historico()

    elif opcao == "6":
        mostrar_ultima()

    elif opcao in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == "1":
                resultado = somar(num1, num2)
                operacao = f"{num1} + {num2} = {resultado}"

            elif opcao == "2":
                resultado = subtrair(num1, num2)
                operacao = f"{num1} - {num2} = {resultado}"

            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                operacao = f"{num1} * {num2} = {resultado}"

            elif opcao == "4":
                resultado = dividir(num1, num2)
                operacao = f"{num1} / {num2} = {resultado}"

            print(f"Resultado: {resultado}")

            salvar_operacao(f"[{data_hora()}] {operacao}")

        except ValueError:
            print("Erro: digite apenas números válidos!")

    else:
        print("Opção inválida!")
