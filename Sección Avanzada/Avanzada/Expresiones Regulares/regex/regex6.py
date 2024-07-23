import re

text = "La fecha es 23/06/2023 y el teléfono es +1-555-666-5600"

pattern = r"\d{2}/\d{2}/\d{4}"

replacement = "Fecha oculta"

new_text = re.sub(pattern,replacement,text)

print("Texto modificado:", new_text)