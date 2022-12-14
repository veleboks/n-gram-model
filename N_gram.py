from collections import defaultdict, Counter
import random
import re

def preprocess(raw):
    clean = raw.lower().replace('ё', 'e')
    clean = re.sub("(?!(?<=\w)[-']\w)\W", ' ', clean, flags = re.U)
    return clean.split()

class N_gram:
    def __init__(self, prefix_size=2):
        self.prefix_size = prefix_size
        self.next_word = defaultdict(Counter)
    def set_random_seed(self, random_seed):
        random.seed(random_seed)
    def fit(self, data):
        # counting words for every n-gram
        for sample in data:
            for i in range(len(sample) - self.prefix_size):
                prefix = tuple(sample[i:i+self.prefix_size-1])
                word = sample[i+self.prefix_size-1]
                self.next_word[prefix][word] += 1
        # print(self.next_word)

    def __generate_one_word(self, prefix):
        # there isn't a next word
        if len(self.next_word[prefix]) == 0:
            return None
        choice = random.choices(*zip(*self.next_word[prefix].items()))[0]
        return choice
    def __generate_random_n_gram(self):
        return list(random.choice(list(self.next_word.keys())))

    def generate(self, prefix=None, iters=10):
        if prefix is not None:
            res = prefix
        else:
            res = self.__generate_random_n_gram()
        for _ in range(iters):
            # get last n-gram
            prefix = tuple(res[-self.prefix_size+1:])
            word = self.__generate_one_word(prefix)
            if word is None:
                break
            res += [word]
        # print(res)
        return ' '.join(res)
