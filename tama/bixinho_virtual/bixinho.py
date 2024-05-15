class Bixinho:
    def __init__(self, data_nascimento):
        self.__dono = None
        self.__nome = None
        self.__felicidade = 0
        self.__fome = 0
        self.__higiene = 0
        self.__sono = 0
        self.__data_nascimento = data_nascimento
        self.__vivo = True
        self.__dormindo = False

    def aumentar_fome(self):
        if not self.dormirndo_ou_acordado():
            if self.__fome < 5:
                self.__fome += 1
            if self.__fome >= 5:
                self.__morrer()

    def diminuir_fome(self):
        if self.verificar_vida() and not self.dormirndo_ou_acordado():
            if self.__fome > 0:
                self.__fome -= 1

    def aumentar_felicidade(self):
        if not self.dormirndo_ou_acordado():
            if self.__felicidade < 5:
                self.__felicidade += 1
            if self.__felicidade >= 5:
                self.__morrer()

    def diminuir_felicidade(self):
        if self.verificar_vida() and not self.dormirndo_ou_acordado():
            if self.__felicidade > 0:
                self.__felicidade -= 1

    def aumentar_higiene(self):
        if not self.dormirndo_ou_acordado():
            if self.__higiene < 5:
                self.__higiene += 1
            if self.__higiene >= 5:
                self.__morrer()

    def diminuir_higiene(self):
        if self.verificar_vida() and not self.dormirndo_ou_acordado():
            if self.__higiene > 0:
                self.__higiene -= 1

    def aumentar_sono(self):
        if not self.dormirndo_ou_acordado():
            if self.__sono < 5:
                self.__sono += 1

    def diminuir_sono(self):
        if self.verificar_vida() and self.dormirndo_ou_acordado():
            if self.__sono > 0:
                self.__sono -= 1

    def dormir(self):
        self.__dormindo = True

    def acordar(self):
        self.__dormindo = False

    def dormirndo_ou_acordado(self):
        return self.__dormindo

    def get_felicidade(self):
        return self.__felicidade

    def get_fome(self):
        return self.__fome

    def get_higiene(self):
        return self.__higiene

    def get_sono(self):
        return self.__sono

    def __morrer(self):
        self.__vivo = False

    def verificar_vida(self):
        return self.__vivo

    def set_nome(self, nome):
        self.__nome = nome

    def set_dono(self, dono):
        self.__dono = dono

    def get_nome(self):
        return self.__nome

    def get_dono(self):
        return self.__dono

    def get_nascimento(self):
        return self.__data_nascimento
