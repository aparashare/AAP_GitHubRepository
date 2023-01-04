#!/usr/bin/env python3                      # shebang, Execute with a Python interpreter, using the env program search path to find it
# Loops

for x in range(6):                          # print 0,1,2,3,4,5
    print("Range: %d" %x)

for x in range(3,7):                        # print 3,4,5,6
    print(x)

for x in range(3,7,2):                      # print 3,5 start by 3, end by 7, increment by 2 --> ending <7 (DOES not consider <=7)
    print(x)