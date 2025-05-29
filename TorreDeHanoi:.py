class Hanoi:
    def __init__(self, num_discos):
        self.discos = num_discos
        self.hastes = [list(range(num_discos, 0, -1)), [], []]

    def estac(self):
        max_alt = max(len(haste) for haste in self.hastes)

        for lvl in range(max_alt, 0, -1):
            lin = []
            for haste in self.hastes:
                if len(haste) >= lvl:
                    tam_disco = haste[lvl - 1]
                    lin.append(' ' * (5 - tam_disco) + '=' * (tam_disco * 2 - 1) + ' ' * (5 - tam_disco))
                else:
                    lin.append(' ' * 11)
            print(' '.join(lin))

        print('    1          2          3   ')
        print()

    def mov_disco(self, d_haste, p_haste):
        if not self.hastes[d_haste]:
            print("A haste original está vazia, tente novamente.")
            return False

        disco = self.hastes[d_haste][-1]
        if self.hastes[p_haste] and self.hastes[p_haste][-1] < disco:
            print("Não é permitido colocar disco maior sobre disco menor.")
            return False

        self.hastes[d_haste].pop()
        self.hastes[p_haste].append(disco)
        return True

    def resolvido(self):
        return self.hastes[2] == list(range(self.discos, 0, -1))

    def jogar(self):
        print("Seja bem-vindo à Torre de Hanói")

        while True:
            try:
                num_discos = int(input("Digite um número de discos, entre 3 a 5: "))
                if 3 <= num_discos <= 5:
                    self.__init__(num_discos)  # Reinitialize with the chosen number of disks
                    break
                else:
                    print("Escolha um número entre 3 a 5.")
            except ValueError:
                print("Entrada inválida, coloque um número.")

        while True:
            self.estac()
            mov_raw = input("Digite o movimento da origem para o destino (ex: 1 3), ou 'sair' para encerrar o jogo: ").strip().lower()

            if mov_raw == 'sair':
                print("Jogo finalizado.")
                break

            try:
                origem, destino = mov_raw.split()
                d_haste = int(origem) - 1
                p_haste = int(destino) - 1

                if d_haste not in [0, 1, 2] or p_haste not in [0, 1, 2]:
                    print("Inválido, escolha entre 1, 2 ou 3.")
                    continue
                if d_haste == p_haste:
                    print("As hastes de origem e destino devem ser diferentes.")
                    continue

                if self.mov_disco(d_haste, p_haste):
                    if self.resolvido():
                        self.estac()
                        print("Parabéns, você resolveu o jogo!")
                        break
            except ValueError:
                print("Entrada inválida, digite dois números separados por espaço (ex: 2 3).")

# Início do jogo 
if __name__ == "__main__":
    Hanoi(3).jogar()
