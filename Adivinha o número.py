# Adivinha o número
import random

class adivinha:
    def __init__(self):
        self.num_secreto = random.randint(1, 100)
        self.tentativas = 0 
        
    def jogar(self):
        print("Olá meu bom, seja bem-vindo ao Adivinha o número")
        print("Adivinhe  o número de 1 a 100")
        
        while True:
            try:
                escolha = int(input("Digite o número que voçê acha: "))
                self.tentativas += 1
                
                if escolha < self.num_secreto:
                    print("Numero abaixo, escolha valores mais altos")
                elif escolha > self.num_secreto:
                    print("Numero alto, escolha valores mais baixos")
                else:
                    print(f"Acertou!!! {self.tentativas} tentaviva(s)")
                    break
                
            except ValueError:
                print("Digite um número válido")

# Instância e jogar
jogo = adivinha()
jogo.jogar()