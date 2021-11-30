def creer_pile():
    """ Créé une pile vide
    :return: Une pile vide représentée par la liste vide
    """
    return []


def est_vide(p):
    """ Teste si une pile est vide
    :param p: Une pile
    :return: True si p est vide, False sinon
    """
    return p == []


def empiler(p, e):
    """ Empile un élément au sommet d'une pile
    :param p: Une pile
    :param e: Un élément
    :return: None
    :Effets: Empile e au sommet de p
    """
    p.append(e)


def depiler(p):
    """ Dépile un élément au sommet d'une pile et le renvoie
    :param p: Une pile
    :return: L'élément au sommet de la pile
    :Précondition: p est non vide
    """
    assert not est_vide(p), "Impossible de dépiler une pile vide"
    return p.pop()


def afficher_pile(p):
    """ Affiche le contenu d'une pile
    :param p : Une pile
    :return: None
    """
    print("-" * 20)
    for element in p[::-1]:
        print("|" + " " * 18 + "|")
        print("|" + str(element).center(18) + "|")
        print("|" + " " * 18 + "|")
        print("-" * 20)
    print("-" * 20)
