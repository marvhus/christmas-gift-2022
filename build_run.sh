#!/bin/bash

set -xe

python3 main.py config.gift
chmod u+x gift.py
./gift.py
