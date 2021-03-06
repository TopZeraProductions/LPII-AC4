#João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
#Daniel Roberto - 1800479 - bruce-irom@hotmail.com
#Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
#Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

class Professor:

    def __init__(self):
        self.__email = None
        self.__nome = None
        self.__ra = None
        self.__celular = None
        self.__listaDisciplina = []

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ra(self):
        return self.__ra

    @ra.setter
    def ra(self, ra):
        self.__ra = ra

    @property
    def celular(self):
        return self.__celular

    @celular.setter
    def celular(self, celular):
        self.__celular = celular

    @property
    def disciplinas(self):
        return self.__listaDisciplina

    def add_disciplinas(self, discName):
        self.__listaDisciplina.append(discName)

x = Professor()
x.nome = "Tomás Ferreira"
x.email = "tomas@gmail.com"
x.ra = 1800299
x.celular = 11988972762
x.add_disciplinas = "Ciências"
print(x.nome)
print(x.email)
print(x.ra)
print(x.celular)
print(x.add_disciplinas)
