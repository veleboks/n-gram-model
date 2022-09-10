from argparse import ArgumentParser
import os, glob
from N_gram import N_gram, preprocess
import pickle

parser = ArgumentParser(description='Train a n-gram model for text generation')

parser.add_argument('--input-dir', \
                    type=str, \
                    help='dir with a data for model')
parser.add_argument('--model', \
                    type=str, \
                    default='model.pkl', \
                    help='filename for save a model')

args = parser.parse_args()

raw = []

if args.input_dir is not None:
    files = glob.glob(os.path.join(args.input_dir, '*'))
    for filename in files:
        with open(filename) as f:
            raw.append(f.read())
else:
    raw = [input()]

data = []
for sample in raw:
    data.append(preprocess(sample))

model = N_gram()

model.fit(data)

with open(args.model, 'wb') as f:
    pickle.dump(model, f)

