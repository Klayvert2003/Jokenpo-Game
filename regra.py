class regraJogo:
    def __init__(self, obj1=None or 0, obj2=None or 0, **kwargs):
        self.obj1 = obj1
        self.obj2 = obj2
        super().__init__(**kwargs)
        if self.obj1 != self.obj2:
            try:
                if int(self.obj1) == 1 and (int(self.obj2) == 3 or int(self.obj2) == 5):
                    print('Jogador 1 Ganhou!')

                elif int(self.obj1) == 2 and (int(self.obj2) == 4 or int(self.obj2) == 1):
                    print('Jogador 1 Ganhou!')

                elif int(self.obj1) == 3 and (int(self.obj2) == 2 or int(self.obj2) == 5):
                    print('Jogador 1 Ganhou!')

                elif int(self.obj1) == 4 and (int(self.obj2) == 3 or int(self.obj2) == 1):
                    print('Jogador 1 Ganhou!')

                elif int(self.obj1) == 5 and (int(self.obj2) == 2 or int(self.obj2) == 4):
                    print('Jogador 1 Ganhou!')
                else:
                    print("Jogador 1 perdeu!")
            except:
                if str(self.obj1) == 'Pedra' or str(self.obj1) == 'pedra' and (str(self.obj2) == 'Tesoura' or 
                (str(self.obj2) == 'tesoura' or str(self.obj2) == 'Lagarto' or str(self.obj2) == 'lagarto')):
                    print('Jogador 1 Ganhou!')

                elif str(self.obj1) == 'Papel' or str(self.obj1) == 'papel' and (str(self.obj2) == 'Spock' or
                    str(self.obj2) == 'spock' or str(self.obj2) == 'Pedra' or str(self.obj2) == 'pedra'):
                    print('Jogador 1 Ganhou!')

                elif str(self.obj1) == 'Tesoura' or str(self.obj1) == 'tesoura' and (str(self.obj2) == 'Papel' or 
                    str(self.obj2) == 'papel' or str(self.obj2) == 'Lagarto' or str(self.obj2) == 'lagarto'):
                    print('Jogador 1 Ganhou!')

                elif str(self.obj1) == 'Spock' or str(self.obj1) == 'spock' and (str(self.obj2) == 'Tesoura' or 
                    str(self.obj2) == 'tesoura' or str(self.obj2) == 'Pedra' or str(self.obj2) == 'pedra'):
                    print('Jogador 1 Ganhou!')

                elif str(self.obj1) == 'Lagarto' or str(self.obj1) == 'lagarto' and (str(self.obj2) == 'Papel' or 
                    str(self.obj2) == 'papel' or str(self.obj2) == 'Spock' or str(self.obj2) == 'spock'):
                    print('Jogador 1 Ganhou!')
                else:
                    print("Jogador 1 perdeu!")
        else:
            print("Empate")