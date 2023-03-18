class regraJogo:
    def __init__(self, obj1, obj2, **kwargs):
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
                if str(self.obj1).lower() == 'pedra' and ((str(self.obj2).lower() == 'tesoura' or str(self.obj2).lower() == 'lagarto')):
                    print('Jogador 1 Ganhou!')
                
                elif str(self.obj1).lower() == 'papel' and ((str(self.obj2).lower() == 'spock' or str(self.obj2).lower() == 'pedra')):
                    print('Jogador 1 Ganhou!')
                
                elif str(self.obj1).lower() == 'tesoura' and ((str(self.obj2).lower() == 'papel' or str(self.obj2).lower() == 'lagarto')):
                    print('Jogador 1 Ganhou!')
                
                elif str(self.obj1).lower() == 'spock' and ((str(self.obj2).lower() == 'tesoura' or str(self.obj2).lower() == 'pedra')):
                    print('Jogador 1 Ganhou!')
                
                elif str(self.obj1).lower() == 'lagarto' and ((str(self.obj2).lower() == 'papel' or str(self.obj2).lower() == 'spock')):
                    print('Jogador 1 Ganhou!')
                else:
                    print("Jogador 1 perdeu!")
        else:
            print("Empate")