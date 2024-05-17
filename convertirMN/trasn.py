from googletrans import Translator




trad = Translator(src="es",
    dest="ja")
tx = input("ingrese el texto :")
resultado = trad.translate(tx)
print(resultado)