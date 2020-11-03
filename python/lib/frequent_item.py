import random
from .fp_growth_plus import Fp_growth_plus

class Frequent_item:
    def __init__(self):
        pass

    @staticmethod
    def gen_group_X(data):
        source = data[::-1]
        group = []
        while source:
            g = []
            n = random.randrange(2, 5)
            while source and n > 0:
                g.append(source.pop())
                n -= 1
            group.append(g)
        return group

    @staticmethod
    def gen_group(data):
        group = []
        g = []
        t = 0
        wait = 3000
        for x in sorted(data, key=lambda x: x["time"]):
            time = x["time"]
            action = x["action"]
            if time - t > wait:
                if g: group.append(g)
                g = [action]
            else:
                g.append(action)
            t = time
        if g: group.append(g)
        return group

    @staticmethod
    def calc(data):
        min_support = 2
        min_conf = 0.5

        # print(data)
        fpgp = Fp_growth_plus()
        rule_list = fpgp.generate_R(data, min_support, min_conf)
        # print(rule_list)
        res = [[list(d[0]), list(d[1]), d[2], d[3]] for d in rule_list]
        return res