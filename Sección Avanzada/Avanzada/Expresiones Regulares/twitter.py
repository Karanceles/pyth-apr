import re

url = input("URL: ").strip()
# .sub can replace by the second string parameter
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(2)) ## can use group(1) if (?:www\.) isn't capturing