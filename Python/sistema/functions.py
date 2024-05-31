# Importação de Bibliotecas para uso no algorítmo
from time import sleep
from random import randint

# Declaração de variáveis com o valor dos nomes dos arquivos para uso no algorítmo
arq_areas_pesca = 'areaspesca.txt'
arq_especies = 'especies.txt'
arq_relatorios_pesca = 'relatoriospesca.txt'
arq_registros_pescadores = 'registrospescadores.txt'

# Declaração de variáveis com valores de cores para uso no console
limpa_cor, vermelho, verde, amarelo, azul, azul_claro = ('\033[m', '\033[31m', '\033[32m', '\033[33m', '\033[34m',
                                                         '\033[36m')


# Função que valida se os arquivos já existem ou não, caso não exista, cria eles
def validar_arquivos(arqap, arqe, arqrelp, arqregp):
    if not existe_arquivo(arqap):
        criar_arquivo(arqap)
    if not existe_arquivo(arqe):
        criar_arquivo(arqe)
    if not existe_arquivo(arqrelp):
        criar_arquivo(arqrelp)
    if not existe_arquivo(arqregp):
        criar_arquivo(arqregp)


# Função que checa se o arquivo existe ou não, caso exista retorna True, caso não exista retorna False
def existe_arquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print(f'{vermelho}Arquivo {arq} não encontrado, criando...{limpa_cor}')
        sleep(1.5)
        return False
    else:
        return True


# Função que cria um arquivo
def criar_arquivo(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print(f'{vermelho}Erro! Não foi possível criar o arquivo {arq}.{limpa_cor}')
    else:
        print(f'{verde}Arquivo de registro {arq} criado com sucesso!{limpa_cor}')
        sleep(1.5)
    finally:
        a.close()


# Função que lê um arquivo e mostra seus dados formatados no console
def ler_arquivo(arq):
    espaco = ''
    try:
        a = open(arq, 'rt')
    except:
        print(f'{vermelho}Erro! não foi possível ler o arquivo.{limpa_cor}')
    else:
        if arq == arq_areas_pesca:
            cabecalho('Áreas de Pesca Registradas no Sistema')
        elif arq == arq_especies:
            cabecalho('Espécies de Peixe Registradas no Sistema')
        elif arq == arq_relatorios_pesca:
            cabecalho('Relatórios de Pesca')
        elif arq == arq_registros_pescadores:
            cabecalho('Pescadores Registrados no Sistema')
        for linhas in a:
            dado = linhas.split(';')
            if arq == arq_relatorios_pesca:
                dado[4] = dado[4].replace('\n', '')
                print(f'Espécie: {dado[0]:<15} {espaco:>4}Qntd: {dado[1]:>5} {espaco:>4} '
                      f'Data:{dado[2]}/{dado[3]} {espaco:>4} ID do Pescador: {dado[4]}')
            else:
                dado[1] = dado[1].replace('\n', '')
            if arq == arq_areas_pesca:
                print(f'Área: {dado[0]:<38} {espaco:>20}Status: {dado[1]}')
            elif arq == arq_especies:
                print(f'Espécie: {dado[0]:<38} {espaco:>18}Status: {dado[1]}')
            elif arq == arq_registros_pescadores:
                print(f'Nome do Pescador: {dado[0]:<40} {espaco:>15}ID: {dado[1]}')
        sleep(2)
    finally:
        a.close()


# Função que cadastra uma área de pesca nova no sistema
def cadastrar_area(arq, nome='desconhecida', status='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print(f'{vermelho}Não foi possível registrar a área.{limpa_cor}')
    else:
        a.write(f'{nome};{status}\n')
        a.close()


# Função que cadastra uma espécie de peixe nova no sistema
def cadastrar_especie(arq, nome='desconhecida', status='desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print(f'{vermelho}Não foi possível registrar a espécie.{limpa_cor}')
    else:
        a.write(f'{nome};{status}\n')
        a.close()


# Função que registra um novo relatório de pesca no sistema
def registrar_relatorio_pesca(arq, especie='desconhecido', qntd=0, dia=0, mes=0, id_p=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{vermelho}Não foi possível registrar o novo relatório.{limpa_cor}')
    else:
        a.write(f'{especie};{qntd};{dia};{mes};{id_p}\n')
        a.close()


# Função que cadastra um pescador novo no sistema
def cadastrar_pescador(arq, nome='desconhecido', id_p=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'{vermelho}Não foi possível cadastrar o pescador.{limpa_cor}')
    else:
        a.write(f'{nome};{id_p}\n')
        a.close()


# Função que retorna uma linha horizontal
def linha():
    return '--' * 42


# Função que printa no console um cabeçalho com o texto desejado no centro
def cabecalho(txt):
    print(linha())
    print(txt.center(84))
    print(linha())


# Função que lê um número inteiro e não deixa dar erro no sistema.
def ler_int(txt):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print(f'{vermelho}Por favor, digite um número inteiro válido.{limpa_cor}')
        else:
            return n


# Lista que contém todas as opções do menu do console que aparecem para o usuário
opcoes = ['Verificar Áreas de Pesca', 'Registrar Nova Área de Pesca', 'Verificar Espécies de Peixe',
          'Registrar Nova Espécie de Peixe', 'Verificar Relatórios de Pesca', 'Novo Relatório de Pesca',
          'Verificar Registros de Pescador', 'Novo Registro de Pescador', 'Sair do Sistema']


# Função que printa cada opção do menu no console formatado
def menu(opc):
    for i in range(len(opc)):
        print(f'{amarelo}{i + 1}{limpa_cor} - {azul}{opc[i]}{limpa_cor}')


# Função que executa o programa principal
def programa_principal():
    while True:
        cabecalho('Sistema de Controle de Pesca')
        menu(opcoes)
        esc = ler_int(f'{verde}Sua escolha: {limpa_cor}')
        match esc:
            case 1:
                ler_arquivo(arq_areas_pesca)
            case 2:
                cabecalho('Cadastrar Nova Área de Pesca no Sistema')
                nome = str(input('Nome da Área: ')).strip().capitalize()
                status = str(input('Status da Área [Liberada / Proibida]: ')).strip().capitalize()
                cadastrar_area(arq_areas_pesca, nome, status)
                print(f'{verde}Área {nome} registrada com sucesso!{limpa_cor}')
                sleep(0.5)
            case 3:
                ler_arquivo(arq_especies)
            case 4:
                cabecalho('Cadastrar Nova Espécie de Peixe no Sistema')
                nome = str(input('Nome da Espécie: ')).strip().capitalize()
                status = str(input('Status da Espécie [Liberada / Risco]: ')).strip().capitalize()
                cadastrar_especie(arq_especies, nome, status)
                print(f'{verde}Espécie {nome} cadastrada com sucesso!{limpa_cor}')
                sleep(0.5)
            case 5:
                ler_arquivo(arq_relatorios_pesca)
            case 6:
                cabecalho('Novo Relatório de Pesca')
                especie = str(input('Nome da Espécie: ')).strip().capitalize()
                qntd = ler_int(f'Quantidade de {especie} pescado: ')
                dia = ler_int('Dia da Pesca: ')
                mes = ler_int('Mês: ')
                id_p = ler_int('ID do Pescador: ')
                registrar_relatorio_pesca(arq_relatorios_pesca, especie, qntd, dia, mes, id_p)
                print(f'{verde}Relatório registrado com sucesso.{limpa_cor}')
                sleep(0.5)
            case 7:
                ler_arquivo(arq_registros_pescadores)
            case 8:
                cabecalho('Novo Registro de Pescador')
                nome = str(input('Nome do Pescador: ')).strip().capitalize()
                id_p = randint(1000, 9999)
                cadastrar_pescador(arq_registros_pescadores, nome, id_p)
                print(f'{verde}Pescador {nome} registrado com sucesso.{limpa_cor}')
                sleep(0.5)
            case 9:
                print(f'{vermelho}Programa finalizando...{limpa_cor}')
                sleep(1)
                break
