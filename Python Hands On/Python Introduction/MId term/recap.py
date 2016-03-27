from google.translate import Translator

translate = Translator().translate
print (translate("Mani sauc Pēteris", lang_to="en"))

print (translate("Mani sauc Pēteris", lang_to="ru").encode('utf-8'))

print (translate("Меня зовут Петр"))

