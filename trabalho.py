# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 16:14:20 2020

@author: Wescley
"""

import numpy as np
from lib import distancia

data = np.loadtxt('iris_log.dat', encoding='ASCII')

class1 = data[0:50]
class2 = data[50:100]
class3 = data[100:150]

class1_center = class1.mean(axis=0)[0:4]
class2_center = class2.mean(axis=0)[0:4]
class3_center = class3.mean(axis=0)[0:4]

distancia.euclidiana(class1_center, class2_center, class3_center, data)

distancia.manhattan(class1_center, class2_center, class3_center, data)

distancia.chebyshev(class1_center, class2_center, class3_center, data)

stop = False

while not stop:
    new_instance = [float(input('\n\nDigite o valor do atributo nº 1: ')),
                    float(input('Digite o valor do atributo nº 2: ')),
                    float(input('Digite o valor do atributo nº 3: ')),
                    float(input('Digite o valor do atributo nº 4: '))]

    choice = int(input('\nEscolha uma das médias digitando o número correspondente:\n'
                       '1 - Euclidiana\n'
                       '2 - Manhattan\n'
                       '3 - Chebyshev\n'
                       'Escolha: '))

    print(f'\nA sua instância pertence a classe:', end=' ')
    if choice == 1:
        print(int(distancia.euclidiana(class1_center,
                                       class2_center,
                                       class3_center,
                                       data,
                                       individual_instance=new_instance)))
    elif choice == 2:
        print(int(distancia.manhattan(class1_center,
                                      class2_center,
                                      class3_center,
                                      data,
                                      individual_instance=new_instance)))
    elif choice == 3:
        print(int(distancia.chebyshev(class1_center,
                                      class2_center,
                                      class3_center,
                                      data,
                                      individual_instance=new_instance)))
    else:
        print('Escolha inválida, tente novamente!')
        continue

    response = input('Deseja testar com outra instância?\n\nDigite "S" para continuar ou "N" para sair: ')

    if response[0].lower() == 's':
        print('\n=== === === === Carregando === === === === ===', end='')

exit()
