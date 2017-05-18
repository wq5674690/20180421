#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os,sys
import re
from datetime import datetime

# now=datetime.now()
# print(now)

l = [6, 1,2,2,2,3,1, 2, 2, 3, 4, 5]
s = set(l)
c = [i for i in s] #python的列表生成式
print (c)