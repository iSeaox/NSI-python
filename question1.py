html = open("quest1-file.html", "w", encoding = "utf-8")

prefix = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <title>Question 1</title>
        <meta charset="utf-8"/>
    </head>
    <body>
"""

body = "<p>Woaw un jolie paragraphe</p>"

suffix = """
    </body>
</html>
"""
print(prefix, body, suffix, sep="", file=html)
html.close()