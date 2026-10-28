from math import isfinite


def cadastrar_produto(estoque):
    while True:
        codigo = input("Digite o código do produto: ").strip().upper()

        if not codigo:
            print("O código não pode ficar vazio.")
        elif any(produto["codigo"] == codigo for produto in estoque):
            print("Já existe um produto cadastrado com esse código.")
        else:
            break

    while True:
        nome = input("Digite o nome do produto: ").strip()

        if nome:
            break

        print("O nome não pode ficar vazio.")

    while True:
        try:
            preco = float(input("Digite o preço do produto: R$ ").replace(",", "."))

            if not isfinite(preco):
                print("Digite um preço válido.")
            elif preco < 0:
                print("O preço não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Digite um preço válido.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Digite uma quantidade inteira válida.")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)
    print("Produto cadastrado com sucesso.")


def calcular_total_produtos(estoque):
    total = sum(produto["quantidade"] for produto in estoque)
    print(f"Quantidade total de produtos em estoque: {total}")


def exibir_menu():
    estoque = []

    while True:
        print("\nCONTROLE DE ESTOQUE - LOJA DE CAPINHAS")
        print("1 - Cadastrar Produto")
        print("2 - Calcular o Total de Produtos em Estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(estoque)
        elif opcao == "2":
            calcular_total_produtos(estoque)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


exibir_menu()
