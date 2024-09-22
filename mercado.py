from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("\n")
    print("=" * 30)
    print(" Projeto Mercado ".center(30, "="))
    print("=" * 30 + "\n")

    print("Selecione uma das opções abaixo:")
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Comprar produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair do sistema")

    opcao: int = int(input("\nInforme sua escolha: "))

    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            listar_produtos()
        case 3:
            comprar_produto()
        case 4:
            visualizar_carrinho()
        case 5:
            fechar_pedido()
        case 6:
            print("Volte sempre!")
            sleep(2)
            exit(0)
        case _:
            print('Opção inválida')
            sleep(1)
            menu()


def cadastrar_produto() -> None:
    print("Cadastro de Produto")
    print("=" * len("Cadastro de Produto"))

    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input("Informe o preço do produto: "))

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print("Listagem de produtos")
        print("=" * len("Listagem de produtos"))

        for produto in produtos:
            print(produto)
            print("-" * 40)
            sleep(1)
    else:
        print("Ainda não existe produtos cadastrados.")
    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código o produto que deseja adicionar ao carrinho:')
        print('------------------------------------------------------------')
        print('Produtos Disponíveis'.center(60, '='))
        for produto in produtos:
            print(produto)
            print('-' * 60)
            sleep(1)
        codigo: int = int(input('Código: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get('produto')
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} agora possui {quantidade+1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod: dict = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()

            else:
                item: dict = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()

    else:
        print("Ainda não existem produtos para vender")
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if (carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        print('=' * len('Produtos do carrinho'))
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('-' * 25)
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
