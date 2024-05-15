from tkinter import *
from verificacao import *
from bixinho import Bixinho
from datetime import date
from PIL import Image, ImageTk


class Telas:
    def __init__(self):
        self.bixinho = None

        self.nome_bixinho = None
        self.nome_dono = None
        self.data_nasc = None

        self.cadastro = None

        aux = "    "
        self.barra = ['[▊▊▊▊▊]', f'[▊▊▊▊{aux}]', f'[▊▊▊{aux}{aux}]', f'[▊▊{aux}{aux}{aux}]',
                           f'[▊{aux}{aux}{aux}{aux}]', f'[{aux}{aux}{aux}{aux}{aux}]']

        self.aviso = ''

        self.janela = Tk()
        self.definicoes_tela()

        self.tela_cadastro()

        self.janela.mainloop()

    def definicoes_tela(self):

        largura = 450
        altura = 500

        x = self.janela.winfo_screenwidth()
        y = self.janela.winfo_screenheight()

        x = (x - largura) / 2
        y = (y - altura) / 2

        self.janela.title('Tamagoshi')
        self.janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.janela.resizable(False, False)
        self.janela.configure(bg='Black')

    def tela_cadastro(self):
        self.cadastro = Frame(self.janela, bg='black')
        self.cadastro.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(self.cadastro, text='T A M A G O S H I', font=('Arial', 24), foreground='#00ee00', bg='black').place(relx=0.19, rely=0.03)

        Label(self.cadastro, text='Digite o nome do seu bixinho', foreground='#00ee00', bg='black').place(relx=0.32, rely=0.3)
        self.nome_bixinho = Entry(self.cadastro, bg='#002f00', foreground='#005f00', highlightbackground='#00ee00', relief='flat')
        self.nome_bixinho.place(relx=0.22, rely=0.35, relwidth=0.56)

        Label(self.cadastro, text='Digite como ele vai te chamar', foreground='#00ee00', bg='black').place(relx=0.32, rely=0.5)
        self.nome_dono = Entry(self.cadastro, bg='#002f00', foreground='#005f00', highlightbackground='#00ee00', relief='flat')
        self.nome_dono.place(relx=0.22, rely=0.55, relwidth=0.56)

        self.mensagem_aviso = Label(self.cadastro, text=self.aviso, foreground='#ee0000', bg='black')
        self.mensagem_aviso.place(relx=0.37, rely=0.68)

        criar_bixinho = Button(self.cadastro, text='Criar', font=('Arial', 20), fg='#00ee00', bg='black', relief='flat', command=self.mudanca_cadastro_jogo)
        criar_bixinho.configure(activebackground='black', activeforeground='#00ee00')
        criar_bixinho.place(relx=0.31, rely=0.8, relwidth=0.4, relheight=0.1)

    def mudanca_cadastro_jogo(self):
        if validar_nome(self.nome_bixinho.get()) and validar_nome(self.nome_dono.get()):
            if validar_tamanho(self.nome_bixinho.get()) and validar_tamanho(self.nome_dono.get()):
                self.aviso = ''
                self.bixinho = Bixinho(arrumar_data(date.today()))

                self.bixinho.set_nome(self.nome_bixinho.get())
                self.bixinho.set_dono(self.nome_dono.get())

                self.cadastro.destroy()
                self.tela_bixo()
                self.tela_status()
                self.tela_botoes()

            else:
                self.aviso = 'Nomes muito grande'
                self.mensagem_aviso.configure(text=self.aviso)

        else:
            self.aviso = 'Digite nomes válidos'
            self.mensagem_aviso.configure(text=self.aviso)

    def tela_bixo(self):

        self.bixo = Frame(self.janela, bg='black')
        self.bixo.place(relx=0, rely=0, relwidth=1, relheight=0.48)

        pegar = Image.open('img/tux.png')
        foto = pegar.resize((250, 250))
        self.tux = ImageTk.PhotoImage(foto)

        self.imagem = Label(self.bixo, image=self.tux, bg='black')
        self.imagem.place(relx=0, rely=0, relwidth=1)


        self.tela_informacoes()

    def tela_informacoes(self):

        self.info = Frame(self.janela, bg='#002f00', highlightbackground='#00ee00', highlightthickness=1)
        self.info.place(relx=0.05, rely=0.06, relwidth=0.32, relheight=0.15)

        Label(self.info, text=f'Nome: {self.bixinho.get_nome()}', bg='#002f00', fg='#00ee00').place(relx=0.01, rely=0.03)
        Label(self.info, text=f'Dono: {self.bixinho.get_dono()}', bg='#002f00', fg='#00ee00').place(relx=0.01, rely=0.36)
        Label(self.info, text=f'Nascimento: {self.bixinho.get_nascimento()}', bg='#002f00', fg='#00ee00').place(relx=0.01, rely=0.69)

    def tela_status(self):
        felicidade = self.bixinho.get_felicidade()
        fome = self.bixinho.get_fome()
        higiene = self.bixinho.get_higiene()
        sono = self.bixinho.get_sono()

        self.status = Frame(self.janela, bg='#002f00', highlightbackground='#00ee00', highlightthickness=1)
        self.status.place(relx=0, rely=0.48, relwidth=1, relheight=0.12)

        Label(self.status, text='Felicidade', foreground='#00ee00', bg='#002f00').place(relx=0, rely=0)
        self.texto_barra_felicidade = Label(self.status, text=self.barra[felicidade], foreground='#00ee00', bg='#002f00')
        self.texto_barra_felicidade.place(relx=0, rely=0.5)

        Label(self.status, text='Fome', foreground='#00ee00', bg='#002f00').place(relx=0.25, rely=0)
        self.texto_barra_fome = Label(self.status, text=self.barra[fome], foreground='#00ee00', bg='#002f00')
        self.texto_barra_fome.place(relx=0.25, rely=0.5)

        Label(self.status, text='Higiene', foreground='#00ee00', bg='#002f00').place(relx=0.5, rely=0)
        self.texto_barra_higiene = Label(self.status, text=self.barra[higiene], foreground='#00ee00', bg='#002f00')
        self.texto_barra_higiene.place(relx=0.5, rely=0.5)

        Label(self.status, text='Energia', foreground='#00ee00', bg='#002f00').place(relx=0.75, rely=0)
        self.texto_barra_sono = Label(self.status, text=self.barra[sono], foreground='#00ee00', bg='#002f00')
        self.texto_barra_sono.place(relx=0.75, rely=0.5)

        self.status.after(20000, self.ficar_triste)
        self.status.after(10000, self.ficar_fome)
        self.status.after(30000, self.ficar_sujo)
        self.status.after(50000, self.sono_disposicao)

        self.status.after(100, self.atualizar_status)

    def ficar_triste(self):
        self.bixinho.aumentar_felicidade()

        if self.bixinho.verificar_vida():
            self.status.after(20000, self.ficar_triste)

    def ficar_fome(self):
        self.bixinho.aumentar_fome()

        if self.bixinho.verificar_vida():
            self.status.after(10000, self.ficar_fome)

    def ficar_sujo(self):
        self.bixinho.aumentar_higiene()

        if self.bixinho.verificar_vida():
            self.status.after(30000, self.ficar_sujo)

    def sono_disposicao(self):
        self.bixinho.diminuir_sono()
        self.bixinho.aumentar_sono()

        if self.bixinho.verificar_vida():
            self.status.after(50000, self.sono_disposicao)

    def atualizar_status(self):
        felicidade = self.bixinho.get_felicidade()
        fome = self.bixinho.get_fome()
        higiene = self.bixinho.get_higiene()
        sono = self.bixinho.get_sono()

        self.texto_barra_felicidade.configure(text=self.barra[felicidade])
        self.texto_barra_fome.configure(text=self.barra[fome])
        self.texto_barra_higiene.configure(text=self.barra[higiene])
        self.texto_barra_sono.configure(text=self.barra[sono])

        if not self.bixinho.verificar_vida():
            self.morrer()

        else:

            self.status.after(100, self.atualizar_status)

    def morrer(self):
        self.bixo.destroy()
        self.status.destroy()
        self.botoes.destroy()

        self.tela_morte()

    def tela_morte(self):
        self.morte = Frame(self.janela, bg='black')
        self.morte.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(self.morte, text=f'Você deixou {self.bixinho.get_nome()} morrer', font=('Arial', 24), foreground='#00ee00', bg='black').place(relx=0.05, rely=0.03)

        pegar = Image.open('img/triste.png')
        foto = pegar.resize((250, 250))
        self.tux = ImageTk.PhotoImage(foto)

        Label(self.morte, image=self.tux, bg='black').place(relx=0, rely=0.23, relwidth=1)

        recomecar = Button(self.morte, text='Recomeçar', font=('Arial', 20), relief='flat', command=self.recomecar)
        recomecar.configure(fg='#00ee00', bg='#002f00', activebackground='#002f00', activeforeground='#00ee00')
        recomecar.place(relx=0.07, rely=0.8, relwidth=0.4, relheight=0.14)

        fechar = Button(self.morte, text='Fechar', font=('Arial', 20), relief='flat', command=self.janela.destroy)
        fechar.configure(fg='#00ee00', bg='#002f00', activebackground='#002f00', activeforeground='#00ee00')
        fechar.place(relx=0.53, rely=0.8, relwidth=0.4, relheight=0.14)

    def recomecar(self):
        self.morte.destroy()

        self.tela_cadastro()

    def tela_botoes(self):

        self.botoes = Frame(self.janela, bg='black')
        self.botoes.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)

        brincar = Button(self.botoes, text='Brincar', font=('Arial', 20), relief='flat', command=self.bixinho.diminuir_felicidade)
        brincar.configure(fg='#00ee00', bg='black', activebackground='black', activeforeground='#00ee00')
        brincar.place(relx=0.07, rely=0.15, relwidth=0.4, relheight=0.3)

        alimentar = Button(self.botoes, text='Alimentar', font=('Arial', 20), relief='flat', command=self.bixinho.diminuir_fome)
        alimentar.configure(fg='#00ee00', bg='black', activebackground='black', activeforeground='#00ee00', highlightbackground='black')
        alimentar.place(relx=0.53, rely=0.15, relwidth=0.4, relheight=0.3)

        limpar = Button(self.botoes, text='Limpar', font=('Arial', 20), fg='#00ee00', bg='black', relief='flat', command=self.bixinho.diminuir_higiene)
        limpar.configure(fg='#00ee00', bg='black', activebackground='black', activeforeground='#00ee00')
        limpar.place(relx=0.07, rely=0.55, relwidth=0.4, relheight=0.3)

        self.dormir = Button(self.botoes, text='Dormir', font=('Arial', 20), fg='#00ee00', bg='black', relief='flat', command=self.dormir_acordar)
        self.dormir.configure(fg='#00ee00', bg='black', activebackground='black', activeforeground='#00ee00')
        self.dormir.place(relx=0.53, rely=0.55, relwidth=0.4, relheight=0.3)

    def dormir_acordar(self):
        if self.bixinho.dormirndo_ou_acordado():
            self.bixinho.acordar()

            pegar = Image.open('img/tux.png')
            foto = pegar.resize((250, 250))
            self.tux = ImageTk.PhotoImage(foto)

            self.imagem.configure(image=self.tux)
            self.dormir.configure(text='Dormir')

        else:
            self.bixinho.dormir()

            pegar = Image.open('img/dormindo.png')
            foto = pegar.resize((400, 250))
            self.tux = ImageTk.PhotoImage(foto)

            self.imagem.configure(image=self.tux)
            self.dormir.configure(text='Acordar')





if __name__ == '__main__':
    #   Paleta
    #00ee00
    #008e00
    #005f00
    #002f00
    #000000

    Telas()
