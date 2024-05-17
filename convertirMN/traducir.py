from translate import *

trad = Translator(
    from_lang="spanish",
    to_lang="Japanese")

tx = input("ingrese el texto :")
resultado = trad.translate(tx)
print(resultado)