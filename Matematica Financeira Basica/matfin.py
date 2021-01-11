import pandas as pd
import numpy as np
import math
import datetime
from sympy import Symbol
from matplotlib import pyplot as plt

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# VALOR PRESENTE
def PV01(lst, tx): 
    "Argumentos: lista de listas com uma data e o fluxo e taxa de juros"
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, index = ["1", "2", "3", "4", "5"], 
                  columns = ["Ano", "Fluxo de Caixa"])

    print(df)

    #Calculando o valor presente 
    df["VP"] = (df["Fluxo de Caixa"])/((1+tx)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    SPV = df["VP"].sum()
    print("Valor Presente: ", SPV)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
# VALOR PRESENTE DO EXCEL
def PV02(lst, tx):
    "Argumentos: lista de listas com uma data e o fluxo e taxa de juros"
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, index = ["1", "2", "3", "4", "5"], 
                      columns = ["Ano", "Fluxo de Caixa"])
    print(df)

    #Calculando o valor presente 
    df["VP"] = (df["Fluxo de Caixa"])/((1+tx)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    NPV = df["VP"].sum()
    print("Valor Presente: ", NPV)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## VALOR PRESENTE PARA UM FLUXO DE CAIXA COM UM VALOR NEGATIVO
def NPV03(lst, tx):
    "Argumentos: lista de listas com uma data e o fluxo e taxa de juros"
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, 
                  columns = ["Ano", "Fluxo de Caixa"])
    print(df)

    #Calculando o valor presente 
    df["VP"] = (df["Fluxo de Caixa"])/((1+tx)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    NPV = df["VP"].sum()
    print("Valor Presente: ", NPV)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## VALOR PRESENTE DE UMA ANUIDADE INFINITA
def ANN04(c, r, lst):
    "Argumentos: "
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, index = ["1", "2", "3", "4", "5"], 
                  columns = ["Ano", "Pagamento Anual"])

    #Calculando o valor presente
    df["VP"] = (df["Pagamento Anual"])/((1+r)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    SPV = df["VP"].sum()
    print("Valor Presente: ", SPV)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## ANUIDADE INFINITA
def IANN05(c,r):
    "Argumentos: pagamento periódico e taxa de juros"
    VP = c/r
    print("Valor Presente: ", VP)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## ANUIDADE CRESCENTE FINITA
def VGA06(lst, c, g, r):
    "Argumentos: lista com períodos e fluxos, pagamento, taxa de crescimento, juros"
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, index = ["1", "2", "3", "4", "5"], 
                  columns = ["Ano", "Pagamento Anual"])
    print(df)

    #Calculando C levando em conta g
    df["VPG"] = c*((1+g))**(df["Ano"]-1)
    print(df)

    #Calculndo o valor presente dos fluxos com G
    df["VP2"] = (df["VPG"])/((1+r)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    SPV = df["VP2"].sum()
    print("Valor Presente: ", SPV)

'Utilizando a fórmula:'
def FVGA06(c, g, r, n):
    "Argumentos: pagamento, taxa de crescimento, taxa de juros, número de períodos"
    VP = c*(1-((1+g)/(1+r))**n)/(r-g)
    print("Utilizando a Fórmula o Valor Presente é: ", VP)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## ANUIDADE CRESCENTE INFINITA
def VGIA07(c, r, g):
    "Argumentos: fluxo, taxa de juros, taxa de crescimento"
    VP = c/(r-g)
    print("Valor Presente: ", VP)

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## TAXA INTERNA DE RETORNO
def TIR08(lst):
    "Argumentos: lista de listas"
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, 
                  columns = ["Ano", "Fluxo de Caixa"])
    print(df)
    #Definindo um símbolo para taxa de juros
    r = Symbol("r")
    #Calculando o valor presente 
    df["VP"] = (df["Fluxo de Caixa"])/((1+r)**df["Ano"])
    print(df)

    #Explicitando a conta que estamos fazendo.
    eq = df["VP"].sum()
    print("A conta é:", eq, "= 0")
    #Criando uma lista com os fluxos de caixa a partir 
    #da lista original:
    fluxos = [fluxo[1] for fluxo in lst]
    print("Os fluxos são: ", fluxos)

    #Calculando a TIR
    TIR = np.irr(fluxos)
    print("A TIR é: ", 100*TIR, "%")

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
## TAXA INTERNA DE RETORNO DO EXCEL
    '''
        A função do Excel para calcular a TIR o faz por tentativa e erro. 
        É possível simular esse procedimento no Excel “chutando” vários valores 
        para a TIR e checando para quais deles o valor presente é zero:
    '''
def TABLE09(lst, r):
    #Convertendo a lista em dataframe
    df = pd.DataFrame(lst, 
                  columns = ["Ano", "Fluxo de Caixa"])
    print(df)

    #Calculando o valor presente 
    df["VP"] = (df["Fluxo de Caixa"])/((1+r)**df["Ano"])
    print(df)

    #Soma dos valores presentes
    NPV = df["VP"].sum()
    print("Valor Presente: ", NPV)

    '''
    O objetivo é zerar o valor presente. Vamos fazer isso definindo um range e usar 
    um loop para que o programa teste para quais valores de juros o valor presente entra
    em um intervalo ao redor do zero
    ''' 
def TIR10(lst):
    df = pd.DataFrame(lst, 
                  columns = ["Ano", "Fluxo de Caixa"])
    print(df)
    for i in range(-10000, 10001):
        r = i/10000
        df["VP"] = (df["Fluxo de Caixa"])/((1+r)**df["Ano"])
        NPV = df["VP"].sum()
        if -0.1<= NPV <=0.1:
            print("Uma Aproximação Para a TIR é: ", r)

    '''
        Há dois problemas evidentes com esse método. O primeiro é o intervalo para os chutes 
        da taxa de juros. Como ele só vai de -1 a 1, a função não retornará nenhum resultado
        caso a TIR esteja fora dele. O segundo é o intervalo ao redor do zero para o valor presente. 
        Se por azar todos os valores presentes calculados para todas as taxas de juros caírem fora 
        dele, a função também não retornará nenhum resultado
    '''
