'''
def funk(a):  
    for i in set(a):
        c = 0
        for f in a:
            if i == f:
                c += 1
        print(i, '-', c)

a = input()
funk(a)
'''

def funk(a):
    sk = {}
    for i in a:
        sk[i] = sk.get(i, 0) + 1
    for i, j in sk.items():
        print(i, '-', j)

a = input()
funk(a)