import sys

def calcular():
    while True:
        print("\n=== Calculadora ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '5':
            print("Finalizando...")
            sys.exit()

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        try:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
        except ValueError:
            print("Erro! Digite apenas números.")
            continue

        if escolha == '1':
            resultado = num1 + num2
        elif escolha == '2':
            resultado = num1 - num2
        elif escolha == '3':
            resultado = num1 * num2
        elif escolha == '4':
            if num2 == 0:
                print("Erro: divisão por zero!")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calcular()
