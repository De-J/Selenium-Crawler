p = {'a':1, 'b':2, 'c':3}
    for value in p.values():
        tf.write(value)


if __name__ = "__main__":
    with open(Searches.txt, 'w') as tf:
        for key in d.keys():
            tf.write(str(key))
            tf.write('\t\t\t')
        print('\n')
