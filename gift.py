from datetime import datetime as dt;a=print;b=int;e=chr
if hex(dt.today().day+16)<"29":
    for i in range(0,132,4):
        print(chr((int('695f7f3685e6303e78247174869b7551308c84f67fe3303787dd718b7960844930e07130303a76ac752e878630ca7de77f978236751330ab743c716f895b838e3e22'[i:i+2],16)-16)%255), end='')
else:
    a(''.join([chr((int('5d5275ae8215822b89d03093533f785782d7793b832284d97db1713e833331a8'[i:i+2],16)-16)%255) for i in range(0,64,4)]))