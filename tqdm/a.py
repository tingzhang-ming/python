# encoding: utf-8
from tqdm import tqdm, trange
from time import sleep


def t1():
    for i in tqdm(range(1000)):
        sleep(0.01)


def t2():
    for i in trange(100):
        sleep(0.1)


def t3():
    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        sleep(2)
        pbar.set_description("processing %s" % char)
# processing d: 100%|██████████| 4/4 [00:08<00:00,  2.00s/it]


def t4():
    with tqdm(total=100) as pbar:
        for i in range(100):
            sleep(0.1)
            pbar.update(1)


if __name__ == '__main__':
    t4()
