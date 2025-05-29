import time

class Quiz:
    def __init__(self):
        self.perguntas = [
            {
                "pergunta": "Qual é a capital do Brasil?",
                "opcoes": ["A) São Paulo", "B) Brasília", "C) Rio de Janeiro", "D) Belo Horizonte"],
                "correta": "B"
            },
            {
                "pergunta": "Quanto é 9 x 3?",
                "opcoes": ["A) 27", "B) 18", "C) 36", "D) 21"],
                "correta": "A"
            },
            {
                "pergunta": "Qual linguagem é usada para páginas da web?",
                "opcoes": ["A) Python", "B) C++", "C) HTML", "D) Java"],
                "correta": "C"
            }
        ]
        self.pontuacao = 0

    def jogar(self):
        print("Seja bem-vindo ao Quiz!\n")
        time.sleep(1)

        for i, pergunta in enumerate(self.perguntas, 1):
            print(f"Pergunta {i}: {pergunta['pergunta']}")
            for opcao in pergunta["opcoes"]:
                print(opcao)
            resposta = input("Sua resposta (A/B/C/D): ").strip().upper()

            if resposta == pergunta["correta"]:
                print("Acertou miseravel!\n")
                self.pontuacao += 1
            else:
                print(f"Errouuu. A resposta correta é {pergunta['correta']}.\n")
            time.sleep(1)

        print(f"Fim do quiz. Sua pontuação final foi: {self.pontuacao} de {len(self.perguntas)}")

# Rodar o quiz
quiz = Quiz()
quiz.jogar()
