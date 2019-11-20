#!/usr/bin/python

import re
import string

# charset
cs = string.ascii_uppercase

# regex vertical/horizontal
rv = ['R+D',
      '[^WORK]*ING?',
      '.*[IN].*',
      'C{0}N[NECT]*']

rh = ['.(LN|K|D)*',
      '([MBERS]*)\1',
      '(ENG|INE|E|R)*',
      '[LINKED]*IN']

# candidate matrix
cm = [[set() for _ in rh] for _ in rv]
for i, r in enumerate(rh):
    for a in cs:
        for b in cs:
            for c in cs:
                for d in cs:
                    if re.match(r+'$', a+b+c+d):
                        cm[i][0].add(a)
                        cm[i][1].add(b)
                        cm[i][2].add(c)
                        cm[i][3].add(d)

# answer matrix
am = [[set() for _ in rh] for _ in rv]
for j, r in enumerate(rv):
    for a in cm[0][j]:
        for b in cm[1][j]:
            for c in cm[2][j]:
                for d in cm[3][j]:
                    if re.match(r+'$', a+b+c+d):
                        am[0][j].add(a)
                        am[1][j].add(b)
                        am[2][j].add(c)
                        am[3][j].add(d)

for a in am: print(a)
