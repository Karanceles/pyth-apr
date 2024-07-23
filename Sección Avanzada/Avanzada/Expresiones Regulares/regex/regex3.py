import re

text = "Ana y Alberto fueron a Atenas, pero Ana no vio a Alberto."
pattern = r'\bA\w*\b'

matches = re.findall(pattern, text)
print(matches)