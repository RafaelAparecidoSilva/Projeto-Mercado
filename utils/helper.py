def formata_float_str_moeda(valor: float) -> str:
    # Substitui a vírgula pelo ponto e o ponto pela vírgula para o formato brasileiro
    resultado = f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
    return resultado