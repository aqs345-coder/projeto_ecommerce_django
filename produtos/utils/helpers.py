def formata_preco(valor):
    if valor is not None:
        return f'R$ {valor:.2f}'.replace('.', ',')
    return 'R$ 0,00'
