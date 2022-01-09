import os
import sys
import winsound

def limpar_buffer():
    sys.stdout.flush()

class produto():
    def __init__(self,ref,dat = [],lig = dict()):
        self.ref = ref
        self.dat = dat
        self.lig = lig

def addcor(param):
    return {'cor':param ,'1': 0,'2' : 0,'3' : 0,'4' : 0,'5': 0,'6': 0}

def vdict(x):
    x = x.replace(' ', '')
    x = x.replace('{', '')
    x = x.replace('}', '')
    x = x.replace("'", '')
    saida = []
    y = x.split(',')
    for x in y:
        saida.append(x.split(':')[1])
    return {'cor':saida[0] ,'1': int(saida[1]),'2' : int(saida[2]),'3' : int(saida[3]),'4' : int(saida[4]),'5': int(saida[5]),'6': int(saida[6])}

def vdict_list(x):
    x = x.replace(' ', '')
    x = x.replace('[', '')
    x = x.replace(']', '')
    y = x.split('},{')
    saida = []
    for x in y:
        saida.append(vdict(x))
    return saida

def vdict_cores(x):
    x = x.replace('{','')
    x = x.replace('}','')
    x = x.replace(' ','')
    x = x.replace("'",'')
    lista = x.split(',')
    hop = dict()
    for y in lista:
        z = y.split(':')
        hop.update({z[0]:int(z[1])})

    return hop

data = 'C:\\Users\\leotp\\Desktop\\meusprojetos\\contador_do_leo\\banco_de_dados.txt'
lista_de_tamanhos = ['PP','P','M','G','GG','EGG']


def ler(mnsg='==>'):
    x = input(mnsg)
    y = list()
    y.append(x[-8:-1])
    y.append(x[-12:-8])
    y.append(x[:-12])

    return y

def checar_cmd(entrada):
    for cmd in entrada:
        if cmd == 'SAIR':
            exit('Saindo...')
        
        if cmd == 'COLECAO':
            pass

        if cmd == 'PESQUISA':
            pass

def ler_manual(mnsg='==>'):
    entrada = input(mnsg).upper().split(' ')

    ref = None
    cor = None
    qnt = None
    tam = None
    adc = []

    for elemento in entrada:
        if elemento.isnumeric() and len(elemento) == 7:
            ref = elemento

        if elemento.isalpha():
            cor = elemento

        if '.' in elemento:
            elems = elemento.split('.')
            if len(elems) != 2:
                continue

            if elems[0] in lista_de_tamanhos and elems[1].isnumeric():
                qnt = int(elems[1])
                tam = elems[0]
            elif elems[1] in lista_de_tamanhos and elems[0].isnumeric():
                qnt = int(elems[0])
                tam = elems[1]
            else:
                continue

            adc.append([qnt,tam])

        return [ref,cor,adc]

def carregar_dados():
    dados = open(data, 'r').read().split('\n')
    lista = []
    dicts_refs = dict()
    for i,x in enumerate(dados):
        xlist = x.split('@@')
        if len(xlist)>2:
            dicts_refs.update({xlist[0]:i})
            lista.append(produto(xlist[0],vdict_list(xlist[1]),vdict_cores(xlist[2])))

    return [lista, dicts_refs]    

def alert():
    winsound.Beep(2500, 500)

def nao_tem_problema(ent):
    if len(ent[0])+len(ent[1])+len(ent[2]) < 11:
        print('Erro!! Leia novamente')
        alert()
        return False
    else:
        return True

def tem_essa_ref(ref, _refs):
    return ref in _refs.keys()

def tem_essa_cor(lista,_refs,ref,cor):
    try:
        y = lista[_refs[ref]].lig[cor]
        return True
    except:
        return False

def salvar(lista):
    save = open('banco_de_dados.txt', 'w')
            
    for i,x in enumerate(lista,1):
        print(x.ref, x.dat, x.lig, sep='@@', end='', file = save)
        if i != len(lista):
            print('\n',end='', file = save)

    save.close()

def header():
    os.system('cls')
    print('#####################################')
    print('####    CONTADOR DO LÉO VICTOR    ###')
    print('####      v 1.0.0 p/ Windows      ###')
    print('#####################################')