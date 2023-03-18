from regra import regraJogo

def main():
    print('Escolha duas Opções:')
    print("""
    1 - Pedra
    2 - Papel
    3 - Tesoura
    4 - Spock
    5 - Lagarto
    """)

    jogo = regraJogo(
        obj1 = input('Jogador 1 escolhe: '),
        obj2 = input('Jogador 2 escolhe: ')
    )
    
    jogo=jogo

if __name__== "__main__":
    main()