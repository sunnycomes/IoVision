#!/bin/bash

python generate.py 
scp -r build/* root@ipv6.suncaijun.cn:/usr/share/nginx/html
