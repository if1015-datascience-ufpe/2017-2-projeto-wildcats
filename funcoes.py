def inicia_browser():
    if(platform.system() == 'Windows'):
        browser = webdriver.Chrome(executable_path="../2017-2-projeto-wildcats/chromer/chromedriver.exe")
    else:
        browser = webdriver.Chrome()
    return browser

def array_df(lista):
    array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (len(lista)):
        if ':' in lista[i]:
            tops = lista[i].split(':')
            if tops[0] == 'Melhor índice de solução':
                array[10] = tops[1]
            elif tops[0] == 'Melhores Índices de Voltar a Fazer Negócios':
                array[11] = tops[1]
            elif tops[0] == 'Melhores notas médias':
                array[12] = tops[1]
            elif tops[0] == 'Mais resolveram nos últimos 30 dias':
                array[13] = tops[1]
            elif tops[0] == 'Mais resolveram nos últimos 12 meses':
                array[14] = tops[1]
            elif tops[0] == 'Piores empresas nos últimos 30 dias':
                array[15] = tops[1]
            elif tops[0] == 'Mais reclamadas nos últimos 12 meses':
                array[16] = tops[1]
            elif tops[0] == 'Empresas recém-cadastradas com mais reclamações':
                array[17] = tops[1]
            elif tops[0] == 'Mais Reclamadas do dia':
                array[18] = tops[1]
            elif tops[0] == 'Mais Reclamadas da semana':
                array[19] = tops[1]
            elif tops[0] == 'Mais Reclamadas nos últimos 30 dias':
                array[20] = tops[1]
        else:
            if lista[i] != '--':
                array[i] = lista[i]
    return array

            
def click_list(lista):
    for i in lista:
        if i.text != '':
            return i
            break;
    
def append_manual(length,lista,array):
    if length == 2:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1]]
    elif length == 3:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2]]
    elif length == 4:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3]]
    elif length == 5:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4]]
    elif length == 6:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5]]
    elif length == 7:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]]
    elif length == 8:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7]]
    elif length == 9:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8]]
    elif length == 10:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9]]
    elif length == 11:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10]]
    elif length == 12:
        return [array[0] , array[1], array[2], array[3], array[4], array[5], array[6], array[7], array[8], array[9], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9], lista[10], lista[11]]
