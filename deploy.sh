#!/bin/bash

python generate.py 
scp -r build/* root@ipv4.suncaijun.cn:/usr/share/nginx/www/
