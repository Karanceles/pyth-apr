import random
import re

pass_code = r"\w"
len_pass = int(input("Lenght of password: "))
a = "".join(random.sample(pass_code,len_pass))
print(f"Random pass: {a}")
