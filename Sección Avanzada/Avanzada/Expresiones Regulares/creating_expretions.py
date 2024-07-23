import re

texto = "Moshi moshi, mi número es: +569 92769504"

pattern = r'\+\d{2,3}\s\d{8,9}'

reemplazo = re.sub(pattern,"(Número oculto)",texto)

print(reemplazo)