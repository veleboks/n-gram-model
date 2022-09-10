from argparse import ArgumentParser
import pickle
from N_gram import N_gram, preprocess

parser = ArgumentParser(description='Generate some text')

parser.add_argument('--model', \
                    default='model.pkl', \
                    type=str, \
                    help='filename for load a model')

parser.add_argument('--prefix', \
                    default=None, \
                    type=str, \
                    help='begin of a sequence')

parser.add_argument('--length', \
                    default=10, \
                    type=int, \
                    help='length of a sequence')

parser.add_argument('--random-seed', \
                    default=None, \
                    type=int, \
                    help='random seed for a model')

args = parser.parse_args()

with open(args.model, 'rb') as f:
    model = pickle.load(f)

if args.random_seed is not None:
    model.set_random_seed(agrs.random_seed)

if args.prefix is not None:
    prefix = preprocess(args.prefix)
    print(model.generate(prefix=prefix, iters=args.length))
else:
    print(model.generate(iters=args.length))

