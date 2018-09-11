# -*- coding: utf-8 -*-
from random import randrange


loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))
print loops
for i in loops:
    print i


loop = (randrange(2, 6) for x in range(10))

print(loop)

for x in loop:
    print x












