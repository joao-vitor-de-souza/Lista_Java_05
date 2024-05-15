import os
import time
import threading
import keyboard


class Coisas:
    def __init__(self):
        self.tempo = 0
        self.limite = True
        self.acontecer = True


    def mostrar_horas(self):
        print(self.tempo)


    def contar_horas(self):
        while self.acontecer:
            self.tempo += 1
            # time.sleep(1)

    def tempo_limite(self):
        while self.acontecer:
            time.sleep(3)
            if self.limite == True:
                keyboard.press('3')
                keyboard.press('Enter')

    def trocar_limite(self):
        if self.limite == True:
            self.limite = False
        else:
            self.limite = True

if __name__ == '__main__':
    coisas = Coisas()

    paralelo = threading.Thread(target=coisas.contar_horas)
    paralelo.start()

    limite = threading.Thread(target=coisas.tempo_limite)
    limite.start()

    while True:
        print('1 - mostrar horas')
        print('2 - Tirar limite')
        print('3 - Sair')
        a = int(input('O que quer fazer: '))
        os.system('cls')

        if a == 1:
            coisas.mostrar_horas()

        elif a == 2:
            coisas.trocar_limite()

        else:
            coisas.acontecer = False
            break
