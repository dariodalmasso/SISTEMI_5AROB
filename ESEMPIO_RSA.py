import math

def main():
    p = 131
    q = 479

    n = calcola_prodotto(p,q)
    print(n)
    m = mcm_fattori(p,q)
    print(m)
    c = scegli_numero(m)
    print(c)
    
    


def calcola_prodotto(p,q):
    m = p* q
    return m

def mcm_fattori(p,q):
    mcm = math.lcm(p-1,q-1)
    return mcm


def scegli_numero(m):
    c = 1
    k = 0
    while (c < 1 and c > m):
        if (math.gcd(c,m) == 1):
            k += 1
    return c
            

        




if __name__ == '__main__':
    main()