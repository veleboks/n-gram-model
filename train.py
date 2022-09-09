import argparse
import N_gram
import re

with open('belkin.txt') as f:
    raw = f.read()

raw = raw.lower().replace('ё', 'e')
clean = re.sub("(?!(?<=\w)[-']\w)\W", ' ', raw, flags = re.U)
clean = ' '.join(clean.split())

with open('clean_data.txt', 'w') as f:
    f.write(clean)

data = [clean.split()]

model = N_gram.N_gram(2)

model.fit(data)

for i in range(10):
    print(model.generate())
