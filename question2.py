
Chapitre=['NUMERATION ET CODAGE','LANGAGE PYTHON', 'BOOLEENS','TYPES CONSTRUITS','ALGORITHMES', 'RESEAUX', 'ARCHITECTURE DES ORDINATEURS']

html = open("quest2-file.html", "w", encoding = "utf-8")

prefix = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Question 2</title>
        <meta charset="utf-8"/>
    </head>
    <body>
"""

body = "<ol>"
for chap in Chapitre:
    body += "   <li>"+chap+"<br/><p>Les thèmes abordès dans cette partie:</p></li>"
body += "</ol>"

suffix = """
    </body>
</html>
"""
print(prefix, body, suffix, sep="", file=html)
html.close()

print("ecriture réussite")