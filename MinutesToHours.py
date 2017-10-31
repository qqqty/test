#!/usr/bin/env python3



import sys

def Hours():
    try:
        num = int (sys.argv[1])
        
        if num < 0 :
            raise ValueError ('ValueError? Input number cannot be negative')

        h, m = divmod(num, 60)

        print ("{} H, {} M".format(h, m))
     
    except ValueError:
        print ('ValueError? Input number cannot be negative')






Hours()
