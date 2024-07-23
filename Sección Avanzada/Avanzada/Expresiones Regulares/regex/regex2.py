import re

text = "Mis números son (153) 465-7711 y 554-2755. No coinciden: 12-3456-7890 y 1234567890"
pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'

matches = re.findall(pattern, text)
print(matches)