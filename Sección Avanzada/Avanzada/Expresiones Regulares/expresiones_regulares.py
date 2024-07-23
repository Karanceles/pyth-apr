import re # we use RegEx as well, despite not being from python oficially

# texto para ser analizado
texto ='''Moshi moshi, esta es la 1ra cadena de texto
Cómo estás tr@esma, aquí la 2da línea
Y aquí la 3ra línea, somos jaleros expertos ya'''

# Busqueda simple: .findall looks for every term//.search goes for 1 
#resultado = re.findall("la",texto)

# \d --> looking for hexadecimal numbers
# \D --> looking for everything (TODO) except hexadecimal numbers
#resultado = re.findall(r"\d",texto)

# \w --> looking for alphanumeric characters [a-z A-Z 0-9 _]
# \W --> looking for TODO except alphanumeric characters
#resultado = re.findall(r"\w",texto)

# \s --> looking for blank spaces, tabs, linebreaks
# \S --> looking for TODO except blank spaces, tabs, linebreaks
#resultado = re.findall(r"\s",texto)

# . --> looks for TODO but linebreaks
# \n --> looking for linebreaks
#resultado = re.findall(r'\n',texto)

# \ --> cancel special characters (¡BUM!)
# wana search dots?? \. --> literally cancels its previous functionality
#resultado = re.findall(r'\.',texto) --> how many dots are there

# making a chain that looks up for a number, followed by a dot and a blank space
#resultado = re.findall(f'\d\.\s',texto)

# ^ --> finds the begining of a line + ^word --> finds a certain word at a begining line
#resultado = re.findall(f'^',texto,flags=re.M) # flags=re.M = Multi line // re.MULTILINE
# flags=re.IGNORECASE = ignores mayus/minus
# re.DOTALL -> recognizes any characters + new line

# $ --> finds the end of a line
#resultado = re.findall(f'línea$',texto,flags=re.M)

# {n} --> finds n times the left value
#resultado = re.findall(f'\d{3}\s',texto) # 3 times a numerical digit + an space or smtn

# {n,m} --> at least n, max m
# digit => \d{2,4}
# d char => d{2,4}
# group => (ab){2,4}
# group times => (adc){2} ==> find 'adcadc' but just returns 'adc'
# any char times => [ab]{2} ==> 'aa','ab','bb','ba'
#resultado = re.findall(r'{2,4}',texto)

# | search a thing or another and returns both of them
resultado = re.findall(f'\d{2,4}|Hola',texto)

# (?:) non-capturing version group

# * affects the left char => find 0 or more events // 
# + 1 or more reps
# ? 0 or 1 rep

print(resultado)