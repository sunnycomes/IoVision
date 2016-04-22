#!/bin/bash

python generate.py
scp -r build/* root@ipv6.scj.suncaijun.cn:/usr/share/nginx/html
scp -r build/* root@ipv4.vps100.suncaijun.cn:/usr/share/nginx/html
