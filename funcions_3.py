#The code prints hello in multiple languages
def language (lang) :
    if lang == "es" :
        return ("Hola")
    elif lang == "fr" :
        return ("Bonjour")
    elif lang == "kl" :
        return ("nuqneH")
    elif lang == "pt" :
        return ("Bom dia")
    elif lang == "it" :
        return ("Ciao")
    else:
        return ("We don't have this language")

print(language("es"),"Roque")
print(language("fr"),"Roque")
print(language("kl"),"Roque")
print(language("pt"),"Roque")
print(language("it"),"Roque")