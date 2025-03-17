import re

regex_pattern = r"\b[,.]"
txt = ["The rain, in. Spain", "100,000,000.000"]
for s in txt:
    x = re.split(regex_pattern, s)
    print("\n".join(x))