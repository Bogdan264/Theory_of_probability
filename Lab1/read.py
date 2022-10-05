def read(txt):
    f = open(txt, 'r')
    return [int(line.strip()) for line in f]