#!/bin/bash

python generate.py
scp -r build/* root@ipv4.vps100.suncaijun.cn:/usr/share/nginx/html
scp -r build/* root@ipv4.vps3.suncaijun.cn:/usr/share/nginx/html
