"""

    João Vitor Paulino - 1801021 - paulino.joaovitor@yahoo.com.br
    Daniel Roberto - 1800479 - bruce-irom@hotmail.com
    Tiago Beneteli - 1800804 - tiagobeneteli@hotmail.com
    Ramon C. Pires - 1800260 - ramoncavpires@gmail.com

"""


from Aluno import Aluno

def create_obj():
    obj = object.__new__(Aluno)
    obj.__init__()
    return obj

def test_name():
    objTeste = create_obj()

    objTeste.nome = "joao"
    assert (objTeste.nome == "joao")
    objTeste.nome = "maria"
    assert (objTeste.nome == "maria")
    objTeste.nome = "Jose"
    assert (objTeste.nome == "Jose")

def test_email():
    objTeste = create_obj()

    objTeste.email = "teste@teste"
    assert (objTeste.email == "teste@teste")
    objTeste.email = "maria@teste.com"
    assert (objTeste.email == "maria@teste.com")
    objTeste.email = "Jose@jose.com.br"
    assert (objTeste.email == "Jose@jose.com.br")

def test_ra():
    objTeste = create_obj()

    objTeste.ra = "123456"
    assert (objTeste.ra == "123456")
    objTeste.ra = "654321"
    assert (objTeste.ra == "654321")
    objTeste.ra = "6543255"
    assert (objTeste.ra == "6543255")

def test_celular():
    objTeste = create_obj()

    objTeste.celular = "12443456"
    assert (objTeste.celular == "12443456")
    objTeste.celular = "654321"
    assert (objTeste.celular == "654321")
    objTeste.celular = "6543255"
    assert (objTeste.celular == "6543255")

def test_desconto_methods():
    objTeste = create_obj()
    objTeste.desconto = 5

    objTeste.aumenta_desconto(5)
    assert(objTeste.desconto == 10)

    objTeste.diminui_desconto(5)
    assert(objTeste.desconto == 5)


def test_lista_disciplinas_methods():
    objTeste = create_obj()

    objTeste.add_disciplina("Arg")

    assert (len(objTeste.disciplinas) > 0)
    assert (objTeste.disciplinas[0] == "Arg")
