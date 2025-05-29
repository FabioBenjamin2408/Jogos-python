import random

class PPT: 
    def __init__(self):
        self.opcoes = ["pedra", "papel", "tesoura"]
        self.vit_usuario = 0
        self.vit_computador = 0
        self.empates = 0
    def jogar(self):
        print("Olá meu bom, seja bem-vindo ao PPT (Pedra, Papel e Tesoura)!")
        print("Digite 'sair' para encerrar o jogo.")

        while True:
            usuario = input("Faça sua escolha: Pedra, Papel ou Tesoura?").strip().lower() # para permitir letrs minúsculas
            if usuario == "sair":
                print("Jogo acabou.")
                self.placar()
                break

            if usuario not in self.opcoes:
                print("AMIGÃO FAZ FAVOR, ESCOLHA UMA OPÇÃO VÁLIDA, SEJA GENTE!")
                continue
            computador = random.choice(self.opcoes)
            print(f"PC escolheu: {computador}")
            if usuario == computador:
                print("empate")
                self.empates += 1
            elif(
                (usuario == "pedra" and computador == "tesoura") or
                (usuario == "papel" and computador == "pedra") or
                (usuario == "tesoura" and computador == "papel")
            ):
                print("Você venceu!")
                self.vit_usuario += 1
            else:
                print("PC venceu")
                self.vit_computador += 1
            print()
            self.placar()
        
    def placar(self):
        print(f"Seu placar: {self.vit_usuario} | Computador: {self.vit_computador} | Empates: {self.empates},")
        print("-" * 50)

# Rodar PPT

jogo = PPT()
jogo.jogar()