# LCG
def random():
    class LCG:
        def __init__(self, seed, a, c, m):
            self.seed = seed
            self.a = a
            self.c = c
            self.m = m

        def rand(self):
            self.seed = (self.a * self.seed + self.c) % self.m
            return self.seed / self.m


    lcg = LCG(seed=1234, a=1664525, c=1013904223, m=2**32)

    rand = lcg.rand()
    rand_int = int(rand*6)
    return rand_int 