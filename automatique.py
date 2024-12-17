import math
import fractions
from time import clock
print('Ceci est la version fonctionnelle du calculateur de probabilités pour cases.')
Work, Keep = [1], True
def first():
    global Work
    Unites = int(math.fabs(Work[len(Work) - 2] - Work[len(Work) - 1]) + 1)
    while (Work[len(Work) - 2] + Work[len(Work) - 1]) > 2 and Work[len(Work) - 3] < 6:
        if Work[len(Work) - 2] == 1:
            Work[len(Work) - 1] -= 1
            Work[len(Work) - 3] += 1
        else:
            Work[len(Work) - 2] -= 1
            Work[len(Work) - 3] += 1
        Unites += int(math.fabs(Work[len(Work) - 2] - Work[len(Work) - 1]) + 1)
    return Unites
def second(rang):
    global Work
    global Keep
    if Work[len(Work) - (rang - 1)] > 1 and Work[len(Work) - rang] < 6:
        Work[len(Work) - rang] += 1
        Work[len(Work) - (rang - 1)] -= 1
        sOver = 0
        for d in range(1,rang):
            sOver += Work[len(Work) - d] - 1
            Work[len(Work) - d] = 1
        d = 1
        while sOver > 4:
            Work[len(Work) - d] += 5
            sOver -= 5
            d += 1
        Work[len(Work) - d] += sOver
    else:
        Keep = False
clock()
while True:
    print('Résultat de la somme (numéro de la case)')
    Case = int(input())
    while Case < 1:
        print('Saisie invalide!')
        Case = int(input())
    Proba = fractions.Fraction()
    tdp = clock()
    for Termes in range(1, Case + 1):
        Work = [1] * Termes
        Over = Case - Termes
        if Over != 0 and Over / Termes <= 5:
            del Work[int((math.fabs(len(Work) - math.ceil(Over / 5)) + len(Work) - math.ceil(Over / 5)) / 2):len(Work)]
            if Over % 5 > 0:
                Work += [Over % 5 + 1]
            Work += [6] * (Over // 5)
        Nombre = 0
        Keep = True
        rang = 4
        if Case / Termes > 6:
            Nombre = 0
        elif Termes == 1:
            Nombre = 1
        elif Termes == 2:
            Nombre = int(math.fabs(Work[len(Work) - 2] - Work[len(Work) - 1]) + 1)
        elif Termes == 3:
            Nombre = first()
        else:
            Nombre += first()
            while rang <= Termes:
                second(rang)
                if Keep == False:
                    rang += 1
                    Keep = True
                else:
                    Nombre += first()
                    rang = 4
        Proba = Proba + fractions.Fraction(Nombre,6 ** Termes)
    print('La probabilité correspondante est ', Proba)
    print(str(clock() - tdp) + ' secondes.')
    print('Redémarrage.')
