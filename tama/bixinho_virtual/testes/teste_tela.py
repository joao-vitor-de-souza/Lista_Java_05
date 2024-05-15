# import time
from tkinter import *
# import threading

class Tela:
    def __init__(self):
        self.rodando = True
        self.texto = None
        self.numero = 0
        self.frame = None
        aux = "    "
        # ░▊
        self.barra_fome = ['[▊▊▊▊▊]', f'[▊▊▊▊{aux}]', f'[▊▊▊{aux}{aux}]', f'[▊▊{aux}{aux}{aux}]', f'[▊{aux}{aux}{aux}{aux}]', f'[{aux}{aux}{aux}{aux}{aux}]']

        # paralelo = threading.Thread(target=self.contar)
        # paralelo.start()

        self.tela = Tk()

        self.definicoes_tela()

        # self.tela.bind('<Destroy>', self.mudar)

        self.frame_teste()
        self.frame_teste2()

        self.tela.after(100, self.atualizar)
        self.tela.after(3000, self.contar)






        # if self.tela.quit() != None:
        #     print(self.tela.quit())
        #     self.rodando = False

        self.tela.mainloop()

    def atualizar(self):
        self.frame.destroy()

        self.frame_teste()

        self.tela.after(100, self.atualizar)



    def mudar(self, event):
        self.rodando = False

    def contar(self):
        #   self.rodando == True
        # while True:
        # time.sleep(3)
        self.numero += 1
        self.tela.after(3000, self.contar)
        # if self.numero == 5:
        #     break


    def definicoes_tela(self):

        largura = 450
        altura = 500

        x = self.tela.winfo_screenwidth()
        y = self.tela.winfo_screenheight()

        x = (x - largura) / 2
        y = (y - altura) / 2

        self.tela.title('Teste')
        self.tela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.tela.resizable(False, False)
        self.tela.configure(bg='Black')

    def frame_teste(self):
        self.frame = Frame(self.tela, bg='#00ee00')
        self.frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.1)

        self.texto = Label(self.frame, text=self.barra_fome[self.numero], bg='#00ee00')
        self.texto.place(relx=0.5, rely=0)

    def enter(self, event):
        print('Entrou')

    # function to be called when mouse exits the frame
    def exit_(self, event):
        print('Saiu')

    def aumentar_barra(self):
        if 0 < self.numero < 5:
            self.numero -= 1

    def frame_teste2(self):
        self.frame2 = Frame(self.tela, bg='#008e00')
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        Button(self.frame2, bg='#005f00', width=1, command=self.aumentar_barra).place(relx=0, rely=0)

        self.frame2.bind('<Enter>', self.enter)
        self.frame2.bind('<Leave>', self.exit_)


    # def atualizar_texto(self):
    #     self.texto.configure(text=self.numero)


if __name__ == '__main__':
    #   Paleta
    #00ee00
    #008e00
    #005f00
    #002f00
    #000000

    classe = Tela()
