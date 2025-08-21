from random import *
from rgps import *

def soan_de(a, b):
    #ax + b = 0
    #x = -b/a
    
    de = f"\\begin{{ex}} \n Phương trình $"

    if (a == 1):
        de += "x"
    elif (a == -1):
        de += "-x"
    else:
        de += f"{a}x"

    if (b > 0):
        de += f"+{b}"
    else:
        de += f"{b}"
    
    de += f"=0$ có nghiệm là ? \n \\choice {{{rgps(b,a)}}} \n {{{rgps(-a,b)}}} \n {{\\True {rgps(-b, a)}}} \n {{{rgps(a,b)}}}  \n \\loigiai{{}} \n \\end{{ex}} \n \n"
    return de


de = open("./cau_hoi.tex", "w", encoding="utf8")

num = input("Ban muon tao bao nhieu cau hoi?: ")

for i in range(0, int(num)):
    a = randint(-10, 10)
    b = randint(-10, 10)

    while a == 0 or b == 0 or a == b or a == -b:
         a = randint(-10, 10)
         b = randint(-10, 10)
    de.write(soan_de(a,b))

de.close()
