
Chapitre=['NUMERATION ET CODAGE','LANGAGE PYTHON', 'BOOLEENS','TYPES CONSTRUITS','ALGORITHMES', 'RESEAUX', 'ARCHITECTURE DES ORDINATEURS']

chap0=['Compter en base b','Codage des nombres entiers','Codage des nombres décimaux','Codage du texte']
chap1=['Les types de variables','Les tests conditionnels','Les chaines de caractères','La boucle tant que','Les fonctions']
chap2=['Différentes portes logiques','Fonctions bouléennes','Circuits combinatoires']
chap3=['Les t-uples','Les listes','Les dictionnaires']
chap4=['Tri par insertion','Tri par sélection','Dichotomie']
chap5=['Liaisons entre les ordinateurs','Réseau local : ethernet','Réseau de réseaux : internet']
chap6=['Historique, Von Neumann','Microprocesseur','Little Man Computeur : assembleur','Système d \' exploitation']

html = open("quest3-file.html", "w", encoding = "utf-8")

prefix = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Question 2</title>
        <meta charset="utf-8"/>
    </head>
    <body>
"""

body = "<ol>"
for k in range(len(Chapitre)):
    body += "   <li>"+Chapitre[k]+"<br/><p>Les thèmes abordès dans cette partie:</p><ul>"
    for content in globals()["chap"+str(k)]:
        body += "<li>"+content+"</li>"
    body += "</ul>"
body += "</ol>"

suffix = """
    </body>
</html>
"""
print(prefix, body, suffix, sep="", file=html)
html.close()
print("ecriture réussite")