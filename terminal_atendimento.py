from sisbanco import Banco, Conta

def terminal():
    sisbanco = Banco()
    while True:
        print("\nSisBanco::Bem-Vindo!")
        print(".::OPÇÕES::.")
        print("[0] - Criar Conta")
        print("[1] - Creditar")
        print("[2] - Debitar")
        print("[3] - Transferir")
        print("[4] - Saldo")
        print("[5] - Sair")
        opcao = int(input("Digite uma opção: "))
        if opcao == 0:
            numero = str(input("Digite o número da conta: "))
            conta = Conta(numero)
            sisbanco.cadastrar(conta)
        elif opcao == 1:
            numero = str(input("Digite o número da conta:"))
            valor = float(input("Digite o valor creditado: "))
            sisbanco.creditar(numero,valor)
        elif opcao == 2:
            numero = str(input("Digite o número da conta:"))
            valor = float(input("Digite o valor debitado: "))
            sisbanco.debitar(numero,valor)
        elif opcao == 3:
            origem = str(input("Digite o número da conta de origem: "))
            destino = str(input("Digite o número da conta destino: "))
            valor = float(input("Digite o valor a ser traferido: "))
            sisbanco.transferir(origem,destino,valor)
        elif opcao == 4:
            numero = str(input("Digite o número da conta: "))
            print(f"O saldo da conta {numero} é de {sisbanco.saldo(numero)}")
        elif opcao == 5:
            print("SisBanco::Bye!")
            return
        else:
            print("Operação Inválida!")
            continue

if __name__ == "__main__":
    terminal()