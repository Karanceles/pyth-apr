import re

text = "Las fechas son 01/12/2022 y 25/05/21, pero no 30/02/2022."
pattern = r'\b\d{2}/\d{2}/\d{4}\b'

matches = re.findall(pattern, text)
print(matches)