import re

text = "Este es un ejemplo de URL: https://open.spotify.com y también podemos visitarlo"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" # ? encuentra 0 o 1 coincidencia left (binario)

result = re.findall(pattern,text)

print(result)