import csv
import os
from pprint import pprint
from threading import Thread


def teskarisonlar(son):
    def teskarison(sonn):
        tson = int(str(sonn)[::-1])
        print(tson)

    thraeds = []

    for i in son:
        thread = Thread(target=teskarison, args=(i,))
        thread.start()

        for thread in thraeds:
            thread.join()


if __name__ == '__main__':
    son = map(int, input("Son kiriting: ").split())
    teskarisonlar(son)
