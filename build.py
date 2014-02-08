import json
from collections import Counter

from progressbar import ProgressBar

from powerpassword import get_chr, triplet_generator

def generate_build(srcs):
    # Calculate the total amount of lines first
    lines_total = 0
    for src in srcs:
        with open(src) as datafile:
            for line in datafile:
                lines_total += 1

    lines_added = 0
    chr_pairs = Counter()
    pbar = ProgressBar(maxval=lines_total).start()
    for src in srcs:
        with open(src) as datafile:
            for line in datafile:
                lines_added += 1
                line = line.replace("\r", '').replace("\n", '')
                for triplet in triplet_generator(line):
                    chr_pairs[repr(triplet)] += 1
                pbar.update(lines_added)
    pbar.finish()
    return chr_pairs

def include_only_top(chr_pairs, percentage):
    return chr_pairs.most_common(int(percentage * len(chr_pairs)))

with open('builds/common_passwords.json', 'w') as outfile:
    json.dump(dict(include_only_top(generate_build([
        'datasets/passwords.txt'
    ]), 0.1)), outfile)