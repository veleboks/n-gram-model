import argparse
import N_gram
import re

def clean_text(raw):
    clean = raw.lower().replace('ё', 'e')
    clean = re.sub("(?!(?<=\w)[-']\w)\W", ' ', clean, flags = re.U)
    clean = ' '.join(clean.split())
    return clean

with open('data/belkin.txt') as f:
    raw = f.read()

clean = clean_text(raw)

# with open('clean_data.txt', 'w') as f:
    # f.write(clean)

data = [clean.split()]

model = N_gram.N_gram()

model.fit(data)

for i in range(10):
    print(model.generate())
