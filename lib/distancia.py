import numpy as np


def euclidiana(class1_center, class2_center, class3_center, data):
    class1_qtd = 0
    class2_qtd = 0
    class3_qtd = 0

    len_dte = data.shape[0]

    for i in range(0, len_dte):
        """
        Euclidiana
        """
        distances = np.array([np.sqrt(((class1_center - data[i][0:4]) ** 2).sum()),
                              np.sqrt(((class2_center - data[i][0:4]) ** 2).sum()),
                              np.sqrt(((class3_center - data[i][0:4]) ** 2).sum())])
        min_ = np.min(distances)  # retorna o item menor (menor distancia euclidiana)
        idx = np.argmin(distances)  # retorna o index do menor item

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    print(f'\nInstâncias pela classificadas pela média Euclidiana:\n- Classe 1: {class1_qtd}'
          f'\n- Classe 2: {class2_qtd}\n- Classe 3: {class3_qtd}')


def manhattan(class1_center, class2_center, class3_center, data):
    class1_qtd = 0
    class2_qtd = 0
    class3_qtd = 0

    len_dte = data.shape[0]

    for i in range(0, len_dte):
        """
        Manhattan
        """
        distances = np.array([abs((class1_center - data[i][0:4])).sum(),
                              abs((class2_center - data[i][0:4])).sum(),
                              abs((class3_center - data[i][0:4])).sum()])
        min_ = np.min(distances)  # retorna o item menor (menor distancia Manhattan)
        idx = np.argmin(distances)  # retorna o index do menor item

        # print(distances,  'Menor: distancia',min_, 'classe:',idx)

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    print(f'\nQuantidade pela média Manhattan:\n- Class 1: {class1_qtd}'
          f'\n- Class 2: {class2_qtd}\n- Class 3: {class3_qtd}')


def chebyshev(class1_center, class2_center, class3_center, data):
    class1_qtd = 0
    class2_qtd = 0
    class3_qtd = 0
    max_ = 0

    len_dte = data.shape[0]

    for i in range(0, len_dte):
        """
        Chebyshev
        """
        distances = np.array([abs((class1_center - data[i][0:4])).max().sum(),
                              abs((class2_center - data[i][0:4])).max().sum(),
                              abs((class3_center - data[i][0:4])).max().sum()])

        max_ = np.max(distances)  # retorna o item maior (maior distancia Chebyshev)
        idx = np.argmin(distances)  # retorna o index do maior item

        # print(distances,  'Maior: distancia',max_, 'classe:',idx)

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    print(f'\nQuantidade pela média Chebyshev:\n- Class 1: {class1_qtd}'
          f'\n- Class 2: {class2_qtd}\n- Class 3: {class3_qtd}')
