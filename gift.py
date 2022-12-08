
from datetime import datetime as dt
a=print
b=int
e=chr
if hex(dt.today().day+16) < "29":
    c=''
    d='697f85307871867530847f3087717984307130767587307d7f827530747189833e'
    for i in range(0, 66, 2):
        c += e(b(d[i:i+2], 16) - 16)
    a(c)
else:
    c=''
    d='5d75828289305378827983847d718331'
    for i in range(0, 32, 2):
        c += e(b(d[i:i+2], 16) - 16)
    a(c)
