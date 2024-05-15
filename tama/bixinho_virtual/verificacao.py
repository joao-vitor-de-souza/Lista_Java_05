def validar_nome(nome):
    try:
        if nome != None and nome[0] != ' ':
            return True

    except:

        return False

def validar_tamanho(nome):
    try:
        if len(nome) <= 10:
            return True

    except:

        return False

def arrumar_data(data):
    data_arrumada = ''

    data_arrumada += str(data.day) + '/' + str(data.month) + '/' + str(data.year)

    return data_arrumada
