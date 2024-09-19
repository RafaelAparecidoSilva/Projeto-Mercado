from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    pass

def cadastro_produto() -> None:
    pass

def listar_produtos() -> None:
    pass

def comprar_produto() -> None:
    pass

def visualizar_carrinho() -> None:
    pass

def fechar_pedido() -> None:
    pass

def pega_produto_por_codigo() -> Produto:
    pass


if __name__ == '__main__':
    main()