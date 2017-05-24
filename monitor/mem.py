#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 
import time
import psutil

def CPU():
    try:
        cpuer = psutil.cpu_percent()
        print (cpuer)
    except:
        traceback.print_exc()

CPU()