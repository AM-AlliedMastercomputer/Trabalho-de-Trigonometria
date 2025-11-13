# Imports ----------------------------------------------------------------------
import os
# Def --------------------------------------------------------------------------
def limpar_tela():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
# Prints -----------------------------------------------------------------------
print ("======================================================================")
print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
print ("======================================================================")
print ("| [ 1 ] Calculo dos lados do triângulo                               |")
print ("| [ 2 ] Calculo do sen, cos e tangente                               |")
print ("| [ 3 ] Calculo graus para radianos                                  |")
print ("| [ 4 ] Conversão radianos para graus                                |")
print ("| [ 5 ] Conversão dos angulos opostos                                |")
print ("======================================================================")
# Inputs -----------------------------------------------------------------------
entrada = int(input())
catA = 0
catB = 0
hip = 0
total = 0
# Main code --------------------------------------------------------------------
limpar_tela()
if entrada == 1:
    entrada = 0
    print ("======================================================================")
    print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
    print ("======================================================================")
    print ("|                   Calculo dos lados do triângulo                   |")
    print ("|[ 1 ] Tenho os dois catetos (encontrar a hipotenusa)                |")
    print ("|[ 2 ] Tenho um cateto e a hipotenusa (encontrar o outro cateto)     |")
    print ("|[ 3 ] Tenho a hipotenusa (encontrar os catetos)                     |")
    print ("|[ 4 ] Tenho um cateto (encontrar o cateto e a hipotenusa)           |")
    print ("======================================================================")
    entrada = int(input())
    if entrada == 1:
        limpar_tela()
        print ("======================================================================")
        print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
        print ("======================================================================")
        print ("|                   Calculo dos lados do triângulo                   |")
        print ("|        Tenho os dois catetos (encontrar a hipotenusa)              |")
        print ("|Insira o valor do cateto A:                                         |")
        print ("|Insira o valor do cateto B:                                         |")
        print ("======================================================================")
        catA = int(input())
        catB = int(input())
        limpar_tela()
        hip = ((catA ** 2) + (catB ** 2)) ** 0.5
        print ("======================================================================")
        print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
        print ("======================================================================")
        print ("|                   Calculo dos lados do triângulo                   |")
        print (f"Cateto A: {catA}                                                   ")
        print (f"Cateto B: {catB}                                                   ")
        print (f"Hipotenusa: {hip:.2f}                                              ")
        print ("======================================================================")
        # fim da opção 1
    elif entrada == 2:
        print ("======================================================================")
        print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
        print ("======================================================================")
        print ("|                   Calculo dos lados do triângulo                   |")
        print ("|[ 1 ] Tenho os dois catetos (encontrar a hipotenusa)                |")
        print ("|[ 2 ] Tenho um cateto e a hipotenusa (encontrar o outro cateto)     |")
        print ("|[ 3 ] Tenho a hipotenusa (encontrar os catetos)                     |")
        print ("|[ 4 ] Tenho um cateto (encontrar o cateto e a hipotenusa)           |")
        print ("======================================================================")
elif entrada == 2:
    print ("======================================================================")
    print ("=====================CALCULADORA DE TRIGONOMETRIA=====================")
    print ("======================================================================")
    print ("|                Calculo de Seno, Cosseno e Tangente                 |")
    print ("|[ 1 ] Seno                                                          |")
    print ("|[ 2 ] Cosseno                                                       |")
    print ("|[ 3 ] Tangente                                                      |")
    print ("======================================================================")

#elif entrada == 2