import random

tam_tabuleiro = 10
nav = [5, 4, 3, 3, 2] # Tamanhos dos navios

def cria_tab():
    return [["~"] * tam_tabuleiro for _ in range(tam_tabuleiro)]

def imprime_tab(tab):
    print("  " + " ".join(map(str, range(tam_tabuleiro))))
    for lin_num, lin in enumerate(tab):
        print(lin_num, " ".join(lin))

def pos_nav():
    tab = cria_tab()
    lista_nav = []
    
    for tam in nav:
        colocado = False
        while not colocado:
            vert = random.choice([True, False])
            lin = random.randint(0, tam_tabuleiro - (tam if vert else 1))
            col = random.randint(0, tam_tabuleiro - (1 if vert else tam))

            posicoes = []

            for i in range(tam):
                l = lin + i if vert else lin
                c = col if vert else col + i
                if tab[l][c] != "~":
                    break
                posicoes.append((l, c))
            else:
                for l, c in posicoes:
                    tab[l][c] = "N"
                lista_nav.append({
                    "posicoes": posicoes,
                    "acertos": 0,
                    "tamanho": tam
                })
                colocado = True

    return tab, lista_nav

def todos_afundados(lista_nav):
    return all(n["acertos"] == n["tamanho"] for n in lista_nav)

def jogo():
    tab_secreto, lista_nav = pos_nav()
    tab_jogador = cria_tab()
    tentativas = 0

    print("Bem-vindo à Batalha Naval")
    while not todos_afundados(lista_nav):
        imprime_tab(tab_jogador)
        entrada = input("Digite a linha e a coluna (ex: 3 4): ")

        try:
            lin, col = map(int, entrada.split())
            if not (0 <= lin < tam_tabuleiro and 0 <= col < tam_tabuleiro):
                raise ValueError
        except ValueError:
            print("Coordenadas inválidas. Tente novamente")
            continue

        if tab_jogador[lin][col] != "~":
            print("Você já tentou aqui, faça novamente")
            continue

        tentativas += 1

        if tab_secreto[lin][col] == "N":
            tab_jogador[lin][col] = "X"
            print("Acertou miserável!")
            for navio in lista_nav:
                if (lin, col) in navio["posicoes"]:
                    navio["acertos"] += 1
                    if navio["acertos"] == navio["tamanho"]:
                        print("Você afundou um navio")
                    break
        else:
            tab_jogador[lin][col] = "O"
            print("Água!")

    imprime_tab(tab_jogador)
    print(f"Parabéns. Você afundou todos os navios em {tentativas} tentativas")

if __name__ == "__main__":
    jogo()
