#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import base64

f = open(sys.argv[1],"rb")
dat = f.read()
i = base64.b64encode(dat)

text = open(sys.argv[1] + ".txt","wb")
text.write(i)
text.close()
