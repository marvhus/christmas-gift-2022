from datetime import datetime as dt;a=print;b=int;e=chr;h=hex
if h(dt.today().day+16)<"29":
    a(''.join([e((b('69177f648589309478ae71cf865275e9304a84337fdd30f0879c7142791c84e530eb71b430de761b75ef875f30637d237f8a8258754d3021743871af8917835b3e5b'[i:i+2],16)-16)%255) for i in range(0,132,4)]))
else:
    a(''.join([e((b('5d297594821c82de898a301c53ec78fb823c79a1833184627d9b71bb83b331c3'[i:i+2],16)-16)%255) for i in range(0,64,4)]))