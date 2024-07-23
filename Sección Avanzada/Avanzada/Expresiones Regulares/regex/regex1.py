import re

text = "Mi correo es don_wea73@pucv.mail.cl y el tuyo es el_xuxeta24@puc.mail.cl"
pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'

matches = re.findall(pattern, text)
print(matches)