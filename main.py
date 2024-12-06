#### Imports et définition des variables globales
"""importation des modules"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='utf8') as f:
        r = csv.reader(f, delimiter=';')
        l = list(r)
    l_int = []
    for line in l:
        l_int.append([int(i) for i in line])
    return l_int

def get_list_k(data, k):
    """retourne la k-ième liste"""
    return data[k]

def get_first(l):
    """retourne le premier élément d'une liste"""
    return l[0]

def get_last(l):
    """retourne le dernier élément d'une liste"""
    return l[-1]

def get_max(l):
    """retourne la valeur maximum d'une liste"""
    return max(l)

def get_min(l):
    """retourne la valeur minimum d'une liste"""
    return min(l)

def get_sum(l):
    """retourne la somme des valeurs d'une liste"""
    return sum(l)


#### Fonction principale


def main():
    """fonction principale"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
