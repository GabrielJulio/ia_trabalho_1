import numpy as np


def euclidiana(class1_center, class2_center, class3_center, data, individual_instance=None):
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
        idx = np.argmin(distances)  # retorna o index do menor item

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    if not individual_instance:
        print(f'\nInstâncias pela classificadas pela média Euclidiana:\n- Classe 1: {class1_qtd}'
              f'\n- Classe 2: {class2_qtd}\n- Classe 3: {class3_qtd}')
        return

    instance_class = np.amin(individual_instance)
    return instance_class


def manhattan(class1_center, class2_center, class3_center, data, individual_instance=None):
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
        idx = np.argmin(distances)  # retorna o index do menor item

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    if not individual_instance:
        print(f'\nInstâncias pela classificadas pela média Euclidiana:\n- Classe 1: {class1_qtd}'
              f'\n- Classe 2: {class2_qtd}\n- Classe 3: {class3_qtd}')
        return

    instance_class = np.amin(individual_instance)
    return instance_class


def chebyshev(class1_center, class2_center, class3_center, data, individual_instance=None):
    class1_qtd = 0
    class2_qtd = 0
    class3_qtd = 0

    len_dte = data.shape[0]

    for i in range(0, len_dte):
        """
        Chebyshev
        """
        distances = np.array([abs((class1_center - data[i][0:4])).max().sum(),
                              abs((class2_center - data[i][0:4])).max().sum(),
                              abs((class3_center - data[i][0:4])).max().sum()])

        idx = np.argmin(distances)  # retorna o index do maior item

        if idx == 0:
            class1_qtd += 1
        elif idx == 1:
            class2_qtd += 1
        else:
            class3_qtd += 1

    if not individual_instance:
        print(f'\nInstâncias pela classificadas pela média Euclidiana:\n- Classe 1: {class1_qtd}'
              f'\n- Classe 2: {class2_qtd}\n- Classe 3: {class3_qtd}')
        return

    instance_class = np.amin(individual_instance)
    return instance_class
