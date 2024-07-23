import re

text = "reemplazando todas las vocales por asteriscos"
new_text = re.sub("[AEIOU]", "*", text,flags=re.IGNORECASE)
print(new_text)