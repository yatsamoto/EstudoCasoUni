# Estudo de Caso

estoque = {}

# Menu
while True:
    print("\n===== Menu Principal =====")
    print("1. Cadastrar Produto")
    print("2. Atualizar Produto")
    print("3. Checar Estoque")
    print("4. Sair")

    escolha = input("Escolha uma opção (1-4): ")

    if escolha == '1':
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        quantidade_produto = int(input("Digite a quantidade em estoque: "))
        
        estoque[nome_produto] = {'preco': preco_produto, 'quantidade': quantidade_produto}
        print(f"{nome_produto} cadastrado com sucesso!")
    elif escolha == '2':
        nome_produto = input("Digite o nome do produto que deseja atualizar: ")
        
        if nome_produto in estoque:
            novo_preco = float(input("Digite o novo preço do produto: "))
            nova_quantidade = int(input("Digite a nova quantidade em estoque: "))
            
            estoque[nome_produto]['preco'] = novo_preco
            estoque[nome_produto]['quantidade'] = nova_quantidade
            print(f"{nome_produto} atualizado com sucesso!")
        else:
            print(f"{nome_produto} não encontrado no estoque.")
    elif escolha == '3':
        print("Estoque atual:")
        for produto, info in estoque.items():
            print(f"{produto}: Preço - {info['preco']}, Quantidade - {info['quantidade']}")
    elif escolha == '4':
        print("Programa encerrado. Obrigado!")
        break
    else:
        print("Opção inválida. Tente novamente.")